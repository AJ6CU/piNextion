import serial
from time import sleep
from timeit import default_timer as timer
from configuration import configuration
import globalvars as gv
from tkinter import messagebox

from comportManager import *


class piRadio:
    def __init__(self, serialPortName, serialPort, window, debugFlag=True):
        self.debugCommandDecoding = debugFlag
        self.tty = serialPortName
        serial
        self.mainWindow = window
        self.radioPort = serialPort

        self.MCU_Update_Period = gv.config.get_MCU_Update_Period()
        gv.config.register_observer("MCU Update Period", self.updateMCU_Update_Period)

        self.MCU_Command_Headroom = gv.config.get_MCU_Command_Headroom()
        gv.config.register_observer("MCU Command Headroom", self.updateMCU_Command_Headroom)

        # print("update period is ", self.MCU_Update_Period)
        # print("command headroom = ", self.MCU_Command_Headroom)


#   note on external device to MCU protocol
        #   Proceeded by 3 bytes ("preamble), completed by 3 bytes ("postscript)
        #   In the middle there are 5 bytes tha are in one of two formats
        #   1. First byte is the command, 2nd byte is a subfunction and 3-5 bytes are not used and 0x0
        #   e.g. Mode change is command "1" and second byte selects the mode. 2= LSB, 3=USB, etc.
        #   The last 4 bytes could also be characters for 4 digits (e.g. v1-5 for tuning)
        #   2. First byte is the command and the remaining 4 bytes encode a number.
        #   e.g. Frequency is set with a "4" The remaining 4 bytes shift at 24 bit, 2nd 16, etc. and
        #   then add them together for the frequency

        self.tx_to_mcu_preamble = b'\x59\x58\x68'       # all commands to MCU must start with these three bytes
        self.tx_to_mcu_postscript = b'\xff\xff\x73'     # all commands to MCU must end with these three numbers

        self.mcu_command_buffer =[]                     # buffer used to send bytes to MCU
        self.time_of_last_sent = timer()                # used to avoid overloading MCU



    # def openRadio(self):
    #
    #     if self.debugCommandDecoding:
    #         print("***opening port to radio***")
    #     try:
    #         self.radioPort = serial.Serial(self.tty, 9600, timeout=0)
    #     except:
    #         return   # serial.SerialException as e:
    #
    #     return

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
    def processRadioCommand(self, buffer):
        command = buffer[3]  + buffer[4]
        self.mainWindow.delegate_command_processing (command, buffer)

    def rebootRadio(self):
        # self.openRadio()
        command=[0x5f,0x6c,0x48,0x45,0x59]
        self.sendCommandToMCU(bytes(command))

#
#   Read and process all the values sent at startup of radio
#
    def readALLValues(self):

        ffCount = 0
        buffer = []
        commandCount = 0

        while commandCount < 26:
            # Read a line from the serial port (until a newline character is received)
            # Decode the bytes to a string (e.g., 'utf-8') and remove leading/trailing whitespace

            in_byte= self.radioPort.read(1)

            if in_byte:
                #
                #   Looking for the first line with a "p" in the first character
                #   CEC sends a zero to start, just ignore it
                #
                if ((len(buffer) == 0) and (in_byte.decode(errors='ignore') != 'p')):
                    pass
                else:
                    buffer.append (in_byte)


                    if in_byte.hex() == 'ff':
                        ffCount += 1
                        if ffCount == 3:
                            #
                            #   decode the characters into ascii
                            #
                            decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]

                            # if self.debugCommandDecoding:
                            #     for item in decoded_buffer_char:
                            #         print(f"{item:<{4}}", end="")
                            #     print("")

                            # decoded_buffer_hex = [item.hex() for item in buffer]
                                # for item in decoded_buffer_hex:
                                #     print(f"{item:<{4}}", end="")
                                # print("")

                            # decoded_buffer_ord = [ord(item) for item in buffer]
                                # for item in decoded_buffer_ord:
                                #     print(f"{item:<{4}}", end="")
                                # print("")
                            #
                            #   since we saw 3 0xff's in a row, we can call the getter to
                            #   set the value in the UX
                            #
                            self.processRadioCommand(decoded_buffer_char)
                            #
                            #   reset counters (and add one to total processed)
                            #
                            ffCount = 0
                            buffer = buffer[:0]
                            commandCount += 1

            # time.sleep(0.1)  # Small delay to prevent busy-waiting

    def updateData(self, repeatFlag=True):
        ffCount = 0
        buffer = []
        while self.radioPort.in_waiting > 0:
            #
            #   Get command
            #
            in_byte = self.radioPort.read(1)

            if in_byte:
                #
                #   Looking for the first line with a "p" in the first character
                #   CEC sends a zero to start, just ignore it
                #
                if ((len(buffer) == 0) and (in_byte.decode(errors='ignore') != 'p')):
                    pass
                else:

                    buffer.append(in_byte)

                    if in_byte.hex() == 'ff':
                        ffCount += 1
                        if ffCount == 3:
                            #
                            #   decode the characters into ascii
                            #
                            decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]
                            #
                            #   since we saw 3 0xff's in a row, we can call the getter to
                            #   set the value in the UX
                            #
                            self.processRadioCommand(decoded_buffer_char)
                            #
                            #   reset counters (and add one to total processed)
                            #
                            ffCount = 0
                            buffer = buffer[:0]
        if repeatFlag:
            self.mainWindow.after(self.MCU_Update_Period,self.updateData)
#
#   Send command to MCU
#
    def sendCommandToMCU(self, commandList):

        currentTime = timer()
        timeDiff = currentTime - self.time_of_last_sent

        if (timeDiff < self.MCU_Command_Headroom):
            sleep(self.MCU_Command_Headroom - timeDiff)
        self.time_of_last_sent = timer()

        self.tx_to_mcu_preamble = b'\x59\x58\x68'  # all commands to MCU must start with these three bytes
        self.tx_to_mcu_postscript = b'\xff\xff\x73'  # all commands to MCU must end with these three numbers

        try:
            self.radioPort.write(self.tx_to_mcu_preamble + commandList + self.tx_to_mcu_postscript)
        except:
            messagebox.showerror(title="ERROR Communicating with uBITX",
                                                     message="Communication failed with uBITX.", parent=self,
                                 DETAILS="Did you select the right com port?\n"+"You selected: "+ self.tty)
            sys.exit(-1)



    def updateMCU_Update_Period(self, value):
        self.MCU_Update_Period = value
        print("update period is changing, now = ", self.MCU_Update_Period)

    def updateMCU_Command_Headroom(self, value):
        self.MCU_Command_Headroom = value
        print("update MCU Command Headroom is changing, now = ", self.MCU_Command_Headroom)


