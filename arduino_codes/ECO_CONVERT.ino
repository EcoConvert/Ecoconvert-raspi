.
#define PlasticShredder (9) //
    // Variables
    int timbang = 0;
int movearmlong = 2650;

int isHome = 0;
int bottleNo = 3;
float weight = 0;
float weight1 = 0;
String cmd = "";
int process = 0;

#define lms_for 11
#define lms_rev 12

//=====RELAYS=====
#define RELAY_WIPER 22          // Dispenser Motor pin.
const uint8_t RELAY_ON = LOW;   // Use LOW signal to turn relay on.
const uint8_t RELAY_OFF = HIGH; // Use HIGH signal to turn relay off.

//=====HX711 LOAD CELL=====
// TAAS
#include "HX711.h"
HX711 scale; // TAAS
// float calibration_factor = -759671; // Adjust this number to match your setup
float calibration_factor = -751973; // New calibration_factor

HX711 scale1;                        // BABA
float calibration_factor1 = -759671; // Adjust this number to match your setup

// BABA

//=====SERVO=====

#include <Servo.h>
Servo servo1;
//=====STEPPER=====
// Pin Definitions
const int PUL = 6; // Pulse pin
const int DIR = 7; // Direction pin
const int ENA = 8; // Enable pin (optional)

#define LS_Wiper_Home (30)
#define LS_Stepper_Home (28)

// ================================ SUP LIGHT =====================================

#define lightPin 10

void setup()
{

    // Initialization =======================================================================
    Serial.begin(9600);
    // Light declarations
    pinMode(lightPin, OUTPUT);

    pinMode(LS_Wiper_Home, INPUT_PULLUP);
    pinMode(LS_Stepper_Home, INPUT_PULLUP);
    Serial.println("\n==================");
    pinMode(PUL, OUTPUT);
    pinMode(DIR, OUTPUT);
    pinMode(ENA, OUTPUT);
    digitalWrite(ENA, LOW); // Enable driver (LOW = active on some drivers)

    pinMode(PlasticShredder, OUTPUT);
    digitalWrite(PlasticShredder, RELAY_OFF); // Might delete this

    // Load Cell 1
    scale.begin(2, 3);
    //   scale.set_scale();    // No calibration factor yet
    //   scale.tare();         // Reset the scale to 0

    //   long reading = scale.get_units(10);
    //   Serial.print("Reading (no calibration): ");
    //   Serial.println(reading);
    //   scale.set_scale(calibration_factor);
    // Serial.print(scale.get_units(10), 1);

    // Load Cell 2
    scale1.begin(4, 5);
    scale1.set_scale(); // No calibration factor yet
    scale1.tare();      // Reset the scale to 0

    long reading1 = scale1.get_units(10);
    Serial.print("Reading1 (no calibration): ");
    Serial.println(reading1);
    scale1.set_scale(calibration_factor1);
    Serial.print(scale1.get_units(10), 1);

    // Relays and Sensors Initialize
    pinMode(RELAY_WIPER, OUTPUT);
    digitalWrite(RELAY_WIPER, RELAY_OFF);
    servo1.attach(26);
    // servo1.write(0); // This is the one that opens the gripper in the beginning

    // Reset State of the machine ===============================================================
    resetNow();

    Serial.println("Ready\n==========");
    // For test only
    delay(1000);
    Serial.println("PROCESS START");
    holdbottle("ON");
}

//  For tests
// unsigned long prev = 0 ;
// unsigned long interval = 60000 ;

bool testing = false;

void loop()
{
    // For testing only ======================================================
    // unsigned long curr = millis();
    // if(curr - prev <= interval){
    //   // resetNow();
    //   // holdbottle("OFF");
    //   // delay(5000);
    //   // holdbottle("ON");
    //   wiper(20);  //Change 20 SEC
    //   // holdbottle("OFF");
    //   // moveStepperHome();
    //   // getWeight();
    // } else {
    //   moveWiperHome();
    //   holdbottle("OFF");
    // }

    //  getWeight();
    // serialCommand();
    // // Serial.print(digitalRead(LS_Wiper_Home));
    // // Serial.print(digitalRead(LS_Stepper_Home));

    // This if block will produce ecobrick
    // if(process==1){
    //   Serial.println("PROCESS START");
    //   resetNow();
    //   holdbottle("OFF");
    //   delay(5000);
    //   holdbottle("ON");
    //   wiper(2);  //Change 20 SEC
    //   holdbottle("OFF");
    //   moveStepperHome();
    //   getWeight();

    //     if(weight>=0.4){ // 500grams weight trigger
    //         Serial.print("BOTTLE OK MOVING");
    //         bottleNo+=1;

    //         moveStepperHome();
    //         holdbottle("OFF");
    //         delay(3000);
    //         holdbottle("ON");
    // moveBottle();

    //        if( bottleNo >= 4){
    //         process=0;
    //         bottleNo=0;
    //         Serial.print("FINISH");
    //       }
    //     }
    // }
    // Serial.println("PROCESS START");
    // resetNow();
    // holdbottle("OFF");
    // delay(5000);
    // holdbottle("ON");
    // wiper(20);  //Change 20 SEC
    // holdbottle("OFF");
    // // moveStepperHome();
    // getWeight();

    // if(weight>=0.4){ // 500grams weight trigger
    //       moveStepperHome();
    //       Serial.print("BOTTLE OK MOVING");
    //       bottleNo+=1;

    //       moveStepperHome();
    //       holdbottle("OFF");
    //       delay(3000);
    //       holdbottle("ON");
    //       moveBottle();

    //      if( bottleNo >= 4){
    //       process=0;
    //       bottleNo=0;
    //       Serial.print("FINISH");
    //     }
    //   }

    // moveStepperHome(); // For test only
    // moveBottle();

    wiper(20); // Change 20 SEC
    // moveWiperHome();

    // After receiving the serial command
    // moveBottle();
    delay(1000); // Change
    Serial.println(" ============= FINISH LOOP ================ ");
}

void moveBottle()
{
    Serial.print("Bottle No: ");
    Serial.println(bottleNo);
    // moveWiperHome();
    delay(2000);
    // if(bottleNo > 2){ // Para kumonte yung code -> conciseness
    if (bottleNo == 4)
    {
        movearmlong = 2650 + 550;
    }
    else if (bottleNo == 3)
    {
        movearmlong = 2650 + 550;
    }
    else if (bottleNo == 2)
    {
        movearmlong = 2650;
    }
    else if (bottleNo == 1)
    {
        movearmlong = 2650;
    }
    else
    {
        movearmlong = 2650;
    }
    // Moving   LEFT 1 , 2 - > HOME
    digitalWrite(DIR, LOW);
    moveSteps(long(movearmlong));
    holdbottle("OFF");
    holdbottle("ON");
    // moveWiperHome();
    moveStepperHome();
}
