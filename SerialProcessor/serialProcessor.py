import serial
import time

debugCommandDecoding = False

def extractValue (buffer, start, end):
    returnBuffer =""
    i = start
    while i < end:
        returnBuffer = returnBuffer + buffer[i]
        i +=1
    return returnBuffer.replace('"','')

def decodeCEC_command (command_buffer):
    #
    # Command format is "pm.xx.val=nn..n" terminated by 3 0xff
    # Command starts in position 3(0,1,2,3)
    # Value starts in position 10, and ends before the 3 0xff
    #


    command = command_buffer[3]  + command_buffer[4]
    if debugCommandDecoding:
        print("found command = ", command)

    match command:
        case "v1":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("v1 tuning 1")
                print("value=", value,sep='*',end='*')
                print("\n")

        case "v2":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("v2 tuning 2")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "v3":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("v3 tuning 3")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "v4":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("v4 tuning 4")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "v5":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("v5 tuning 5")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "ch":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("ch shift frequency for cw?")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vh":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vh add cw offset?")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vo":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vo related to display shift")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vp":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vp display option 1")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vq":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vq display option 2")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "sv":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("sv software version")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "sc":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("sc call sign")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "cm":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("cm display version and callsign?")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "c0":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("c0 text (yellow box) or graphics mode")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vc":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vc new frequency change")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "cc":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("cc change mode for frequency")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "va":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("va assign vfo a frequency")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "ca":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("ca assign mode for vfoa frequecy")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vb":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vb set vfob frequency")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "cb":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("cb set mode for vfoB")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "cn":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("cn which tuning step (1-5)")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vt":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vt tone for CW")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "ck":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("ck select key for cw")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vs":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vs word/minute for keyer")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "vy":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("vy delay returning after cw key")
                print("value=", value,sep='*',end='*')
                print("\n")
        case "ve":
            value = extractValue(command_buffer, 10, len(command_buffer)-3)
            if debugCommandDecoding:
                print("ve delay for start")
                print("value=", value,sep='*',end='*')
                print("\n")
        case _:
            print("unimplemented yet command=", command)


if debugCommandDecoding:
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
                if debugCommandDecoding:
                    if (len(buffer) == 0):
                        print("line ", lineNum)
                buffer.append (in_byte)


                if in_byte.hex() == 'ff':
                    ffCount += 1
                    if ffCount == 3:

                        decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]
                        if debugCommandDecoding:
                            for item in decoded_buffer_char:
                                print(f"{item:<{4}}", end="")
                            print("")
                    
                        decoded_buffer_hex = [item.hex() for item in buffer]
                        if debugCommandDecoding:
                            for item in decoded_buffer_hex:
                                print(f"{item:<{4}}", end="")
                            print("")
                    
                        decoded_buffer_ord = [ord(item) for item in buffer]
                        if debugCommandDecoding:
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
