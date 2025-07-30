import serial
import time

def extractValue (buffer, start, end):
    returnBuffer =""
    i = start
    while i < end:
        returnBuffer = returnBuffer + buffer[i]
        i +=1
    return returnBuffer.replace('"','')

def decodeCEC_command (command_buffer):
    command = command_buffer[3]  + command_buffer[4]
    print("found command = ", command)

    match command:
        case "v1":
            print("v1 tuning 1")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")

        case "v2":
            print("v2 tuning 2")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "v3":
            print("v3 tuning 3")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "v4":
            print("v4 tuning 4")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "v5":
            print("v5 tuning 5")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "ch":
            print("ch shift frequency for cw?")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vh":
            print("vh add cw offset?")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vo":
            print("vo related to display shift")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vp":
            print("vp display option 1")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vq":
            print("vq display option 2")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "sv":
            print("sv software version")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "sc":
            print("sc call sign")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "cm":
            print("cm display version and callsign?")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "c0":
            print("c0 text (yellow box) or graphics mode")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vc":
            print("vc new frequency change")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "cc":
            print("cc change mode for frequency")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "va":
            print("va assign vfo a frequency")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "ca":
            print("ca assign mode for vfoa frequecy")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vb":
            print("vb set vfob frequency")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "cb":
            print("cb set mode for vfoB")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "cn":
            print("cn which tuning step (1-5)")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vt":
            print("vt tone for CW")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "ck":
            print("ck select key for cw")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vs":
            print("vs word/minute for keyer")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "vy":
            print("vy delay returning after cw key")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
        case "ve":
            print("ve delay for start")
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            print("value=", value,sep='*',end='*')
            print("\n")
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
