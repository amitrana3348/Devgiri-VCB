#!/usr/bin/env python
import minimalmodbus
import time
import serial
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
minimalmodbus.BAUDRATE = 9600

meter = minimalmodbus.Instrument('COM4', 3)
meter.mode = minimalmodbus.MODE_RTU

#print (minimalmodbus._getDiagnosticString())
print ('entering main code')
#time.sleep(2)


meter.address
while True:
     ## Read temperature (PV = ProcessValue) ##
     try:
          #keep this register value always one less than actual
          # SO FOR READING register 71, put 70 here
          ## by default, its reading swap float
          bc = meter.read_float(70,4,2)

          
          print (bc)
          #reg_a = meter.read_registers(70,2,4)
          #print (reg_a)
          #print(bc)
     except IOError:
          print("Failed to read from instrument")
     except ValueError:
          print("value error")
     time.sleep(1)


