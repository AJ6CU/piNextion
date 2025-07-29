import serial
import time

print(" starting serial test\n")
ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)

try:
    ffCount = 0
    buffer = []
    lineNum = 1
    
    while True:
        # Read a line from the serial port (until a newline character is received)
        # Decode the bytes to a string (e.g., 'utf-8') and remove leading/trailing whitespace
 
        in_byte= ser.read(1)
        
        if in_byte:
            if (len(buffer) == 0):
                print("line ", lineNum)
            
            buffer.append (in_byte)

            if in_byte.hex() == 'ff':
                ffCount += 1
                if ffCount == 3:

                    decoded_buffer = [item.decode(errors='replace') for item in buffer]
                    for item in decoded_buffer:
                        print(f"{item:<{4}}", end="")
                    print("")
                    
                    decoded_buffer = [item.hex() for item in buffer]
                    for item in decoded_buffer:
                        print(f"{item:<{4}}", end="")
                    print("")
                    
                    decoded_buffer = [ord(item) for item in buffer]
                    for item in decoded_buffer:
                        print(f"{item:<{4}}", end="")
                    print("")
                    print("\n")
                    ffCount = 0
                    lineNum += 1
                    buffer = buffer[:0]
 
        time.sleep(0.1)  # Small delay to prevent busy-waiting

except serial.SerialException as e:
    print(f"Serial port error: {e}")
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")
