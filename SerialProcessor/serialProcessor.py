import serial
import time

def extractValue (buffer, start, termination_key):
    returnBuffer =[]
    i = start
    while buffer[i].hex != termination_key
        buffer.append(buffer[i])
        i +=1
    return returnBuffer

def decodeCEC_command (command_buffer):
    command = command_buffer[3]  + command_buffer[4]
    print("found command = ", command)

    match command:
        case "v1":
            value = extractValue(command_buffer, 10, 0xff)
            print("v1 tuning1, value=", value)

        case "v2":
            print("v2 tuning 2")
        case "v3":
            print("v3 tuning 3")
        case "v4":
            print("v4 tuning 4")
        case "v5":
            print("v5 tuning 5")
        case "ch":
            print("ch shift frequency for cw?")
        case "vh":
            print("vh add cw offset?")
        case "vo":
            print("vo related to display shift")
        case "vp":
            print("vp display option 1")
        case "vq":
            print("vq display option 2")
        case "sv":
            print("sv software version")
        case "sc":
            print("sc call sign")
        case "cm":
            print("cm display version and callsign?")
        case "c0":
            print("c0 text (yellow box) or graphics mode")
        case "vc":
            print("vc new frequency change")
        case "cc":
            print("cc change mode for frequency")
        case "va":
            print("va assign vfo a frequency")
        case "ca":
            print("ca assign mode for vfoa frequecy")
        case "vb":
            print("vb set vfob frequency")
        case "cb":
            print("cb set mode for vfoB")
        case "cn":
            print("cn which tuning step (1-5)")
        case "vt":
            print("vt tone for CW")
        case "ck":
            print("ck select key for cw")
        case "vs":
            print("vs word/minute for keyer")
        case "vy":
            print("vy delay returning after cw key")
        case "ve":
            print("ve delay for start")
        case _:
            print("unimplemented yet")

print("***starting serial procesor***")
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

            if ((len(buffer) == 0) and (in_byte.decode(errors='ignore') != 'p')):
                pass
            else:
                if (len(buffer) == 0):
                    print("line ", lineNum)
                buffer.append (in_byte)


                if in_byte.hex() == 'ff':
                    ffCount += 1
                    if ffCount == 3:

                        decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]
                        for item in decoded_buffer_char:
                            print(f"{item:<{4}}", end="")
                        print("")
                    
                        decoded_buffer_hex = [item.hex() for item in buffer]
                        for item in decoded_buffer_hex:
                            print(f"{item:<{4}}", end="")
                        print("")
                    
                        decoded_buffer_ord = [ord(item) for item in buffer]
                        for item in decoded_buffer_ord:
                            print(f"{item:<{4}}", end="")
                        print("")
                        print("\n")
                        ffCount = 0
                        lineNum += 1
                        buffer = buffer[:0]
                        #
                        # process and print it
                        #
                        decodeCEC_command (decoded_buffer_char)
 
        time.sleep(0.1)  # Small delay to prevent busy-waiting

except serial.SerialException as e:
    print(f"Serial port error: {e}")
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    if ser.is_open:
        ser.close()
        print("Serial port closed.")
