import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dotenv
from process.modules.Camera_YPet_v2 import CameraPet
import time

def main():
    print("Initializing CameraPet...")
    # Initialize with camera ID 2
    camera_pet = CameraPet(camera_id=0, model_path=os.getenv("MODEL_PATH_CLASSIFICATION"))
    
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
    # camera_pet.release_camera()
    print("Done!")

if __name__ == "__main__":
    main()