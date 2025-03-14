// // PLEASE PLEASE GAMIT KAYO NG MODULAR FUNCTIONS.
// // IF POSSIBLE PA GAYA NG STRUCTURE NG NASA HYDROWATCH,
// // PERO KUNG HINDI KAYA, BASTA NAKA MODULAR FUNCTIONS.
// // puro .h files lang wala nang cpp
// // stepperOperations.h
// // lightsOperations.h
// // globalVars.h
// // ...
// // etc.
// #include "globalVars.h"

// int incomingByte = 0; // for incoming serial data

// void setup()
// {
//     initPinmode();      // from globalVars.h
//     Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
// }

// void loop()
// {
//     // send data only when you receive data:
//     if (Serial.available() > 0)
//     {
//         incomingByte = Serial.read();
//         // for strings, we need to process it.
//         // incoming bytes get replaced by the new bytes
//         // if there is more than one,
//         // The last one will be the incomingBytes.
//         Serial.write(incomingByte);

//         switch (incomingByte)
//         {
//         case '0':
//             // Standby Mode
//             showState(led1, "Standby Mode");
//             break;

//         case '1':
//             // Insert Mode'
//             showState(led2, "Insert Mode");
//             break;

//         case '2':
//             // Processing Mode
//             showState(led3, "Processing Mode");
//             break;

//         case '3':
//             // Retrieve Mode
//             showState(led4, "Retrieve Mode");
//             break;

//         default:
//             // Error case: Handle unexpected input
//             // Serial.println("");
//             // Serial.println(incomingByte);
//             break;
//         }
//     }
// }

// void offAllPin()
// {
//     digitalWrite(led1, LOW);
//     digitalWrite(led2, LOW);
//     digitalWrite(led3, LOW);
//     digitalWrite(led4, LOW);
// }

// void showState(int pin, String message)
// {
//     Serial.write(message.c_str());
//     Serial.println("");
//     offAllPin();
//     digitalWrite(pin, HIGH);
// }

void setup()
{
    Serial.begin(9600); // Set baud rate
}

void loop()
{
    if (Serial.available())
    {                                                       // Check if data is received
        String receivedData = Serial.readStringUntil('\n'); // Read data
        Serial.print("Received: ");
        Serial.println(receivedData); // Send response back to Python
    }

    Serial.println("Hello from Arduino!"); // Send data to Python
    delay(1000);                           // Send data every second
}
