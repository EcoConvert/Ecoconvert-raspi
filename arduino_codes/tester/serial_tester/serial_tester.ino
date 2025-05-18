//Many thanks to Nick Gammon for the basis of this code
//http://www.gammon.com.au/serial

const int led = 13;

void SerialCommand(String& Command, const int& pin, int rep, int del = 200) {
  Serial.print("State: ");
  Serial.println(Command); 
  if (Command != "R"){
    char ardAck[] = "A";
    Serial.write(ardAck);
    Serial.println("");
  }  
  for(int i = 0; i < rep; i++) {
      digitalWrite(pin, HIGH);
      delay(del);
      digitalWrite(pin, LOW);
      Serial.println("one cycle");   
      delay(del);  
  }
}

void state2() {
  float value = 999.12356;
  char c_string[8];
  dtostrf(value, 6, 2, c_string);
  Serial.write(c_string);
  Serial.println(""); 
}
void state3(int del= 200) {
  delay(del);
  char ecoDone[] = "H";
  Serial.write(ecoDone);
  Serial.println(""); 
}

void setup() {
 Serial.begin(9600);
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
        state2();
    }
  else if (inString == "3"){
    SerialCommand(inString, led, int(inString.toInt()), int(250));
    state3(int(500));
    }
  else if (inString == "4") 
    SerialCommand(inString, led, int(inString.toInt()), int(500));
  else if (inString == "R") 
    SerialCommand(inString, led, int(2), int(200));
  else if (inString == "G") 
    SerialCommand(inString, led, int(3), int(200));
 }
}



