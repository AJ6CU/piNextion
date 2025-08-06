import serial
import time

#from piCEC_UX.pygubu.piCEC_UX import mainWindow


class piRadio:
    def __init__(self, serialPort, window, debugFlag):
        self.debugCommandDecoding = debugFlag
        self.tty = serialPort
        self.mainWindow = window
        self.radioPort = None

        self.tx_to_mcu_preamble = [0x59,0x58,0x68]      # all commands to MCU must start with these three bytes
        self.tx_to_mcu_postscript = [0x00,0x00,0x00,0xff,0xff,0x73]    # all commands to MCU must end with these three numbers
        self.tx_select_tuning = [0x59,0x58,0x68,0x11,0x05,0x00,0x00,0x00,0xff,0xff,0x73]
        self.tx_bandup = [0x59, 0x58, 0x68, 0x03, 0x02, 0x00, 0x00, 0x00, 0xff, 0xff, 0x73]
        self.mcu_command_buffer =[]                     # buffer used to send bytes to MCU


    def openRadio(self):

        if self.debugCommandDecoding:
            print("***opening port to radio***")
        try:
            self.radioPort = serial.Serial(self.tty, 9600, timeout=0)
        except serial.SerialException as e:
            print(f"Serial port error: {e}")
        return



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
        if self.debugCommandDecoding:
            print("found command = ", command)
        self.mainWindow.delegate_command_processing (command, buffer)


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
            #print("just tried read, in_byte=", in_byte)

            if in_byte:
                #
                #   Looking for the first line with a "p" in the first character
                #   CEC sends a zero to start, just ignore it
                #
                if ((len(buffer) == 0) and (in_byte.decode(errors='ignore') != 'p')):
                    pass
                else:
                    if self.debugCommandDecoding:
                        if (len(buffer) == 0):
                            print("line ", commandCount)
                    buffer.append (in_byte)


                    if in_byte.hex() == 'ff':
                        ffCount += 1
                        if ffCount == 3:
                            #
                            #   decode the characters into ascii
                            #
                            decoded_buffer_char = [item.decode(errors='ignore') for item in buffer]

                            if self.debugCommandDecoding:
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

    def updateData(self):
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
        self.mainWindow.after(500,self.updateData)
#
#   Send command to MCU
#
    def sendCommandToMCU(self, commandList):
        print("command")
        buffer = []
        buffer.extend (self.tx_to_mcu_preamble)
        print(bytes(buffer))
        buffer.extend(commandList)
        print(bytes(buffer))
        buffer.extend (self.tx_to_mcu_postscript)
        print(bytes(buffer))

        buffer_bytes = bytes(buffer)

        print(buffer)
        print (buffer_bytes.hex())
        # for item in buffer_bytes:
        #     self.radioPort.write(item)
        print("changing tuning")
        for item in self.tx_select_tuning:
            self.radioPort.write(item)
            print(item)
        print("changing band")
        for item in self.tx_bandup:
            self.radioPort.write(item)
            print(item)

        print("changing mode")
        for item in buffer_bytes:
            self.radioPort.write(item)
            print(item)
        #
        # for item in self.tx_to_mcu_preamble:
        #
        # for item in self.tx_to_mcu_preamble:
        #     self.radioPort.write(item)
        #
        # for item in commandList:
        #     self.radioPort.write(bytes(item))
        #
        # for item in self.tx_to_mcu_postscript:
        #     self.radioPort.write(item)
        #
        # self.radioPort.flush()
