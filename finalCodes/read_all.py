#!/usr/bin/env python
from struct import *
import minimalmodbus
import time
import serial
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = False
minimalmodbus.BAUDRATE = 9600

meter = minimalmodbus.Instrument('COM4', 1)
meter.mode = minimalmodbus.MODE_RTU

#print (minimalmodbus._getDiagnosticString())
print ('entering main code')
#time.sleep(2)

flag = 0

def read_registers(address):
     regs = meter.read_registers(address,2,3)
     i1 = regs[0]
     i2 = regs[1]
     val = unpack('<f',pack('<HH',i1,i2))[0]
     val = round(val,4)
     return val

def read_all_para(address):
     regs = meter.read_registers(address,8,3)
     i1 = regs[0]
     i2 = regs[1]
     kwh = unpack('<f',pack('<HH',i1,i2))[0]
     kwh = round(kwh,3)
     print ("kwh = ",kwh)

     i1 = regs[2]
     i2 = regs[3]
     kvah = unpack('<f',pack('<HH',i1,i2))[0]
     kvah = round(kvah,3)
     print ("kVAh = ",kvah)

     i1 = regs[4]
     i2 = regs[5]
     kvarhlag = unpack('<f',pack('<HH',i1,i2))[0]
     kvarhlag = round(kvarhlag,3)
     print ("kVARhlag = ",kvarhlag)
     
     i1 = regs[6]
     i2 = regs[7]
     kvarhlead = unpack('<f',pack('<HH',i1,i2))[0]
     kvarhlead = round(kvarhlead,3)
     print ("kVARhlead = ",kvarhlead)
     print("************************************\n")
while True:
     ## Read temperature (PV = ProcessValue) ##
     for x in range(0,4):
          try:
               print('reading pf')
               pf = read_registers(139)
               print("AVG PF = ",pf)
          except IOError:
               print("Failed to read from instrument")
          except ValueError:
               print("value error")
          time.sleep(2)

     for x in range(0,4):
          try:
               read_all_para(223)
          except IOError:
               print("Failed to read from instrument")
          except ValueError:
               print("value error")
          time.sleep(2)

     minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
     
     

               
