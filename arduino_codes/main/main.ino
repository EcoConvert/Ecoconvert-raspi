// PLEASE PLEASE GAMIT KAYO NG MODULAR FUNCTIONS.
// IF POSSIBLE PA GAYA NG STRUCTURE NG NASA HYDROWATCH,
// PERO KUNG HINDI KAYA, BASTA NAKA MODULAR FUNCTIONS.
// puro .h files lang wala nang cpp
// stepperOperations.h
// lightsOperations.h
// globalVars.h
// ...
// etc.

int incomingByte = 0; // for incoming serial data

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop()
{
    // send data only when you receive data:
    if (Serial.available() > 0)
    {
        incomingByte = Serial.read();
        // for strings, we need to process it.
        // incoming bytes get replaced by the new bytes
        // if there is more than one,
        // The last one will be the incomingBytes.
        switch (incomingByte)
        {
        case '0':
            // Standby Mode
            Serial.write("off");
            digitalWrite(LED_BUILTIN, LOW);
            break;

        case '1':
            // Insert Mode
            Serial.write("on");
            digitalWrite(LED_BUILTIN, HIGH);
            break;

        case '2':
            // Processing Mode
            break;

        case '3':
            // Retrieve Mode
            break;

        default:
            // Error case: Handle unexpected input
            Serial.println("Invalid input received.");
            break;
        }
    }
}