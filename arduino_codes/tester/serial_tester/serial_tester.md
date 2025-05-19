The serial tester only has 

receiving ports when sent data are
n\ 10, 0x0A, .readString() default terminator
0, 48, 0x30, state_0
1, 49, 0x31, state_1
2, 50, 0x32, state_2
3, 51, 0x33, state_3
4, 52, 0x34, state_4
F, 70, 0x46, end_insert_pet
G, 71, 0x47, end_insert_SUP
R, 72, 0x82, rPi ack

Should be able to send
A, 65, 0x41, Ard ack
H, 72, 0x49, Ecobrick_done
char[8], "buffer",  SUP weight // I did 8 but 6 or 7 is probably enough  

(optional:
send ecobrick weight on display
)
