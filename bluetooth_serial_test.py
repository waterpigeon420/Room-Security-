#! /usr/bin/python3
import serial
import os
import time

if os.path.exists('/dev/rfcomm0')==False:
    path='sudo rfcomm bind 0 98:D3:61:F6:41:E4'
    os.system(path)
    time.sleep(1)
bluetoothSerial=serial.Serial("/dev/rfcomm0",baudrate=9600)
count=None
while count!="terminate":

    count=input("Enter the command: ")
    j=str(count)
    b=j.encode()
    bluetoothSerial.write(b)
    time.sleep(1)

    
    
RXData=(bluetoothSerial.readline()).strip().decode("utf-8")

print(RXData)
