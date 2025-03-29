from process.modules.CameraBase import CameraBase

### DITO ILALAGAY YUNG INFERENCE IMPORTANT IMPORTANT IMPORTANT!!!
class CameraPet(CameraBase):
    def __init__(self, camera_id=0): #CHANGE THE CAM ID DEPENDS ON PORT NUMBER....
        super().__init__(camera_id)
    
    def infer(self):
        print("infer")
        inferance = True
        return inferance 