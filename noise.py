#import smbus
import time
from datetime import datetime
import RPi.GPIO as GPIO
import requests
import json
import serial
import os
import struct

cr=0x0D
lf=0x0A
fo = open("foo.txt", "wb")

ser1 = serial.Serial("/dev/ttyUSB0", timeout=2)
print ser1
ser1.flushInput()

ser1.write("Frequency Weighting?")
ser1.write('\r\n')

while ser1.inWaiting() > 0:
      out += ser1.read(1)
      print out

ser1.write("Echo,Off")
ser1.write('\r\n')

tnow = time.strftime("%Y/%m/%d %H:%M:%S")
print tnow

ser1.write("Clock,")
ser1.write(tnow)
ser1.write('\r\n')

# Setting parameters to ON
ser1.write("Display Sub Channel,On")
ser1.write('\r\n')
time.sleep(1)

ser1.write("Display Ly,On")
ser1.write('\r\n')
time.sleep(1)

ser1.write("Display Leq,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LE,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display Lmax,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display Lmin,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LN1,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LN2,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LN3,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LN4,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("Display LN5,On")
ser1.write('\r\n')
time.sleep(1)
ser1.write("AC OUT, Main")
ser1.write('\r\n')

ser1.write("Display Ly, On")
ser1.write('\r\n')

ser1.write("Measure,Start")
ser1.write('\r\n')


while 1:
#  ser1.flushInput()
  out = ''
  try:
        print time.strftime("%Y/%m/%d %H:%M:%S")
        ser1.write("DOD?")
        ser1.write('\r\n')

        while ser1.inWaiting() > 0:
            out += ser1.read(1)
        print out

        time.sleep(3)

  except KeyboardInterrupt:
        ser1.write("Measure,Stop")
        ser1.write('\r\n')



