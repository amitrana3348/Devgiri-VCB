from struct import *
# Two integers to a floating point
i1 = 16967

i2 = 57898


f = unpack('<f',pack('<HH',i2,i1))[0]



print (f)

print(type(f))

# Floating point to two integers
i1, i2 = unpack('>HH',pack('f',3.14))
