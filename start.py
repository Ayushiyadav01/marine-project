<<<<<<< HEAD
# import serial
=======
from time import process_time_ns
import serial
>>>>>>> fd6b92bfc725b8af728c7307ed020674e020f9e5

# ser = serial.Serial('COM5', 4800, timeout=2)

<<<<<<< HEAD
# while True :
#     data_raw = str(ser.readline())
#     # print(type(data_raw))
#     # print(data_raw)
#     data_li = list(data_raw.split(","))
#     # print(data_li)
#     if (data_li[0]=='b\'$GPGGA'):
#         print(data_li)
        
print("hello")
=======
while True :
    data_raw = str(ser.readline())
    # print(type(data_raw))
    # print(data_raw)
    data_li = list(data_raw.split(","))
    # print(data_li)
    if (data_li[0]=='b\'$GPGGA'):
        # print(data_li)

        UTC = data_li[1]
        print("UTC = ", UTC)
        lat = data_li[2]
        print("Latitude = ", lat, data_li[3])
        long = data_li[4]
        print("Longitude = ", long, data_li[5])

>>>>>>> fd6b92bfc725b8af728c7307ed020674e020f9e5