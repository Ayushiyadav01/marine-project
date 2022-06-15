import serial

ser = serial.Serial('COM5', 4800, timeout=2)

while True :
    data_raw = str(ser.readline())
    # print(type(data_raw))
    # print(data_raw)
    data_li = list(data_raw.split(","))
    # print(data_li)
    if (data_li[0]=='b\'$GPGGA'):
        print(data_li)