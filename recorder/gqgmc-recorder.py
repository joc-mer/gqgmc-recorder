import serial
import struct
import time

def connect():
    s = serial.Serial( "/dev/ttyUSB0", 115200 )
    return s

def get_version(serial):
    serial.write(("<GETVER>>").encode())
    version = serial.read(14)
    return version.decode()

def get_cpm(serial):
    serial.write(("<GETCPM>>").encode())
    cpm_bytes = serial.read(2)
    (hb, lb) = struct.unpack(">BB", cpm_bytes)

    cpm = hb * 256 + lb

    return cpm
            
def main():
    serial = connect()
    version = get_version(serial)
    print('Connected to ' + version)

    for i in range(100):
        print(get_cpm(serial))
        time.sleep(1)

    serial.close()
    exit()

main()
