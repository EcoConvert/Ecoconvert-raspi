import cv2
import numpy as np
import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="/home/capstone/app/Models/mobilenet_fpn_640/mobilefpn640.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Input Details:", input_details)
print("Output Details:", output_details)

# Load labels
with open("/home/capstone/app/Models/mobilenet_fpn_640/label_map.pbtxt", "r") as f:
    labels = {}
    for line in f:
        if "id" in line:
            class_id = int(line.split(":")[1].strip())
        if "name" in line:
            class_name = line.split("'")[1]
            labels[class_id-1] = class_name

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the image
    input_shape = input_details[0]['shape']
    input_tensor = cv2.resize(frame, (input_shape[1], input_shape[2]))
    input_tensor = np.expand_dims(input_tensor, axis=0)
    input_tensor = (np.float32(input_tensor) - 127.5) / 127.5  # Normalize to [-1, 1]

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], input_tensor)

    # Run inference
    interpreter.invoke()

    # Get the output tensors
    scores = interpreter.get_tensor(output_details[0]['index'])[0]
    boxes = interpreter.get_tensor(output_details[1]['index'])[0]
    num_detections = int(interpreter.get_tensor(output_details[2]['index'])[0])
    classes = interpreter.get_tensor(output_details[3]['index'])[0]

    # Process detections
    for i in range(num_detections):
        if scores[i] > 0.5:  # Confidence threshold
            class_id = int(classes[i])
            class_name = labels.get(class_id, f"Class {class_id}")
            box = boxes[i]
            
            # Denormalize bounding box coordinates
            h, w, _ = frame.shape
            ymin, xmin, ymax, xmax = box
            xmin, ymin, xmax, ymax = int(xmin * w), int(ymin * h), int(xmax * w), int(ymax * h)

            # Draw bounding box and label
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
            label = f"{class_name}: {scores[i]:.2f}"
            cv2.putText(frame, label, (xmin, ymin - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
