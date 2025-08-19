from imghdr import test_xbm

from Cython.Compiler.Naming import self_cname

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

        # self.ATT_Jogwheel.configure(command=self.updateATTValue_CB)
        self.ATT_Jogwheel.command = self.updateATTValue_CB
        self.ATT_Jogwheel.setState("disabled")
        self.IFS_Jogwheel.command=self.updateIFSValue_CB
        self.IFS_Jogwheel.setState("disabled")



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
            "cc": self.cc_UX_Set_Mode,
            "va": self.vaGet,
            "ca": self.caGet,
            "vb": self.vbGet,
            "cb": self.cbGet,
            "cn": self.cnGet,
            "vt": self.vtGet,
            "ck": self.ckGet,
            "vs": self.vsGet,
            "vy": self.vyGet,
            "ve": self.veGet,
            "cv": self.cvGet,            #sets active VFO, A=0, B=1
            "s0": self.s0Get,
            "cl": self.cl_UX_Lock_Screen,
            "cj": self.cj_UX_Speaker_Toggle,
            "cs": self.csGet,
            "vr": self.vrGet,
            "cr": self.crGet,
            "ci": self.ciGet,
            "cx": self.cxGet
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

    def settings_CB(self):
        print("settings_CB")

    def vfo_CB(self):
        print("primary vfo =",self.primary_VFO_VAR.get())
        print("current mode =",self.primary_Mode_VAR.get())
        self.secondary_VFO_VAR.set(self.primary_VFO_VAR.get())
        self.secondary_Mode_VAR.set(self.primary_Mode_VAR.get())
        print("secondary vfo =",self.secondary_VFO_VAR.get())
        print("current mode =",self.secondary_Mode_VAR.get())

        self.Radio_Toggle_VFO()

    def mode_lsb_CB(self):
        print("lsb change cb called")
        self.primary_Mode_VAR.set("LSB")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["LSB"])

    def mode_usb_CB(self):
        print("usb change cb called")
        self.primary_Mode_VAR.set("USB")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["USB"])


    def mode_cwl_CB(self):
        print("cwl change cb called")
        self.primary_Mode_VAR.set("CWL")
        self.cc_Radio_Set_Mode(self.Text_To_ModeNum["CWL"])


    def mode_cwu_CB(self):
        print("cwu change cb called")
        self.primary_Mode_VAR.set("CWU")
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
        if (self.stop_Button_On):
            self.stop_Button_On = False
        else:
            self.stop_Button_On = True
        self.Radio_Toggle_Stop()

    def split_CB(self):
        if(self.split_Button_On):
            self.split_Button_On = False
        else:
            self.split_Button_On = True
        self.Radio_Toggle_Split()

    def rit_CB(self):
        if(self.rit_Button_On):
            self.rit_Button_On = False
        else:
            self.rit_Button_On = True
        self.Radio_Toggle_RIT()

    def store_CB(self):
        print("store_CB")

    def recall_CB(self):
        print("recall_CB")

    def att_CB(self):
        # Is ATT Command correctly implemented? on goes to 46hex
#         if(hATT.val==0)
# {
#   //Set Default ATT Level
#   rSendData.val=70			//ATT Value
# }else
# {
#   rSendData.val=0				//ATT Value
# }
        if(self.att_Button_On):
            self.att_Button_On = False
        else:
            self.att_Button_On = True
        self.Radio_Toggle_ATT()
    def updateATTValue_CB(self):
        print("updateATTValue_CB called")

    def IFS_Jogwheel_ButtonPressed_CB(self, event=None):
        print(">>>Jogwheel Button Pressed called")
        currentState = self.IFS_Jogwheel.getState()
        self.IFS_Jogwheel.lastValue = self.IFS_Jogwheel.get()
        print("current state =",currentState)
        print("IFS current value=", self.IFS_Jogwheel.lastValue)
    def toggleIFS_State(self):
        if self.IFS_Jogwheel.getState() == "disabled":
            self.IFS_Jogwheel.setState("normal")
            print("Changing state to normal")
        else:
            self.IFS_Jogwheel.setState("disabled")
            print("changing state to disabled")

    def IFS_Jogwheel_ButtonReleased_CB(self, event=None):
        print("<<<Jogwheel Button Released called")
        currentState = self.IFS_Jogwheel.getState()
        currentValue = self.IFS_Jogwheel.get()
        if self.IFS_Jogwheel.lastValue == currentValue:
            print("no movement detected, can change state")
            self.toggleIFS_State()
        else:
            print("movement detected no chamge in state")

        print("current state =",self.IFS_Jogwheel.getState())

    def ifs_CB(self):
        if(self.ifs_Button_On):
            self.ifs_Button_On = False
        else:
            self.ifs_Button_On = True
        self.Radio_Toggle_IFS()


    def updateIFSValue_CB(self):
        print("updateIFSValue_CB called")
        currentState = self.IFS_Jogwheel.getState()
        print("current state =",currentState)
        if(currentState == "normal"):
            print("processing value change")
        else:
            print("ignorming value change")

    def tuning_Step_CB(self):
        print("tuning_Step cb called")

    def dialClicked(self, event=None):
        print("Dial Clicked")
        self.last_VFODial_Reading=self.dial1.get()
        print(self.dial1.get())

    def dialReleased(self, event=None):
        print("Dial Released")
        currentVFO = self.dial1.get()
        print(self.dial1.get())
        if currentVFO != self.last_VFODial_Reading:
            self.last_VFODial_Reading=currentVFO
            print("movement detected")
        else:
            print("no movement detected, toggle button")



