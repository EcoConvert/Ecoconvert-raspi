# States of the machine before I forgot

## State

The RVM has on state that can either be one of four.
Initialize Everytime

- check if the motors is in the right position
- load the states variables
- check the serial communication line
- Show a screen saying initialzing

  0: standby mode

- Disable all button
- Enable VButton ONLY

1: insert mode bottle

- Enable Relay to the lights above
- Enable Camera bottle
-

2: insert mode SUP

- enable load cell sa ilalim
- enable lights sa ilalim
- enable camera sa ilalim
-

3: processing mode

- Enable Vbutton
- Enable Motor stepper
- Enable load cell
- Enable load cell
- Enable Shredder

4: retrieve mode

- disable all pins
- counter reset

## State Variables

The state variables contains the things inside the machine even if the power gets cut off, the machine can pick up from the states variables and do the state where it previously halt.

The Internal state of the sup bins, bottle, and made eco bricks. Structured like this  
{
"weight": 0.0,
"eco_brick_stored": 0,
"bottle_exist": false
}

the state.py holds how to change the values for each keys in the json object.
