# Ecoconvert

1. Install the necessary requirements.
   I will not make a detailed guide because tensorflow on different OS, it sucks really.
   Just make sure to have
   - tensorflow
   - pyqt5
   - pyserial
     ❌ no need for rpio gpio or gpiozero because serial communication with arduino will do the work.
2. Make sure to have .env file
   note: this is different from (env)ironmenet folder
   .env contains:
   LABEL_PATH="ABSOLUTE PATH OF THE v2_mobilenetfpn_ssd_640label_map.pbtext"
   MODEL_PATH="ABSOLUTE PATH OF THE v2_latest_mobilnet_ssd.tflite"
   SECRET_KEY="JUST YOUR SECRET KEY FOR THE QR GENERATION"
   SERIAL_PORT = "Just where your arduino is plugged in"
3. If you have questions reach out to me
4. The main file is contains high number of comments. Most of it are for me, for the future me if I forgot what I am doing, -Naypes\
5. ignore all other python files on the main directory, the main.py is what will be going inside the deployment branch later.
6. I provide an arduino_codes folder, but if you want to create separate folder for arduino codes, its fine too.
