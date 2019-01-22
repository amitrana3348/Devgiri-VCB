from struct import *
# Two integers to a floating point
i1 = 10224

i2 = 16968


f = unpack('<f',pack('<HH',i1,i2))[0]



print (f)

print(type(f))

# Floating point to two integers
i1, i2 = unpack('>HH',pack('f',3.14))
