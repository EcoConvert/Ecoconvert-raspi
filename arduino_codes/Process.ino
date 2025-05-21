

void getWeight()
{
    scale.set_scale(calibration_factor);
    Serial.print("Weight (grams): ");
    weight = scale.get_units(), 1;
    weight = weight - 2.02;
    if (weight < 0)
    {
        weight = 0;
    }
    Serial.println(weight); // One decimal place

    // scale1.set_scale(calibration_factor1);
    // Serial.print("Weight1 (grams): ");
    // weight1 = scale1.get_units(), 1;
    // weight1= weight1;
    // if(weight1<0){
    //   weight1=0;
    // }
    // Serial.println(weight1);  // One decimal place

    scale1.set_scale(calibration_factor1);
    Serial.print("Weight1 (grams): ");
    //   weight1 = scale1.get_units(), 1;
    weight1 = scale1.get_units(10);
    //   weight1= weight1-3.48;
    // //  if(weight1<0){
    // //    weight1=0;
    // //  }
    Serial.println(weight1, 3); // One decimal place
}

void getPETWeight()
{
    scale.set_scale(calibration_factor);
    Serial.print("Weight (grams): ");
    weight = scale.get_units(10), 3;
    Serial.println(weight); // One decimal place
}

void getSUPWeight()
{
    scale1.set_scale(calibration_factor);
    Serial.print("Weight (grams): ");
    weight = scale1.get_units(10), 3;
    Serial.println(weight); // One decimal place
}

void wiper(int x)
{
    for (int i = 0; i < x; i++)
    {
        digitalWrite(RELAY_WIPER, RELAY_ON);
        delay(2000);
    }
    digitalWrite(RELAY_WIPER, RELAY_OFF);
}

void shrender(int x)
{
    for (int i = 0; i < x; i++)
    {
        digitalWrite(PlasticShredder, RELAY_ON);
        delay(2000);
    }
    digitalWrite(PlasticShredder, RELAY_OFF);
}

void holdbottle(String x)
{
    // Will release the bottle
    if (x == "OFF")
    {
        Serial.println("hold off");
        servo1.write(0);
        delay(1000);
    }
    // Will hold the bottle
    if (x == "ON")
    {
        Serial.println("hold on");
        // servo1.write(120);
        servo1.write(180);
        delay(1000);
    }
}

void supLight(String x)
{
    if (x == "ON")
    {
        digitalWrite(lightPin, HIGH);
        delay(100);
    }
    else
    {
        digitalWrite(lightPin, LOW);
        delay(100);
    }
}

void moveSteps(long steps)
{
    for (long i = 0; i < steps; i++)
    {
        digitalWrite(PUL, HIGH);
        delayMicroseconds(400); // Step pulse width
        digitalWrite(PUL, LOW);
        delayMicroseconds(400);
    }
}

void resetNow()
{
    Serial.println("reset");
    holdbottle("OFF");
    moveWiperHome();
    moveStepperHome();
    Serial.println("reset done");
}

void moveWiperHome()
{
    while (digitalRead(LS_Wiper_Home) == 1)
    {
        digitalWrite(RELAY_WIPER, RELAY_ON);
        Serial.println("Going Home....");
    }
    digitalWrite(RELAY_WIPER, RELAY_OFF);
}

void moveStepperHome()
{
    // HIGH means the LS is not trigger note: LS is normally closed
    while (digitalRead(LS_Stepper_Home) == HIGH)
    {
        digitalWrite(DIR, HIGH);
        moveSteps(long(50));
    }
}
