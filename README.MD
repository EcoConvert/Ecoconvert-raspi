### 1. PLEASE CREATE A BRANCH WHERE YOU CAN PLAY AROUND 
 FOR DEPLOYMENT, COMBINE PULL REQUEST WHEN YOU ARE DONE PLAYING AROUND. 
### 2. THE DEPLOYMENT BRANCH SHOULD BE READ ONLY BECAUSE IT WILL BE GIT PULL BY THE INITIAL SCRIPT (FOR NOw IT'S CALLED TEST.SH), 
IF THERE ARE CODES, NONE WILL BE PULLED AND WE WILL MANUALLY MERGE IT. 
DO NOT ATTEMPT TO CODE IN DEPLOYMENT BRANCH  
# ON FIRST RUN DO THESE
### 3. CREATE A VENV NAMED "env" not not venv not .venv not myvenv just env 
 IF NOT THE SCRIPT WILL NOT INSTALL THE DEPENDENCIES. This is a folder that will contain a virtual environment for python. 
### 4. IF INSTALLLING LIBRARIES OUTSIDE OF REQUIREMENTS .TXT 
Run ANY of these commands to update the requirements
`python3 -m pip freeze > requirements.txt`
`python -m pip freeze > requirements.txt`
`pip freeze > requirements.txt`
### 5. CREATE .env FILE. this is a .env file not a directory
this contains sensitive information and information that might change on run time example 
MODEL_PATH = "mobelefpn640.tflite" // this depends on whose PC or raspi is this. 
LABEL_PATH = "label_mp.pbtxt"  

ps always source env/bin/activate