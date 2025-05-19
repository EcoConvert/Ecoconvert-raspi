const int led = 13;
const int ZERO = 0;
const int VAR = 500; 

void SerialCommand(String& Command, const int& pin, int rep, int del = 200) {
  // Serial.print("State: ");
  if (Command != "R"){
    // char ardAck[] = "A\n";
    // Serial.flush();
    // Serial.write(ardAck);
    // Serial.println("");
  }  
  for(int i = 0; i < rep; i++) {
      digitalWrite(pin, HIGH);
      delay(ZERO);
      digitalWrite(pin, LOW);
      // Serial.println("one cycle");   
      delay(ZERO);  
  }
}

void GripperEndProcess(){

}

void SUPEndProcess(){
  float value = 120.0;
  char c_string[8];
  dtostrf(value, 6, 2, c_string);
  Serial.write(c_string);
  Serial.write("\n");
  digitalWrite(led, HIGH);
  delay(500);
  digitalWrite(led, LOW );
  delay(500);
}

void state3(int del= 200) {
  delay(ZERO);
  char ecoDone[] = "H\n";
  Serial.flush();
  // Serial.write(ecoDone);
  // Serial.println(""); 
}

void setup() {
 Serial.begin(115200);
 pinMode(led, OUTPUT);
}

void loop() {
 while (Serial.available() > 0)
 {
  String inString = Serial.readString();
  inString.trim();
  if(inString == "0") 
    SerialCommand(inString, led, int(1), int(500));
  else if(inString == "1")
    SerialCommand(inString, led, int(inString.toInt()), int(1000));
  else if(inString == "2"){
        SerialCommand(inString, led, int(inString.toInt()), int(500));
    }
  else if (inString == "3"){
    SerialCommand(inString, led, int(inString.toInt()), int(250));
    state3(int(500));
    }
  else if (inString == "4") 
    SerialCommand(inString, led, int(inString.toInt()), int(500));
  else if (inString == "R") 
    SerialCommand(inString, led, int(2), int(200));
  else if (inString == "F") 
    SerialCommand(inString, led, int(4), int(200));
  else if (inString == "G"){
    SUPEndProcess();
  }
 }
}



