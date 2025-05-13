from src.module.CameraPet import CameraPet

# Path to your TFLite model
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/effnet_gen/effneet_best_test_1_standard.tflite"
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/mobilenetv2_13_25_gen/mobilenetv2_best_test_17_standard.tflite"
# model_path ="/home/untitled/Documents/Coding Repository/python_journey/Capstone/waste-object/runs/classify/pet_bottle_classifier3/weights/best_saved_model/best_float32.tflite"
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/best.tflite"

# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/v8_18_2025_classification_n/weights/best_saved_model/best_float32.tflite"

# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/v8_18_20252_classification_n/weights/best_saved_model/best_float32.tflite"
# Create instance
camera_pet = CameraPet(camera_id=2)

# Run detection + inference
result = camera_pet.infer(timeout=10.0, display=True)

# Print result
if result:
    print(f"Class: {result['class']}, Score: {result['score']}, Reason: {result['reason']}")

# Cleanup
camera_pet.release_camera()
