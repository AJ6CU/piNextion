import piCEC_UXui as baseui
import mystyles  # Styles definition module


class piCECNextion(baseui.piCECNextionUI):
    def __init__(self, master=None, **kw):
        super().__init__(
            master,
            translator=None,
            on_first_object_cb=mystyles.setup_ttk_styles,
        )
        self.theRadio = None
        self.debugCommandDecoding = True

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
            "vt": self.vtGet,
            "ck": self.ckGet,
            "vs": self.vsGet,
            "vy": self.vyGet,
            "ve": self.veGet
        }
        self.putterCB_Dict = {
            "v1": self.v1Put,
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
            "vc": self.vcPut,
            "cc": self.ccPut,
            "va": self.vaPut,
            "ca": self.caPut,
            "vb": self.vbPut,
            "cb": self.cbPut,
            "cn": self.cnPut,
            "vt": self.vtPut,
            "ck": self.ckPut,
            "vs": self.vsPut,
            "vy": self.vyPut,
            "ve": self.vePut
        }
        self.toRadioCommandDict = {
            "TS_CMD_MODE":1,
            "TS_CMD_FREQ":2,
            "TS_CMD_BAND":3,
            "TS_CMD_VFO":4,
            "TS_CMD_SPLIT":5,
            "TS_CMD_RIT":6,
            "TS_CMD_TXSTOP":7,
            "TS_CMD_SDR":8,
            "TS_CMD_LOCK":9,            # Dial Lock
            "TS_CMD_ATT":10,            # ATT
            "TS_CMD_IFS":11,            # IFS Enabled
            "TS_CMD_IFSVALUE":12,       # IFS VALUE
            "TS_CMD_STARTADC":13,
            "TS_CMD_STOPADC":14,
            "TS_CMD_SPECTRUMOPT":15,    # Option for Spectrum
            "TS_CMD_SPECTRUM":16,       # Get Spectrum Value
            "TS_CMD_TUNESTEP":17,       # Get Spectrum Value
            "TS_CMD_WPM":18,            # Set WPM
            "TS_CMD_KEYTYPE":19,        # Set KeyType
            "TS_CMD_SWTRIG":21,         # SW Action Trigger for WSPR and more
            "TS_CMD_READMEM":31,        # Read EEProm
            "TS_CMD_WRITEMEM":32,       # Write EEProm
            "TS_CMD_LOOPBACK0":74,      # Loopback1 (Response to Loopback Channgel)
            "TS_CMD_LOOPBACK1":75,      # Loopback2 (Response to Loopback Channgel)
            "TS_CMD_LOOPBACK2":76,      # Loopback3 (Response to Loopback Channgel)
            "TS_CMD_LOOPBACK3":77,      # Loopback4 (Response to Loopback Channgel)
            "TS_CMD_LOOPBACK4":78,      # Loopback5 (Response to Loopback Channgel)
            "TS_CMD_LOOPBACK5":79,      # Loopback6 (Response to Loopback Channgel)
            "TS_CMD_FACTORYRESET":85,   # Factory Reset
            "TS_CMD_UBITX_REBOOT":95    # Reboot
        }
        self.modeDict = {
            "2":"LSB",
            "3":"USB",
            "4":"CWL",
            "5":"CWU"
        }

    def attachRadio(self, radio):
        self.theRadio = radio
    def delegate_command_processing(self,command, buffer):
        self.getterCB_Dict[command](buffer)

    def extractValue(self, buffer, start, end):
        returnBuffer =""
        i = start
        while i < end:
            returnBuffer = returnBuffer + buffer[i]
            i +=1
        return returnBuffer.replace('"','')

    def mode_lsb_CB(self):
        print("lsb change cb called")
        self.mode_select_VAR.set("LSB")
        self.ccPut(2)

    def mode_usb_CB(self):
        print("usb change cb called")
        self.mode_select_VAR.set("USB")
        self.ccPut(3)


    def mode_cwl_CB(self):
        print("cwl change cb called")
        self.mode_select_VAR.set("CWL")
        self.ccPut(4)


    def mode_cwu_CB(self):
        print("cwu change cb called")
        self.mode_select_VAR.set("CWU")
        self.ccPut(5)

    def band_up_CB(self):
         print("band up")

         tx_mode_switch_USB2pre = b'\x59\x58\x68\x03'
         tx_mode_switch_USB2com = b'\x02\x00\x00\x00'
         tx_mode_switch_USB2post = b'\xff\xff\x73'
         tx_mode_switch_USB2 = tx_mode_switch_USB2pre + tx_mode_switch_USB2com + tx_mode_switch_USB2post
         print('command =', tx_mode_switch_USB2)
         self.theRadio.radioPort.write(tx_mode_switch_USB2)

         #
         #   The "v1" command is used for smallest tuning rate
         #

    def v1Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if self.debugCommandDecoding:
            print("v1 get called:", "buffer =", buffer)
            print("v1 tuning 1")
            print("value=", value, sep='*', end='*')
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
            print("value=", value, sep='*', end='*')
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
            print("sc call sign")
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
        self.primary_VFO_VAR.set(value)

        if self.debugCommandDecoding:
            print("vc get called:", "buffer =", buffer)
            print("vc new frequency change")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vcPut(self):
        if self.debugCommandDecoding:
            print("vc put called")

        #
        #   The "cc" command indicates a change to a new mode (e.g. USB, LSB, etc.)
        #

    def ccGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.mode_select_VAR.set(self.modeDict[value])
        if self.debugCommandDecoding:
            print("cc get called:", "buffer =", buffer)
            print("cc new mode change")
            print("value=", value, sep='*', end='*')
            print("\n")

    def ccPut(self, newMode):
        temp_Buffer = []

        if self.debugCommandDecoding:
            print("cc put called")

        temp_Buffer.append(self.toRadioCommandDict["TS_CMD_MODE"])
        temp_Buffer.append(newMode)
        print("decoded string =", temp_Buffer)

        #
        # decoded_buffer_hex = [item.hex() for item in buffer]
        # for item in decoded_buffer_hex:
        #     print(f"{item:<{4}}", end="")
        # print("")
        temp = 5
        temp_bin = temp.to_bytes(1, byteorder='little')
        tx_mode_switch_USB2pre = b'\x59\x58\x68\x01'
        tx_mode_switch_USB2com = temp_bin + b'\x00\x00\x00'
        tx_mode_switch_USB2post = b'\xff\xff\x73'
        tx_mode_switch_USB2 = tx_mode_switch_USB2pre + tx_mode_switch_USB2com + tx_mode_switch_USB2post
        print('command =', tx_mode_switch_USB2)
        self.theRadio.radioPort.write(tx_mode_switch_USB2)

        # self.sendCommandToMCU(tx_mode_switch_USB2)
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
        self.primary_VFO_VAR.set(value)

    def vaPut(self):
        if self.debugCommandDecoding:
            print("va put called")

        #
        #   The "ca" command indicates assignment of a new mode to vfoA
        #

    def caGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        self.mode_select_VAR.set(self.modeDict[value])

        if self.debugCommandDecoding:
            print("ca get called:", "buffer =", buffer)
            print("ca assign mode for vfoA frequency")
            print("value=", value, sep='*', end='*')
            print("\n")

    def caPut(self, newMode):
        if self.debugCommandDecoding:
            print("ca put called")
        temp_Buffer = []

        temp_Buffer.append(self.toRadioCommandDict["TS_CMD_MODE"])
        temp_Buffer.append(newMode)
        # print("decoded string =", temp_Buffer)

        #
        # decoded_buffer_hex = [item.hex() for item in buffer]
        # for item in decoded_buffer_hex:
        #     print(f"{item:<{4}}", end="")
        # print("")

        self.sendCommandToMCU(temp_Buffer)

        #
        #   The "vb" command indicates assignment of vfoB to new frequency
        #

    def vbGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.secondary_VFO_VAR.set(value)
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
        self.secondary_Mode_VAR.set(self.modeDict[value])
        if self.debugCommandDecoding:
            print("cb get called:", "buffer =", buffer)
            print("cb assign mode for vfoB frequency")
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
        self.tuning_Step_Button_VAR.set("100")
        if self.debugCommandDecoding:
            print("cn get called:", "buffer =", buffer)
            print("cn which tuning step (1-5)")
            print("value=", value, sep='*', end='*')
            print("\n")

    def cnPut(self):
        if self.debugCommandDecoding:
            print("cn put called")

        #
        #   The "vt" command stores the CW tone
        #

    def vtGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vt get called:", "buffer =", buffer)
            print("vt tone for CW")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vtPut(self):
        if self.debugCommandDecoding:
            print("vt put called")

        #
        #   The "ck" command stores which cw key is being used
        #

    def ckGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ck get called:", "buffer =", buffer)
            print("ck select key for cw")
            print("value=", value, sep='*', end='*')
            print("\n")

    def ckPut(self):
        if self.debugCommandDecoding:
            print("ck put called")

        #
        #   The "vs" command stores words/minute
        #

    def vsGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vs get called:", "buffer =", buffer)
            print("vs word/minute for keyer")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vsPut(self):
        if self.debugCommandDecoding:
            print("vs put called")

        #
        #   The "vy" command stores delay returning after last cw character
        #

    def vyGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vy get called:", "buffer =", buffer)
            print("vy delay returning after cw key")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vyPut(self):
        if self.debugCommandDecoding:
            print("vy put called")

        #
        #   The "ve" command stores delay returning after last cw character
        #

    def veGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ve get called:", "buffer =", buffer)
            print("ve start delay for first cw character")
            print("value=", value, sep='*', end='*')
            print("\n")

    def vePut(self):
        if self.debugCommandDecoding:
            print("ve put called")