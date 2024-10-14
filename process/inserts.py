import logging

from modules.Camera import Camera


def test_capture():
    try:
        cam = Camera(2)
        cam.init_camera()

        labels = cam.load_labels()
        print("Labels:", labels)

        inference = cam.capture_and_infer()
        print(inference)

        if inference.lower() == "metal":
            print("Metal")

    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        cam.release_camera()


if __name__ == "__main__":
    test_capture()
