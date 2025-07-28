#!/usr/bin/env python3
import serial

print(" starting serial test\n")

if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)

    data_to_send = bytes([0x59, 0x58, 0x68, 0x06, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x73])
    ser.write(data_to_send)
    print("Sent: ")
    print( data_to_send.hex())
    print("\n")
    ser.close()