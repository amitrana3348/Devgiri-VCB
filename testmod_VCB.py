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



def read_registers(address):
     regs = meter.read_registers(address,2,3)
     i1 = regs[0]
     i2 = regs[1]
     val = unpack('<f',pack('<HH',i1,i2))[0]
     val = round(val,3)
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
     kVAh = unpack('<f',pack('<HH',i1,i2))[0]
     kVAh = round(kVAh,3)
     print ("kVAh = ",kVAh)

     i1 = regs[4]
     i2 = regs[5]
     kwhlag = unpack('<f',pack('<HH',i1,i2))[0]
     kwhlag = round(kwhlag,3)
     print ("kwhlag = ",kwhlag)
     
     i1 = regs[6]
     i2 = regs[7]
     kwhlead = unpack('<f',pack('<HH',i1,i2))[0]
     kwhlead = round(kwhlead,3)
     print ("kwhlead = ",kwhlead)
     print("************************************\n")
while True:
     ## Read temperature (PV = ProcessValue) ##
     try:
          #kwh = read_registers(550) 
          #print('kWH = {}'.format(kwh))
          
          #kVAh = read_registers(552)
          #print('kVAh = {}'.format(kVAh))

          #kWHlag = read_registers(554)
          #print("kWHlag = {}".format(kWHlag))
          
          #kWHlead = read_registers(556)
          #print("kWHlead = {}".format(kWHlead))
          #reg_a = meter.read_registers(70,2,4)
          #print (reg_a)
          #print(bc)
          read_all_para(550)
     except IOError:
          print("Failed to read from instrument")
     except ValueError:
          print("value error")
     time.sleep(2)


