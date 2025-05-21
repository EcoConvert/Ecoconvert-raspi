/*
  Responds to commands sent via Serial.
*/

// The serial tester only has

// receiving ports when sent data are
// n\ 10, 0x0A, .readString() default terminator
// 0, 48, 0x30, state_0
// 1, 49, 0x31, state_1
// 2, 50, 0x32, state_2
// 3, 51, 0x33, state_3
// 4, 52, 0x34, state_4
// F, 70, 0x46, end_insert_pet
// G, 71, 0x47, end_insert_SUP

// Should be able to send
// H, 72, 0x49, Ecobrick_done
// char[8], "buffer",  SUP weight // I did 8 but 6 or 7 is probably enough

// The RVM has on state that can either be one of four.
// Initialize Everytime

// - check if the motors is in the right position
// - load the states variables
// - check the serial communication line
// - Show a screen saying initialzing

//   0: standby mode

// - Disable all button
// - Enable VButton ONLY

// 1: insert mode bottle

// - Enable Relay to the lights above
// - Enable Camera bottle
// -

// 2: insert mode SUP

// - enable load cell sa ilalim
// - enable lights sa ilalim
// - enable camera sa ilalim
// -

// 3: processing mode

// - Enable Vbutton
// - Enable Motor stepper
// - Enable load cell
// - Enable load cell
// - Enable Shredder

// 4: retrieve mode

// - disable all pins
// - counter reset

void serialCommand()
{
    while (Serial.available() > 0)
    {
        String inString = Serial.readString();
        inString.trim();

        if (inString == "0") // 0 means return to standby screen
            // SerialCommand(inString, led, int(1), int(500));
            resetNow();
        else if (inString == "1") // 1 is PET insert mode
            // SerialCommand(inString, led, int(inString.toInt()), int(1000));
            scale.tare(); // To reset the weight
        else if (inString == "2")
        { // 2 is insert mode SUP
            supLight("ON");
            // SerialCommand(inString, led, int(inString.toInt()), int(500));
        }
        else if (inString == "3")
        { // 3 is processing mode
            SerialCommand(inString, led, int(inString.toInt()), int(250));
            state3(int(500));
        }
        else if (inString == "4") // 4 is retrieve mode
            SerialCommand(inString, led, int(inString.toInt()), int(500));
        else if (inString == "R")
            SerialCommand(inString, led, int(2), int(200));
        else if (inString == "F")
            SerialCommand(inString, led, int(4), int(200));
        else if (inString == "G")
        {
            // SUPEndProcess();
            scale1.tare();
        }
    }
    // String cmd = "";
    // if (Serial.available() > 0) {
    //   cmd = Serial.readStringUntil('\n');
    // Serial.println(cmd);
    // }
    // if (cmd.length() <= 0) {
    //   // do nothing for zero length
    // }
    //  else if (cmd == "1") {
    //   process=1;
    // } else if (cmd == "r") {
    //  resetNow();
    // }else if (cmd=="servo"){
    //     holdbottle("OFF");
    //     delay(3000);
    //       holdbottle("ON");

    // }else if (cmd=="wipertest"){
    //   moveStepperHome();
    //   bottleNo=1;
    //   holdbottle("OFF");
    //   delay(3000);
    //   holdbottle("ON");
    //   moveBottle();

    //   moveStepperHome();
    //   bottleNo=2;
    //   holdbottle("OFF");
    //   delay(3000);
    //   holdbottle("ON");
    //   moveBottle();
    //   moveStepperHome();

    //   bottleNo=3;
    //   holdbottle("OFF");
    //   delay(3000);
    //   holdbottle("ON");
    //   moveBottle();
    //   moveStepperHome();

    //   bottleNo=4;
    //   holdbottle("OFF");
    //   delay(3000);
    //   holdbottle("ON");
    //   moveBottle();
    //   moveStepperHome();

    // }else if (cmd=="relay"){
    // digitalWrite(RELAY_WIPER,RELAY_ON);
    // delay(1000);
    // digitalWrite(RELAY_WIPER,RELAY_OFF);
    // delay(1000);
    //       }
}
