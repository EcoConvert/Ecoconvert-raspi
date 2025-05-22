# src/lcd_interface/screens/welcome_screen.py

from .base_screen import BaseScreen
from .views.ecobrick_view import setup_ui
from logging_config import lcd_logger  
from util.state import save_state_variables, load_state_variables

class EcoScreen(BaseScreen):
    """
    Ecobrick Retrieve screen
    """
    
    def __init__(self, config, parent=None):
        super().__init__(config, parent)  # Inherit from BaseScreen
        self.logger = lcd_logger(self.__class__.__name__)  # Initialize logger for this screen
        self.logger.debug("Initializing admin page")  # Log when EcoScreen is initialized
        setup_ui(self) 
        self.is_bottle_existent = False
        self.ecoB_stored = 0
        self.sup_count = 0.0

        self.sup_cam = True
    def _on_click_home(self):
        self.logger.info("Go Home")        
        self.update_state(0)  # update to standby
        self.parent().setCurrentIndex(0)


    def _on_click_pet_toggle(self):
        self.is_bottle_existent = not self.is_bottle_existent
        self.logger.info(f"PET bottle toggled: {self.is_bottle_existent}")
        self.update_state_var("bottle_exist", int(self.is_bottle_existent))
        self.values_refresh()


    def _on_click_sup_zero(self):
        self.sup_count = 0.0
        self.logger.info("SUP count reset to 0")
        self.update_state_var("weight", self.sup_count)
        self.values_refresh()

    def _on_click_sup_full(self):
        self.sup_count = 525 # or 1 depending on threshold
        self.logger.info(f"SUP: {self.sup_count}")
        self.update_state_var("weight", self.sup_count)
        self.values_refresh()

    def _on_click_ecobrick_reset(self):
        self.ecoB_stored = 0
        self.logger.info(f"Ecobrick Reset to 0")
        self.update_state_var("eco_brick_stored", self.ecoB_stored)
        self.values_refresh()

    def update_state_var(self, key, value):
        self.logger.debug(f"Saving state variable: {key} = {value}")
        save_state_variables(key, value)
   
    def load_values_from_json(self): 
        self.is_bottle_existent = load_state_variables("bottle_exist")
        self.ecoB_stored = load_state_variables("eco_brick_stored")
        self.sup_count = load_state_variables("weight")

    def values_refresh(self):
        self.logger.debug(f"values refreshed")
        self.is_bottle_existent_label.setText((f"{self.is_bottle_existent}"))
        self.is_camera_HIGH_label.setText((f"{self.sup_cam}"))
        self.sup_count_label.setText((f"{self.sup_count }"))
        self.ecoB_stored_label.setText((f"{self.ecoB_stored}"))


## camera add ons
    def _on_click_SupCam_toggle(self):
        self.sup_cam = not self.sup_cam
        self.logger.info(f"SUP: {self.sup_cam}")
        self.values_refresh()

    
    def get_SupCam_state(self):
        return self.sup_cam
        
       