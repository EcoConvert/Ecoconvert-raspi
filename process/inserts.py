from process.modules import Camera # from main 

def test_capture():
    print("run inserts")
    cam = Camera(0)
    cam.init_camera()
    
    labels = cam.load_labels()
    print(labels)   

    inference = cam.capture_and_infer()
    print(inference)

if __name__ == "main":
    test_capture()
