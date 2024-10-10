from modules.Camera import Camera

def test_capture():
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)   

    inference = cam.capture_and_infer()
    print(inference)
if __name__ == "__main__":
    test_capture()