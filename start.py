import serial

ser = serial.Serial('COM5', 4800, timeout=2)

while True :
    data_raw = ser.readline()
    print(data_raw)