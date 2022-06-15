import serial
from socket import timeout
# from serial import serial 

ser = serial.Serial('COM5', 4800, timeout=2)
ser.open()
ser.read()
print(ser.name)
while True :
    data = []
    data.append(ser.readlines())
    print(data)
print(data)
ser.close()