from process.modules.Camera_Pet import CameraPet

camera_pet = CameraPet(camera_id=0)

result = camera_pet.infer(timeout=10.0, display=True)

if result:
    print(f'Class: {result["class"]}, Score: {result["score"]}, Reason: {result["reason"]}')

camera_pet.release_camera()