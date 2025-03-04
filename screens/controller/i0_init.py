from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject
from util.state import load_state  # Ensure this import is correct

#creates as many signals as needed
class ScreenSignal(QObject):
    show = pyqtSignal(int)  # value it will return
    

# one thread per job, depends if short burst or long running
class InitThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.signal = ScreenSignal() 

    def run(self):
        # init state 
        state = load_state()
        state_map = {0: 1, 1: 2, 2: 3, 3: 5, 4: 8} 
        screen_index = state_map.get(state, 7)  # iterate over the state_map dictionary to get the screen index  Default to error screen (7) if out of bounds. 
        self.signal.show.emit(screen_index)
        print(f"Signal emitted: {screen_index}")

        # init state variables
        