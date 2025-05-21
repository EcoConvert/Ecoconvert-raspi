from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject
from util.state import load_state, save_state, load_state_variables  # Ensure this import is correct

#creates as many signals as needed
class ScreenSignal(QObject):
    show = pyqtSignal(object, object, object)  # All signals emit 3 args
    pet = pyqtSignal(object, object, object)
    sup = pyqtSignal(object, object, object)

# one thread per job, depends if short burst or long running
class InitThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.signal = ScreenSignal() 

    def run(self):
        # check state variables if they have the right variables
        data = load_state_variables() 
        bottle_exist = data["bottle_exist"]
        weight = data["weight"] 

        # init state 
        state = load_state()
        state_map = {0: 1, 
                     1: 2, 
                     2: 3, 
                     3: 5, 
                     4: 8
                     } # refer to the figma board RVM Screens
        screen_index = state_map.get(state, 7)  # iterate over the state_map dictionary to get the screen index  Default to error screen (7) if out of bounds. 
        print(f"Signal emitted: {screen_index}")
        self.signal.show.emit(screen_index, None, None)
        self.signal.pet.emit(None, bottle_exist, None)
        self.signal.sup.emit(None, None, weight)
        # init state variables