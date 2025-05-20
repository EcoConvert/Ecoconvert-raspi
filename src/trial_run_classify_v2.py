from process.modules.Camera_YPet import CameraPet
from time import time

# Path to your TFLite model
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/effnet_gen/effneet_best_test_1_standard.tflite"
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/mobilenetv2_13_25_gen/mobilenetv2_best_test_17_standard.tflite"
# model_path ="/home/untitled/Documents/Coding Repository/python_journey/Capstone/waste-object/runs/classify/pet_bottle_classifier3/weights/best_saved_model/best_float32.tflite"
# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/best.tflite"

# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/v8_18_2025_classification_n/weights/best_saved_model/best_float32.tflite"

# model_path = "/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/v8_18_20252_classification_n/weights/best_saved_model/best_float32.tflite"
# Create instance
def main():
    print("Initializing CameraPet...")
    # Initialize with camera ID 2
    camera_pet = CameraPet(camera_id=0, model_path="/home/untitled/Documents/Coding_Repository/python_journey/Capstone/waste-classification/models_train/v8_18_20252_classification_n/weights/best.pt")
    
    print("Learning background...")
    # First learn the background without the bottle
    # Dito naman after mag click ng Insert 1.5L PET Bottle
    camera_pet.prepare_for_detection(display=True)
    
    print("Place the bottle in the green box now")
    # Give user a moment to place the bottle
    # Dito papalitan kapag na click na 'yong Done button'
    time.sleep(2)
    
    print("Starting detection and inference...")
    # Run detection + inference
    result = camera_pet.infer(timeout=10.0, display=True)
    
    # Print result
    if result:
        print(f"Class: {result['class']}, Score: {result['score']:.4f}, Reason: {result['reason']}")
    
    # Cleanup
    print("Cleaning up...")
    camera_pet.release_camera()
    print("Done!")

if __name__ == "__main__":
    main()