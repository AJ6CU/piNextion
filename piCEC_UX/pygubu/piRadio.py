import serial
import time
class piRadio():
    def __init__(self, serialPort, debugFlag):
        self.debugCommandDecoding = debugFlag
        self.tty = serialPort
        self.getterCB_Dict = {
            "v1": self.v1Get,
            "v2": self.v2Get,
            "v3": self.v3Get,
            "v4": self.v4Get,
            "v5": self.v5Get,
            "ch": self.chGet,
            "vh": self.vhGet,
            "vo": self.voGet,
            "vp": self.vpGet,
            "vq": self.vqGet,
            "sv": self.svGet,
            "sc": self.scGet,
            "cm": self.cmGet,
            "c0": self.c0Get,
            "vc": self.vcGet,
            "cc": self.ccGet,
            "va": self.vaGet,
            "ca": self.caGet,
            "vb": self.vbGet,
            "cb": self.cbGet,
            "cn": self.cnGet,

        }
        self.putterCB_Dict = {
            "v1": self.v1Put
            "v2": self.v2Put,
            "v3": self.v3Put,
            "v4": self.v4Put,
            "v5": self.v5Put,
            "ch": self.chPut,
            "vh": self.vhPut,
            "vo": self.voPut,
            "vp": self.vpPut,
            "vq": self.vqPut,
            "sv": self.svPut,
            "sc": self.scPut,
            "cm": self.cmPut,
            "c0": self.c0Put,
            "c0": self.c0Put,
            "vc": self.vcPut,
            "cc": self.ccPut,
            "va": self.vaPut,
            "ca": self.caPut,
            "vb": self.vbPut,
            "cb": self.cbPut,
            "cn": self.cnPut,
        }


    def openRadio(self):
        self.radioPort = None
        if self.debugCommandDecoding:
            print("***opening port to radio***")
        try:
            self.radioPort = serial.Serial(self.tty, 9600, timeout=1)
        except serial.SerialException as e:
            print(f"Serial port error: {e}")
        return self.radioPort

    def extractValue(self, buffer, start, end):
        returnBuffer =""
        i = start
        while i < end:
            returnBuffer = returnBuffer + buffer[i]
            i +=1
        return returnBuffer.replace('"','')

#
#   Decoding command buffers sent from MCU to Nextion screens
#
#   Command format is "pm.xx.val=nn..n" terminated by 3 0xff
#   Command starts in position 3(0,1,2,3)
#   Value starts in position 10, and ends before the 3 0xff
#   All"values" are ascii characters  (i.e., frequency might be
#   pm.xx.val=7500000ffffff  for 7.5mhz and a 14m frequency might be
#   pm.xx.val=14032000ffffff
#

    #
    #   decode and update UX
    #   the command is used to access a dict with pointer to the "getter"
    #
    def getRadioCommand(self, buffer):
        command = buffer[3]  + buffer[4]
        if self.debugCommandDecoding:
            print("found command = ", command)
        self.getterCB_Dict[command](buffer)
