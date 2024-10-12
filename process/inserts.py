from modules import Camera

def test_capture():
    print("run inserts")
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)   

    inference = cam.capture_and_infer()
    print(inference)
