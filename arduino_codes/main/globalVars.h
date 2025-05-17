#ifndef GLOBALVARS_H
#define GLOBALVARS_H

extern int led1 = 3;
extern int led2 = 4;
extern int led3 = 5;
extern int led4 = 6;
extern int btn = 2;

void initPinmode() {
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT); 
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(btn, INPUT);  
}

#endif 