#
#   The "v1" command is used for smallest tuning rate
#
    def v1Get (self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if self.debugCommandDecoding:
            print("v1 get called:", "buffer =", buffer)
            print("v1 tuning 1")
            print("value=", value,sep='*',end='*')
            print("\n")

    def v1Put(self):
        if self.debugCommandDecoding:
            print("v1 put called")

#
#   The "v2" command 1s used for the second smallest tuning rate
#
    def v2Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v2 get called:", "buffer =", buffer)
            print("v2 tuning 2")
            print("value=", value,sep='*',end='*')
            print("\n")

    def v2Put(self):
        if self.debugCommandDecoding:
            print("v2 put called")

#
#   The "v3" command 1s used for the third (middle) tuning rate
#
    def v3Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v3 get called:", "buffer =", buffer)
            print("v3 tuning 3")
            print("value=", value, sep='*', end='*')
            print("\n")

    def v3Put(self):
        if self.debugCommandDecoding:
            print("v3 put called")

#
#   The "v4" command 1s used for the next largest tuning rate
#
    def v4Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v4 get called:", "buffer =", buffer)
            print("v4 tuning 4")
            print("value=", value, sep='*', end='*')
            print("\n")

    def v4Put(self):
        if self.debugCommandDecoding:
            print("v4 put called")

#
#   The "v5" command 1s used for the largest tuning rate
#
    def v5Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v5 get called:", "buffer =", buffer)
            print("v5 tuning 5")
            print("value=", value, sep='*', end='*')
            print("\n")

    def v5Put(self):
        if self.debugCommandDecoding:
            print("v5 put called")

#
#   The "ch" command originates from the EEPROM and is added to the frequency to shift it
#
    def chGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ch get called:", "buffer =", buffer)
            print("ch shift frequency for cw?")
            print("value=", value, sep='*', end='*')
            print("\n")

    def chPut(self):
        if self.debugCommandDecoding:
            print("ch put called")

#
#   The "vh" command originates from the EEPROM and is added to the frequency to shift it
#
    def vhGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vh get called:", "buffer =", buffer)
            print("vh add cw offset?")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vhPut(self):
        if self.debugCommandDecoding:
            print("vh put called")

#
#   The "vo" command originates from the EEPROM and is added to the frequency to shift it
#
        def voGet(self, buffer):
            value = self.extractValue(buffer, 10, len(buffer) - 3)
            if self.debugCommandDecoding:
                print("vo get called:", "buffer =", buffer)
                print("vo related to display shift")
                print("value=", value, sep='*', end='*')
                print("\n")

        def voPut(self):
            if self.debugCommandDecoding:
                print("vo put called")

#
#   The "vp" command originates from the EEPROM and is added to the frequency to shift it
#
        def vpGet(self, buffer):
            value = self.extractValue(buffer, 10, len(buffer) - 3)
            if self.debugCommandDecoding:
                print("vp get called:", "buffer =", buffer)
                print("vp related to display shift")
                print("value=", value, sep='*', end='*')
                print("\n")

        def vpPut(self):
            if self.debugCommandDecoding:
                print("vp put called")

#
#   The "vq" command is referred to as display option 2 in EEPROM
#
    def vqGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vq get called:", "buffer =", buffer)
            print("vq related to display shift")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vqPut(self):
        if self.debugCommandDecoding:
            print("vq put called")

#
#   The "sv" command is stores the text of the firmware version
#
    def svGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("sv get called:", "buffer =", buffer)
            print("sv software version")
            print("value=", value, sep='*', end='*')
            print("\n")

    def svPut(self):
        if self.debugCommandDecoding:
            print("sv put called")

#
#   The "sc" command is stores the text of the operators callsign
#
    def scGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("sc get called:", "buffer =", buffer)
            print("sc call sign"")
            print("value=", value, sep='*', end='*')
            print("\n")

    def scPut(self):
        if self.debugCommandDecoding:
            print("sc put called")

#
#   The "cm" command determines whether call sign and firmware versions are displayed
#
    def cmGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("cm get called:", "buffer =", buffer)
            print("cm display version and callsign?")
            print("value=", value, sep='*', end='*')
            print("\n")

    def cmPut(self):
        if self.debugCommandDecoding:
            print("cm put called")

#
#   The "c0" command determines whether we are in text (yellow box) or graphics mode
#
    def c0Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("c0 get called:", "buffer =", buffer)
            print("c0 text (yellow box) or graphics mode")
            print("value=", value, sep='*', end='*')
            print("\n")

    def c0Put(self):
        if self.debugCommandDecoding:
            print("c0 put called")

#
#   The "vc" command indicates a new frequency
#
    def vcGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vc get called:", "buffer =", buffer)
            print("vc new frequency change")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vcPut(self):
        if self.debugCommandDecoding:
            print("vc put called")

#
#   The "cc" command indicates a change to a new mode (e.g. USB, LSB, etc)
#
    def ccGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("cc get called:", "buffer =", buffer)
            print("cc new mode change")
            print("value=", value, sep='*', end='*')
            print("\n")

    def ccPut(self):
        if self.debugCommandDecoding:
            print("cc put called")

#
#   The "va" command indicates assignment of vfoA to new frequency
#
    def vaGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("va get called:", "buffer =", buffer)
            print("va assign vfo a frequency")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vaPut(self):
        if self.debugCommandDecoding:
            print("va put called")

#
#   The "ca" command indicates assignment of a new mode to vfoA
#
    def caGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ca get called:", "buffer =", buffer)
            print("ca assign mode for vfoa frequecy")
            print("value=", value, sep='*', end='*')
            print("\n")

    def caPut(self):
        if self.debugCommandDecoding:
            print("ca put called")

#
#   The "vb" command indicates assignment of vfoB to new frequency
#
    def vbGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vb get called:", "buffer =", buffer)
            print("vb assign vfo b frequency")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vbPut(self):
        if self.debugCommandDecoding:
            print("vb put called")

#
#   The "cb" command indicates assignment of a new mode to vfoB
#
    def cbGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("cb get called:", "buffer =", buffer)
            print("cb assign mode for vfoB frequecy")
            print("value=", value, sep='*', end='*')
            print("\n")

    def cbPut(self):
        if self.debugCommandDecoding:
            print("cb put called")

#
#   The "cn" command indicates which tuning step is active (1(smallest) - 5(largest)
#
    def cnGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("cn get called:", "buffer =", buffer)
            print("cn which tuning step (1-5)")
            print("value=", value, sep='*', end='*')
            print("\n")

    def cnPut(self):
        if self.debugCommandDecoding:
            print("cn put called")



    #         case "vt":
    #             value = extractValue(command_buffer, 10, len(command_buffer)-3)
    #             if debugCommandDecoding:
    #                 print("vt tone for CW")
    #                 print("value=", value,sep='*',end='*')
    #                 print("\n")
    #         case "ck":
    #             value = extractValue(command_buffer, 10, len(command_buffer)-3)
    #             if debugCommandDecoding:
    #                 print("ck select key for cw")
    #                 print("value=", value,sep='*',end='*')
    #                 print("\n")
    #         case "vs":
    #             value = extractValue(command_buffer, 10, len(command_buffer)-3)
    #             if debugCommandDecoding:
    #                 print("vs word/minute for keyer")
    #                 print("value=", value,sep='*',end='*')
    #                 print("\n")
    #         case "vy":
    #             value = extractValue(command_buffer, 10, len(command_buffer)-3)
    #             if debugCommandDecoding:
    #                 print("vy delay returning after cw key")
    #                 print("value=", value,sep='*',end='*')
    #                 print("\n")
    #         case "ve":
    #             value = extractValue(command_buffer, 10, len(command_buffer)-3)
    #             if debugCommandDecoding:
    #                 print("ve delay for start")
    #                 print("value=", value,sep='*',end='*')
    #                 print("\n")
    #         case _:
    #             print("unimplemented yet command=", command)
    #
    #
    # if debugCommandDecoding:
    #     print("***starting serial procesor***")
    # ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)
    #
    # try:
    #     ffCount = 0
    #     buffer = []
    #     lineNum = 1
    #
    #     while True:
    #         # Read a line from the serial port (until a newline character is received)
    #         # Decode the bytes to a string (e.g., 'utf-8') and remove leading/trailing whitespace
    #
    #         in_byte= ser.read(1)
    #
    #         if in_byte:

    #             if ((len(buffer) == 0) and (in_byte.decode(errors='ignore') != 'p')):
    #                 pass
    #             else:
    #                 if debugCommandDecoding:
    #                     if (len(buffer) == 0):
    #                         print("line ", lineNum)
    #                 buffer.append (in_byte)
    #
    #
    #                 if in_byte.hex() == 'ff':
    #                     ffCount += 1
    #                     if ffCount == 3:
    #
    #                         decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]
    #                         if debugCommandDecoding:
    #                             for item in decoded_buffer_char:
    #                                 print(f"{item:<{4}}", end="")
    #                             print("")
    #
    #                         decoded_buffer_hex = [item.hex() for item in buffer]
    #                         if debugCommandDecoding:
    #                             for item in decoded_buffer_hex:
    #                                 print(f"{item:<{4}}", end="")
    #                             print("")
    #
    #                         decoded_buffer_ord = [ord(item) for item in buffer]
    #                         if debugCommandDecoding:
    #                             for item in decoded_buffer_ord:
    #                                 print(f"{item:<{4}}", end="")
    #                             print("")
    #                         ffCount = 0
    #                         lineNum += 1
    #                         buffer = buffer[:0]
    #                         #
    #                         # process and print it
    #                         #
    #                         decodeCEC_command (decoded_buffer_char)
    #
    #         time.sleep(0.1)  # Small delay to prevent busy-waiting
    #
    #
    # except KeyboardInterrupt:
    #     print("Program terminated by user.")
    # finally:
    #     if ser.is_open:
    #         ser.close()
    #         print("Serial port closed.")