####    Start of command processing sent by Radio to Screen

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


    def v2Get(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("v2 get called:", "buffer =", buffer)
            print("v2 tuning 2")
            print("value=", value, sep='*', end='*')
            print("\n")


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

    def svGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("sv get called:", "buffer =", buffer)
            print("sv software version")
            print("value=", value, sep='*', end='*')
            print("\n")


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
        self.att_Button.configure(state="disabled")
        self.labelScale_Set_State(self.att_LabeledScale,"disabled")
        self.labelScale_Set_State(self.ifs_LabeledScale, "disabled")
        self.ifs_Button.configure(state="disabled")
        self.tuning_Step_Button.configure(state="disabled")

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
        self.att_Button.configure(state="normal")
        self.labelScale_Set_State(self.att_LabeledScale,"normal")
        self.labelScale_Set_State(self.ifs_LabeledScale, "normal")
        self.ifs_Button.configure(state="normal")
        self.tuning_Step_Button.configure(state="normal")

    def labelScale_Set_State(self, labeledScale, newstate):
        #
        #   disabling/enabling a label scale requires disabling its children
        #
        for child in labeledScale.winfo_children():
            if hasattr(child,'state'):
                child.configure(state=newstate)


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


    def csGet(self, buffer):
        print("unknown cs called to confirm split mode")  # command is split

    def vrGet(self, buffer):
        print("unknown vr called to confirm rit mode")  # command is rit related

    def crGet(self, buffer):
        print("unknown cr called to confirm split mode")  # command is rit


    def ciGet(self, buffer):
        print("unknown ci called to confirm ifs mode")  # command is ifs
  #         if (L_isIFShift != isIFShift)
  # {
  #   L_isIFShift = isIFShift;
  #   SendCommand1Num(CMD_IS_IFSHIFT, L_isIFShift);

    def cxGet(self, buffer):
        print("unknown cx called to confirm stop mode")  # command is stop


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

    def Radio_Toggle_ATT(self):
        print("ATT toggle")
        command = [self.toRadioCommandDict["TS_CMD_ATT"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_IFS(self):
        print("IFS toggle")
        command = [self.toRadioCommandDict["TS_CMD_IFS"],0,0,0,0]
        self.theRadio.sendCommandToMCU(bytes(command))
      #   first value has something
      #         {
      #   isIFShift = isIFShift ? 0 : 1;  //Toggle
      # }


    #
    #   The "cc" command indicates a change to a new mode (e.g. USB, LSB, etc.)
    #

    def cc_UX_Set_Mode(self, buffer):
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

    def vaGet(self, buffer):
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

    def caGet(self, buffer):
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

    def vbGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.secondary_VFO_VAR.set(value)
        if self.debugCommandDecoding:
            print("vb get called:", "buffer =", buffer)
            print("vb assign vfo b frequency")
            print("value=", value, sep='*', end='*')
            print("\n")



    def cbGet(self, buffer):
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

    def cnGet(self, buffer):

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

    def vtGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.debugCommandDecoding:
            print("vt get called:", "buffer =", buffer)
            print("vt tone for CW")
            print("value=", value, sep='*', end='*')
            print("\n")


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

    #
    #   Returns active VFO, VFO-A=0, VFO-B=1
    def cvGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if (int(value) == 0):
            self.vfo_VAR.set("VFO-A")
        else:
            self.vfo_VAR.set("VFO-B")

        if self.debugCommandDecoding:
            print("cv get called:", "buffer =", buffer)
            print("cv toggle vfo")
            print("value=", value, sep='*', end='*')
            print("\n")

