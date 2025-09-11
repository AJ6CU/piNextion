# from imghdr import test_xbm
import tkinter.ttk as ttk

# from Cython.Compiler.Naming import self_cname

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

        self.vfo_VAR.set("VFO-A")

        # self.vfoB_Freq_Current=None
        # self.vfoB_Mode_Current=None

        self.lock_Button_On = False                 #controls lock of console
        self.speaker_Button_On = False              #On means in Mute/SDR
        self.stop_Button_On = False                 #Emergency stop all tx
        self.split_Button_On = False                #Controls entry into split mode
        self.rit_Button_On = False                  #Controls RIT. On means in RIT mode
        self.att_Button_On = False                  #On allows onscreen control of signal attn
        self.ifs_Button_On = False                  #On allows onscreen mod of the ifs

        self.last_VFODial_Reading = None

        #######################################################################################
        #   Dictionaries that follow are used to lookup textual values based on internal
        #   Representations. Sometimes it is a string integer. Other times it is a string of
        #   a couple characters. These translations are collected here to avoid them being
        #   "codified" directly in the functions that use them.
        #######################################################################################

        self.MCU_Command_To_CB_Dict = {
            "v1": self.v1_UX_Set_Tuning_Rate_1,
            "v2": self.v2_UX_Set_Tuning_Rate_2,
            "v3": self.v3_UX_Set_Tuning_Rate_3,
            "v4": self.v4_UX_Set_Tuning_Rate_4,
            "v5": self.v5_UX_Set_Tuning_Rate_5,
            "ch": self.chGet,
            "vh": self.vhGet,
            "vo": self.voGet,
            "vp": self.vpGet,
            "vq": self.vqGet,
            "sv": self.sv_UX_Set_SW_Version,
            "sc": self.sc_UX_Set_User_Callsign,
            "cm": self.cm_UX_Display_Callsign_Version_Flag,
            "c0": self.c0_UX_In_Yellow_Box_Flag,
            "vc": self.vc_UX_Set_Primary_VFO_Frequency,
            "cc": self.cc_UX_Set_Primary_Mode,
            "va": self.va_UX_Set_VFO_A_Frequency,
            "ca": self.ca_UX_Set_VFO_A_Mode,
            "vb": self.vb_UX_Set_VFO_B_Frequency,
            "cb": self.cb_UX_Set_VFO_B_Mode,
            "cn": self.cn_UX_Set_Active_Tuning_Rate,
            "vt": self.vt_UX_SET_CW_Tone,
            "ck": self.ck_UX_Set_CW_Key_Type,
            "vs": self.vs_UX_Set_CW_Speed,
            "vy": self.vy_UX_Set_CW_Post_Delay,
            "ve": self.ve_UX_Set_CW_Pre_Delay,
            "cv": self.cv_UX_VFO_Toggle,            #sets active VFO, A=0, B=1
            "s0": self.s0Get,
            "vi": self.vi_UX_IFS_Level,
            "cl": self.cl_UX_Lock_Screen,
            "cj": self.cj_UX_Speaker_Toggle,
            "cs": self.cs_UX_SPLIT_Toggle,
            "vr": self.vrGet,
            "cr": self.cr_UX_RIT_Toggle,
            "vf": self.vf_UX_ATT_Level,
            "ci": self.ci_UX_IFA_State_Set,
            "cx": self.cx_UX_TX_Stop_Toggle
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
        self.modeNum_To_TextDict = {
            "2":"LSB",
            "3":"USB",
            "4":"CWL",
            "5":"CWU"
        }

        self.Text_To_ModeNum = {
            "LSB": 2,
            "USB":3,
            "CWL":4,
            "CWU":5
        }

        self.Text_To_BandChange = {
            "UP": 2,
            "DOWN":1
        }
        self.Text_To_VFO= {
            "0": "VFO-A",
            "1": "VFO-B"
        }

    #####################################################################################
    #       End of dictionaries of constants
    #####################################################################################

    def attachRadio(self, radio):
        self.theRadio = radio

    ######################################################################################
    #   This looks up the command processing routing to be called via a dictionary
    #   based on the command type (characters 3,4 in the buffer after prelogue stripped
    ######################################################################################

    def delegate_command_processing(self,command, buffer):
        self.MCU_Command_To_CB_Dict[command](buffer)

    ################################################################################
    #   Format of command sent by radio:
    #   1. Prelog
    #   2. command type: characters 0-2, format "xx." Where "xx" is mostly "pm"
    #   3. subcommand type: characters 3,4  The translation between these characters
    #   and the code that implements them is in the dictionary above "MCU_Command_To_CB_Dict"
    #   4. value: This is the 4 bytes between 10-13. Mostly these are characters. But
    #   in some cases the might represent hex bytes that need to be recoded into an int
    ################################################################################

    def extractValue(self, buffer, start, end):
        returnBuffer =""
        i = start
        while i < end:
            returnBuffer = returnBuffer + buffer[i]
            i +=1
        return returnBuffer.replace('"','')

#####################################################################################
### Start Callbacks
#   These are the callbacks as defined in the GUI Builder pygubu-designer
#####################################################################################

    def settings_CB(self):
        print("settings_CB")

    def vfo_CB(self):
        self.Radio_Toggle_VFO()

    def mode_lsb_CB(self):
        print("lsb change cb called")
        # self.primary_Mode_VAR.set("LSB")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["LSB"])

    def mode_usb_CB(self):
        print("usb change cb called")
        # self.primary_Mode_VAR.set("USB")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["USB"])


    def mode_cwl_CB(self):
        print("cwl change cb called")
        # self.primary_Mode_VAR.set("CWL")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["CWL"])


    def mode_cwu_CB(self):
        print("cwu change cb called")
        # self.primary_Mode_VAR.set("CWU")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["CWU"])

    def band_up_CB(self):
         print("band up")
         self.Radio_Change_Band(self.Text_To_BandChange["UP"])

    def band_down_CB(self):
         print("band down")
         self.Radio_Change_Band(self.Text_To_BandChange["DOWN"])

    def cw_info_CB(self, event=None):
       if (self.lock_Button_On):
           print("lock button on, ignore callback")
       else:
           print("cw_info cb called allowed because lock button off")

#
#   This function sends to the Radio a notice that a screen lock has been requested
#   The actual locking of the screen waits until the Radio sends back a commond
#   to lock the screen. This ensures that the screen is not locked by the UX
#   and the Radio never gets the request for some reason.
#   The sctual locking of screen is set performed by cl_UX_Lock_Screen()
#

    def lock_CB(self):
        self.Radio_Toggle_Lock()    # Inform  Radio that a screen lock has been requested

    def speaker_CB(self):           # Inform Radio that a request was made to mute speaker
        self.Radio_Toggle_Speaker()

    def stop_CB(self):
        self.Radio_Toggle_Stop()

    def split_CB(self):
         self.Radio_Toggle_Split()

    def rit_CB(self):
        self.Radio_Toggle_RIT()

    def store_CB(self):
        print("store_CB")

    def recall_CB(self):
        print("recall_CB")

    def ATT_Jogwheel_ButtonPressed_CB(self, event=None):
        self.ATT_Jogwheel.lastValue = self.ATT_Jogwheel.get()

    def ATT_Jogwheel_ButtonReleased_CB(self, event=None):
        currentValue = self.ATT_Jogwheel.get()
        if self.ATT_Jogwheel.lastValue == currentValue:
            self.toggleATT_State()
        else:
            self.Radio_Set_ATT(currentValue)

    def toggleATT_State(self):

        if self.ATT_Jogwheel.state == "disabled":
            self.ATT_Jogwheel.setStateNormal()
            self.ATT_Status_VAR.set("ATT (ON)")
            self.Radio_Set_ATT(self.ATT_Jogwheel.lastValue)
        else:
            self.ATT_Jogwheel.setStateDisabled()
            self.ATT_Status_VAR.set("ATT (OFF)")
            self.Radio_Set_ATT(0)           # 0 turns off ATT

    def updateATTValue_CB(self):
        self.Radio_Set_ATT(self.ATT_Jogwheel.get())
        print("updateATTValue_CB called")
        print(self.ATT_Jogwheel.get())

    def IFS_Jogwheel_ButtonPressed_CB(self, event=None):
        self.IFS_Jogwheel.lastValue = self.IFS_Jogwheel.get()


    def IFS_Jogwheel_ButtonReleased_CB(self, event=None):
        currentValue = self.IFS_Jogwheel.get()
        if self.IFS_Jogwheel.lastValue == currentValue:
            self.toggleIFS_State()
        else:
            self.Radio_Set_IFS_Level(currentValue)

    def toggleIFS_State(self):

        if self.IFS_Jogwheel.state == "disabled":
            self.IFS_Jogwheel.setStateNormal()
            self.IFS_Status_VAR.set("IFS (ON)")
            self.Radio_Toggle_IFS()                        # toggle IfS
            print("initial value of ifs=",self.IFS_Jogwheel.get())
        else:
            self.IFS_Jogwheel.setStateDisabled()
            self.IFS_Status_VAR.set("IFS (OFF)")
            self.Radio_Toggle_IFS()                        # toggle IfS

    def updateIFSValue_CB(self):
        # conv2BytesToInt32(swr_buffer[commandStartIndex + 4], swr_buffer[commandStartIndex + 5]);
        # conv2BytesToInt32(lsb,msb) (int)((int16_t)((msb<<8) + lsb));
        print("processing value change")
        print(self.IFS_Jogwheel.get())
        self.Radio_Set_IFS_Level(self.IFS_Jogwheel.get())

    def tuning_Step_CB(self):
        print("tuning_Step cb called")



####    Start of command processing sent by Radio to Screen

         #
         #   The "v1" command is used for smallest tuning rate
         #

    def v1_UX_Set_Tuning_Rate_1(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if self.debugCommandDecoding:
            print("v1 get called:", "buffer =", buffer)
            print("v1 tuning 1")
            print("value=", value, sep='*', end='*')
            print("\n")


    def v2_UX_Set_Tuning_Rate_2(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v2 get called:", "buffer =", buffer)
            print("v2 tuning 2")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "v3" command 1s used for the third (middle) tuning rate
        #

    def v3_UX_Set_Tuning_Rate_3(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v3 get called:", "buffer =", buffer)
            print("v3 tuning 3")
            print("value=", value, sep='*', end='*')
            print("\n")



        #
        #   The "v4" command 1s used for the next largest tuning rate
        #

    def v4_UX_Set_Tuning_Rate_4(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v4 get called:", "buffer =", buffer)
            print("v4 tuning 4")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "v5" command 1s used for the largest tuning rate
        #

    def v5_UX_Set_Tuning_Rate_5(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v5 get called:", "buffer =", buffer)
            print("v5 tuning 5")
            print("value=", value, sep='*', end='*')
            print("\n")


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


        #
        #   The "sv" command is stores the text of the firmware version
        #

    def sv_UX_Set_SW_Version(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("sv get called:", "buffer =", buffer)
            print("sv software version")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "sc" command is stores the text of the operators callsign
        #

    def sc_UX_Set_User_Callsign(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("sc get called:", "buffer =", buffer)
            print("sc call sign")
            print("value=", value, sep='*', end='*')
            print("\n")


    #
    #   The "cm" command determines whether call sign and firmware versions are displayed
    #

    def cm_UX_Display_Callsign_Version_Flag(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        # MJH Not complete
        if self.debugCommandDecoding:
            print("cm get called:", "buffer =", buffer)
            print("cm display version and callsign?")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "c0" command determines whether we are in text (yellow box) or graphics mode
        #

    def c0_UX_In_Yellow_Box_Flag(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("c0 get called:", "buffer =", buffer)
            print("c0 text (yellow box) or graphics mode")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "vc" command indicates a new frequency for the Primary
        #

    def vc_UX_Set_Primary_VFO_Frequency(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.primary_VFO_VAR.set(value)

        if self.debugCommandDecoding:
            print("vc get called:", "buffer =", buffer)
            print("vc new frequency change")
            print("value=", value, sep='*', end='*')
            print("\n")

    #
    # The purpose of this command is a little puzzling
    # code talks about this being used to eliminate duplicate data
    # Only sent on the first attempt to lock the screen
    # Also contains the text for the speaker button
    #
    def s0Get(self, buffer):
        print("unknown s0 called from lock screen")
        print("buffer=", buffer)

    #
    #   Received request from Radio to lock the screen
    #
    def viGet(self, buffer):
        print("unknown vi called to confirm new ifs setting")
        print("buffer=", buffer)

    def cl_UX_Lock_Screen(self, buffer):
        print("cl_UX_Lock_Screen requested by Radio")
        if (self.lock_Button_On):
            print("turning normal")
            self.lock_Button_On = False
            self.lock_Button.configure(style='Button2b.TButton', state="normal")
            self.lock_VAR.set("\nLOCK\n")
            self.unlockUX()
        else:
            print("turning red")
            self.lock_Button_On = True
            self.lock_Button.configure(style='RedButton2b.TButton', state='pressed')
            self.lock_VAR.set("\nLOCK-Red\n")
            self.lockUX()

    #
    #   Disable all of the control widgets when a LOCK action is requested
    #
    def lockUX(self):
        self.settings_Button.configure(state = "disabled")
        self.vfo_Button.configure(state="disabled")
        self.mode_select_Menubutton.configure(state="disabled")
        self.band_up_Button.configure(state="disabled")
        self.band_down_Button.configure(state="disabled")
        self.speaker_Button.configure(state="disabled")
        self.split_Button.configure(state="disabled")
        self.rit_Button.configure(state="disabled")
        self.store_Button.configure(state="disabled")
        self.recall_Button.configure(state="disabled")
        # self.att_Button.configure(state="disabled")
        # self.labelScale_Set_State(self.att_LabeledScale,"disabled")
        # self.labelScale_Set_State(self.ifs_LabeledScale, "disabled")
        # self.ifs_Button.configure(state="disabled")
        self.tuning_Step_Button.configure(state="disabled")
        self.ATT_Jogwheel.state = "disabled"
        self.IFS_Jogwheel.state = "disabled"

    #
    #   Reset all widgets to their "normal" state after the  unlock happens
    #
    def unlockUX(self):
        self.settings_Button.configure(state = "normal")
        self.vfo_Button.configure(state="normal")
        self.mode_select_Menubutton.configure(state="normal")
        self.band_up_Button.configure(state="normal")
        self.band_down_Button.configure(state="normal")
        self.speaker_Button.configure(state="normal")
        self.split_Button.configure(state="normal")
        self.rit_Button.configure(state="normal")
        self.store_Button.configure(state="normal")
        self.recall_Button.configure(state="normal")
        # self.att_Button.configure(state="normal")
        # self.labelScale_Set_State(self.att_LabeledScale,"normal")
        # self.labelScale_Set_State(self.ifs_LabeledScale, "normal")
        # self.ifs_Button.configure(state="normal")
        self.tuning_Step_Button.configure(state="normal")
        self.ATT_Jogwheel.state="normal"
        self.IFS_Jogwheel.state="normal"

    # def labelScale_Set_State(self, labeledScale, newstate):
    #     #
    #     #   disabling/enabling a label scale requires disabling its children
    #     #
    #     for child in labeledScale.winfo_children():
    #         if hasattr(child,'state'):
    #             child.configure(state=newstate)


    def cj_UX_Speaker_Toggle(self, buffer):
        print("cj_UX_Speaker_Toggle requested by Radio")
        if (self.speaker_Button_On):
            print("unmuting audio")
            self.speaker_Button_On = False
            self.speaker_Button.configure(style='Button2b.TButton', state="normal")
            self.speaker_VAR.set("\nSPEAKER\n")
        else:
            print("muting audio")
            self.speaker_Button_On = True
            self.speaker_Button.configure(style='RedButton2b.TButton', state="pressed")
            self.speaker_VAR.set("\nMuted-Red\n")


    def cs_UX_SPLIT_Toggle(self, buffer):
        print("cs_UX_SPLIT_Toggle called to confirm split mode")  # command is split
        if (self.split_Button_On):
            print("exiting split mode")
            self.split_Button_On = False
            self.split_Button.configure(style='Button2b.TButton', state="normal")
        else:
            print("going into split mode")
            self.split_Button_On = True
            self.split_Button.configure(style='GreenButton2b.TButton', state="pressed")

    def vrGet(self, buffer):
        print("unknown vr called")  # command is rit related

    def cr_UX_RIT_Toggle(self, buffer):
        print("cr_UX_RIT_Toggle called to confirm RIT mode")  # command is split
        if (self.rit_Button_On):
            print("exiting RIT mode")
            self.rit_Button_On = False
            self.rit_Button.configure(style='Button2b.TButton', state="normal")
        else:
            print("going into RIT mode")
            self.rit_Button_On = True
            self.rit_Button.configure(style='GreenButton2b.TButton', state="pressed")

    def vf_UX_ATT_Level(self, buffer):
        value = int(self.extractValue(buffer, 10, len(buffer) - 3))

        if (int(self.ATT_Jogwheel.get() != value) and (self.ATT_Jogwheel.state == "normal")):
            print("ack value failed to matched!")
            print("state=", self.ATT_Jogwheel.state)
            print(self.ATT_Jogwheel.get())
            print(buffer)
            # print("resetting to current value")
            # self.Radio_Set_ATT(self.ATT_Jogwheel.get())



    def ci_UX_IFA_State_Set(self, buffer):
        print("ci called to confirm ifs mode")  # command is ifs
        print("buffer=", buffer)
        value = int(self.extractValue(buffer, 10, len(buffer) - 3))
        if (self.IFS_Jogwheel.state == "normal") and (value != 1):
            print("mcu says state off, ux says state is on")
        elif (self.IFS_Jogwheel.state == "disabled") and (value != 0):
            print("mcu says state on, ux says state is off")
        else:
            print("MCU and UX agree")

    def vi_UX_IFS_Level(self, buffer):      #verification by MCU of new value
        value = int(self.extractValue(buffer, 10, len(buffer) - 3))

        if (int(self.IFS_Jogwheel.get() != value) and (self.IFS_Jogwheel.state == "normal")):
            print("IFS ack value failed to matched!")
            print("state=", self.IFS_Jogwheel.state)
            print(self.IFS_Jogwheel.get())
            print(buffer)
            # print("resetting MCU to IFS to of UX")
            # self.Radio_Set_IFS_Level(self.IFS_Jogwheel.get())
        else:
            print("IFS mcu and UX agree, value=", value)




    def cx_UX_TX_Stop_Toggle(self, buffer):
        print("cx_UX_TX_Stop_Toggle called to toggle stop mode")  # command is split
        if (self.stop_Button_On):
            print("exiting TX Stop mode")
            self.stop_Button_On = False
            self.stop_Button.configure(style='Button2b.TButton', state="normal")
        else:
            print("going into TX Stop mode")
            self.stop_Button_On = True
            self.stop_Button.configure(style='RedButton2b.TButton', state="pressed")


    def Radio_Toggle_VFO(self):
        command = [self.toRadioCommandDict["TS_CMD_VFO"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Lock(self):
        print("lock toggle")
        command = [self.toRadioCommandDict["TS_CMD_LOCK"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Speaker(self):
        print("speaker toggle")
        command = [self.toRadioCommandDict["TS_CMD_SDR"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Stop(self):
        print("stop toggle")
        command = [self.toRadioCommandDict["TS_CMD_TXSTOP"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Split(self):
        print("split toggle")
        command = [self.toRadioCommandDict["TS_CMD_SPLIT"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_RIT(self):
        print("RIT toggle")
        command = [self.toRadioCommandDict["TS_CMD_RIT"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Set_ATT(self,value: bytes):
        print("ATT Set")
        command = [self.toRadioCommandDict["TS_CMD_ATT"],value,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_IFS(self):
        print("IFS toggle")
        print("IFS value =", self.IFS_Jogwheel.get())
        command = [self.toRadioCommandDict["TS_CMD_IFS"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Set_IFS_Level(self,level):
        print("IFS Set Level =", level)
        intLevel = int(level)
        print("int level=", hex(intLevel))
        firstByte = intLevel & 0xff
        print("firstByte=", firstByte)
        secondByte = (intLevel >> 8) & 0xff
        print("secondByte=", secondByte)
        thirdByte = (intLevel >> 16) & 0xff
        print("thirdByte=", thirdByte)
        command = [self.toRadioCommandDict["TS_CMD_IFSVALUE"],firstByte,secondByte,thirdByte,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    #
    #   The "cc" command indicates a change to a new mode (e.g. USB, LSB, etc.)
    #

    def cc_UX_Set_Primary_Mode(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.primary_Mode_VAR.set(self.modeNum_To_TextDict[value])
        if self.debugCommandDecoding:
            print("cc get called:", "buffer =", buffer)
            print("cc new mode change")
            print("value=", value, sep='*', end='*')
            print("\n")

    #
    #   This function tells the Radio that a new mode has been selected for
    #   the primary (displayed) VFO. After receiving the new mode, the
    #   Radio will separately send back the mode to the UX
    #
    def cc_Radio_Set_Mode(self, newMode):
        command = [self.toRadioCommandDict["TS_CMD_MODE"],newMode,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))
    #
    #   This function tells the Radio that a button up or down has been pushed
    #   in the UX. After receiving this command the radio will send back a new frequency
    #   and mode for the displayed VOF
    #
    def Radio_Change_Band(self, direction):
        command = [self.toRadioCommandDict["TS_CMD_BAND"],direction,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    #
    #   The "va" command indicates assignment of vfoA to new frequency
    #

    def va_UX_Set_VFO_A_Frequency(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("va get called:", "buffer =", buffer)
            print("va assign vfo a frequency")
            print("value=", value, sep='*', end='*')
            print("\n")
        self.primary_VFO_VAR.set(value)


        #
        #   The "ca" command indicates assignment of a new mode to vfoA
        #

    def ca_UX_Set_VFO_A_Mode(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        self.primary_Mode_VAR.set(self.modeNum_To_TextDict[value])

        if self.debugCommandDecoding:
            print("ca get called:", "buffer =", buffer)
            print("ca assign mode for vfoA frequency")
            print("value=", value, sep='*', end='*')
            print("\n")



        #
        #   The "vb" command indicates assignment of vfoB to new frequency
        #

    def vb_UX_Set_VFO_B_Frequency(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.secondary_VFO_VAR.set(value)
        if self.debugCommandDecoding:
            print("vb get called:", "buffer =", buffer)
            print("vb assign vfo b frequency")
            print("value=", value, sep='*', end='*')
            print("\n")
    #
    #   This sets VFO B to a new mode
    #

    def cb_UX_Set_VFO_B_Mode(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.secondary_Mode_VAR.set(self.modeNum_To_TextDict[value])
        if self.debugCommandDecoding:
            print("cb get called:", "buffer =", buffer)
            print("cb assign mode for vfoB frequency")
            print("value=", value, sep='*', end='*')
            print("\n")



        #
        #   The "cn" command indicates which tuning step is active (1(smallest) - 5(largest)
        #

    def cn_UX_Set_Active_Tuning_Rate(self, buffer):

        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Step_Button_VAR.set("100")
        if self.debugCommandDecoding:
            print("cn get called:", "buffer =", buffer)
            print("cn which tuning step (1-5)")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "vt" command stores the CW tone
        #

    def vt_UX_SET_CW_Tone(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vt get called:", "buffer =", buffer)
            print("vt tone for CW")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "ck" command stores which cw key is being used
        #

    def ck_UX_Set_CW_Key_Type(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ck get called:", "buffer =", buffer)
            print("ck select key for cw")
            print("value=", value, sep='*', end='*')
            print("\n")



        #
        #   The "vs" command stores words/minute
        #

    def vs_UX_Set_CW_Speed(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vs get called:", "buffer =", buffer)
            print("vs word/minute for keyer")
            print("value=", value, sep='*', end='*')
            print("\n")


        #
        #   The "vy" command stores delay returning after last cw character
        #

    def vy_UX_Set_CW_Post_Delay(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vy get called:", "buffer =", buffer)
            print("vy delay returning after cw key")
            print("value=", value, sep='*', end='*')
            print("\n")



        #
        #   The "ve" command stores delay prior to TX 1st cw character
        #

    def ve_UX_Set_CW_Pre_Delay(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("ve get called:", "buffer =", buffer)
            print("ve start delay for first cw character")
            print("value=", value, sep='*', end='*')
            print("\n")

    #
    #   Returns active VFO, VFO-A=0, VFO-B=1
    def cv_UX_VFO_Toggle(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if self.debugCommandDecoding:
            print("cv get called:", "buffer =", buffer)
            print("cv toggle vfo")
            print("value=", value, sep='*', end='*')
            print("\n")

        self.vfo_VAR.set(self.Text_To_VFO[value])
        self.secondary_VFO_VAR.set(self.primary_VFO_VAR.get())
        self.secondary_Mode_VAR.set(self.primary_Mode_VAR.get())


