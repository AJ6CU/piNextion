import serial
import time

print(" starting serial test\n")
ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)

try:
    while True:
        # Read a line from the serial port (until a newline character is received)
        # Decode the bytes to a string (e.g., 'utf-8') and remove leading/trailing whitespace
        data = ser.readline().decode('utf-8').strip()

        if data:  # Check if data was received
            print(f"Received: {data.hex()}")

        time.sleep(0.1)  # Small delay to prevent busy-waiting

except serial.SerialException as e:
    print(f"Serial port error: {e}")
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")
