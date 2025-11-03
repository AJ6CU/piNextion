# from imghdr import test_xbm
import tkinter.ttk as ttk
import tkinter as tk

# from Cython.Compiler.Naming import self_cname

import piCEC_UXui as baseui
from settings import settings
from cwSettings import cwSettings

from channels import channels
from Classic_uBITX_Control import Classic_uBITX_Control

import mystyles  # Styles definition module
from time import sleep


class piCECNextion(baseui.piCECNextionUI):
    def __init__(self, master=None, **kw):
        super().__init__(
            master,
            translator=None,
            on_first_object_cb=mystyles.setup_ttk_styles,
        )
        self.configData = None    # Saves the configuration data object address
        self.theRadio = None            # Object pointer for the Radio
        self.cwSettingsWindow = None    # Object pointer for the CW Settinge Window
        self.settingsWindow = None      # Object pointer for the General Settings Window
        self.channelWindow = None      # object pointer for the Memory-> VFO Window
        self.vfoToMemWindow = None      # object pointer for the VFO->Memory Window
        self.classic_uBITX_ControlWindow = None
        self.classic_uBITX_ControlWindowObj = None
        self.DeepDebug = False
        self.CurrentDebug = True

        self.rate_selection = {
            0: self.tuning_Preset_Button,
            1: self.digit1_Highlight_Label,
            2: self.digit2_Highlight_Label,
            3: self.digit3_Highlight_Label,
            4: self.digit4_Highlight_Label,
            5: self.digit5_Highlight_Label,
            6: self.digit6_Highlight_Label,
            7: self.digit7_Highlight_Label
        }

        self.DigitPos_to_Powers_of_Ten = {
            0: 0,
            1: 10,
            2: 100,
            3: 1000,
            4: 10000,
            5: 100000,
            6: 1000000,
            7: 10000000
        }

        self.currentDigitPos = 0
        self.currentVFO_Tuning_Rate = 0


        self.VFO_A = "VFO-A"                        # String used for label of VFO-A
        self.VFO_B = "VFO-B"                        # String used for label of VFO-B
        self.vfo_VAR.set(self.VFO_A)                #Specifies which VFO is active. Also
                                                    #Label on VFO toggle button

        self.lock_Button_On = False                 #controls lock of console
        self.speaker_Button_On = False              #On means in Mute/SDR
        self.stop_Button_On = False                 #Emergency stop all tx
        self.split_Button_On = False                #Controls entry into split mode
        self.rit_Button_On = False                  #Controls RIT. On means in RIT mode
        self.ATT_Button_On = False                  #On allows onscreen control of signal attn
        self.IFS_Button_On = False                  #On allows onscreen mod of the ifs

        self.last_VFODial_Reading = None

        self.tuning_Preset_Selection_Frame.grid_remove()
        self.tuning_Jogwheel.configure(scroll=True)
        self.baselineJogValue = 0
        self.saved_tuning_Preset_Selection = None       # This is a tristate variable.
                                                        # If None, this means we are in
                                                        # Preset mode.
                                                        # When NOT None, this savesthe
                                                        # Preset selection value from the
                                                        # set of radiobuttons for the presets
        self.saved_tuning_Preset_VAR = None
        self.update_Tuning_Preset_Button_Label = True

        # self.channelSelection = None                    # assigned to channel number when selected in channels

#   Constants
        #######################################################################################
        #   Dictionaries that follow are used to lookup textual values based on internal
        #   Representations. Sometimes it is a string integer. Other times it is a string of
        #   a couple characters. These translations are collected here to avoid them being
        #   "codified" directly in the functions that use them.
        #######################################################################################

        self.MCU_Command_To_CB_Dict = {
            "v1": self.v1_UX_Set_Tuning_Preset_1,
            "v2": self.v2_UX_Set_Tuning_Preset_2,
            "v3": self.v3_UX_Set_Tuning_Preset_3,
            "v4": self.v4_UX_Set_Tuning_Preset_4,
            "v5": self.v5_UX_Set_Tuning_Preset_5,
            "cn": self.cn_UX_Set_Active_Tuning_Preset,
            "ch": self.chGet,
            "vh": self.vhGet,
            "vo": self.voGet,
            "vp": self.vpGet,
            "vq": self.vqGet,
            "sv": self.sv_UX_Set_SW_Version,
            "sc": self.sc_UX_Set_User_Callsign,
            "cm": self.cm_UX_Display_Callsign_Version_Flag,
            "c0": self.c0_UX_Toggle_Classic_uBITX_Control,
            "vc": self.vc_UX_Set_Primary_VFO_Frequency,
            "cc": self.cc_UX_Set_Primary_Mode,
            "va": self.va_UX_Set_VFO_A_Frequency,
            "ca": self.ca_UX_Set_VFO_A_Mode,
            "vb": self.vb_UX_Set_VFO_B_Frequency,
            "cb": self.cb_UX_Set_VFO_B_Mode,
            "vt": self.vt_UX_SET_CW_Tone,
            "ck": self.ck_UX_Set_CW_Key_Type,
            "vs": self.vs_UX_Set_CW_Speed,
            "vy": self.vy_UX_Set_CW_Delay_Returning_to_RX,
            "ve": self.ve_UX_Set_CW_Delay_Starting_TX,
            "cv": self.cv_UX_VFO_Toggle,            #sets active VFO, A=0, B=1
            "s0": self.s0_UX_Greenbox_Line1,
            "s1": self.s1_UX_Greenbox_Line2,
            "sh": self.sh_UX_Get_Memory,
            "vn": self.vn_UX_ACK_Memory_Write,
            "cl": self.cl_UX_Lock_Screen,
            "cj": self.cj_UX_Speaker_Toggle,
            "cs": self.cs_UX_SPLIT_Toggle,
            "vr": self.vr_UX_Update_RIT_Freq,
            "cr": self.cr_UX_RIT_Toggle,
            "vf": self.vf_UX_ATT_Level,
            "vi": self.vi_UX_IFS_Level,
            "ci": self.ci_UX_IFS_State_Set,
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
            "0":"DFT",
            "2":"LSB",
            "3":"USB",
            "4":"CWL",
            "5":"CWU"
        }

        self.Text_To_ModeNum = {
            "DFT":0,
            "LSB":2,
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

        self.CW_KeyType = {         # 0: straight, 1 : iambica, 2: iambicb
            "0":"STRAIGHT",
            "1":"IAMBICA",
            "2":"IAMBICB"
        }

        self.CW_KeyValue = {
            "STRAIGHT": 0x0,
            "IAMBICA": 0x01,
            "IAMBICB": 0x02
        }
        self.lsb = 0                    # index of least significant eeprom mem address in list below
        self.msb = 1                    # index of most significant eeprom emem address in list below
        self.memLength = 2
        self.charFlag = 3
        self.memOffset = 4
        self.totalSlots = 5
        self.EEPROM_Mem_Address = {
            "cw_key_type": [ 0x66, 0x01, 0x01, 0x0, 0x0, 0x1],
            "cw_wpm": [ 0x1c, 0x0, 0x04, 0x0, 0x0, 0x1],
            "cw_sidetone": [ 0x18, 0x0, 0x04, 0x0, 0x0, 0x1],
            "cw_Delay_Returning_to_RX": [0x02, 0x1, 0x01, 0x0, 0x0, 0x1],  # eeprom value divided by 10
            "cw_Delay_Starting_TX": [0x03, 0x1, 0x1, 0x0, 0x0,  0x1],  # eeprom saved valued divided by 2
            "channel_freq_Mode": [0x76, 0x2, 0x4, 0x48, 0x4, 0x14], # 0x48 indicates a integer number
            "channel_Label": [0xc7, 0x2, 0x5, 0x57, 0x6, 0x9],  # should be 0xa for total, but bug with v2 cec
                                                                # 0x57 indicates it is a character
            "channel_ShowLabel": [0xc6, 0x2, 0x1, 0x57, 0x6,  0x9] # should be 0xa for total, but bug with v2 cec
                                                                # 0x57 indicates it is a character
        }

        self.memReadingState = "Freq"

        #
        #   These three variables are used to track which memory location (or "slot")
        #   that the retreived memory is from. This is needed because the MCU does not
        #   send any info on which memory location is associated with the value sent back
        #   to the Nextion. It assumes (hopefully corrcctly) that they appear in order.
        #
        self.EEPROM_Current_Slot_Freq = 0
        self.EEPROM_Current_Slot_Label = 0
        self.EEPROM_Current_Slot_ShowLabel = 0


        self.ATT_Status_Off = 0         #indicates that ATT has been turned off

    #####################################################################################
    #       End of dictionaries of constants
    #####################################################################################

    def attachRadio(self, radio):
        self.theRadio = radio

    def attachConfig(self, config):
        self.configData = config

    def initUX(self):
        self.updateRateMultiplier()
        self.updateLabelTuning_Multiplier()
        self.toggle_Digit_Highlight(self.rate_selection[self.currentDigitPos], True)

    ######################################################################################
    #   This looks up the command processing routing to be called via a dictionary
    #   based on the command type (characters 3,4 in the buffer after prelogue stripped
    ######################################################################################

    def delegate_command_processing(self,command, buffer):
        try:
            self.MCU_Command_To_CB_Dict[command](buffer)
        except:
            print("Command not recognized=", buffer,"*")

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
#   Callbacks
#####################################################################################
### Start Callbacks
#   These are the callbacks as defined in the GUI Builder pygubu-designer
#####################################################################################

    def settings_CB(self):
        self.settingsWindow = settings (self.master)
        self.settingsWindow.geometry("300x200")

    def getCurrentCWSettings(self):
        self.cwSettingsWindow.tone_value_VAR.set(self.tone_value_VAR.get())
        self.cwSettingsWindow.key_type_value_VAR.set(self.key_type_value_VAR.get())
        self.cwSettingsWindow.key_speed_value_VAR.set(self.key_speed_value_VAR.get())
        self.cwSettingsWindow.delay_starting_tx_value_VAR.set(self.delay_starting_tx_value_VAR.get())
        self.cwSettingsWindow.delay_returning_to_rx_value_VAR.set(self.delay_returning_to_rx_value_VAR.get())

    def displayCWSettingsWindow(self):
        self.cwSettingsWindow = cwSettings (self.master, self)
        self.getCurrentCWSettings()
        self.cwSettingsWindow.grab_set()  # This line makes the cw settings window modal
        self.cwSettingsWindow.transient(self.master)  # Makes the cw settings appear above the mainwindow
        self.master.wait_window(self.cwSettingsWindow)  # This pauses the main window until the cwsetting is closed

    def dirty_DisplayCWSettings (self):
        if( self.cwSettingsWindow.tone_value_VAR.get() != self.tone_value_VAR.get()):
            self.Radio_Set_CW_Tone(self.cwSettingsWindow.tone_value_VAR.get())

        if (self.cwSettingsWindow.key_type_value_VAR.get() != self.key_type_value_VAR.get()):
            self.Radio_Set_CW_Key_Type(self.cwSettingsWindow.key_type_value_VAR.get())

        if (self.cwSettingsWindow.key_speed_value_VAR.get() != self.key_speed_value_VAR.get()):
            # self.key_speed_value_VAR.set(self.cwSettingsWindow.key_speed_value_VAR.get())
            self.Radio_Set_CW_Key_Speed(self.cwSettingsWindow.key_speed_value_VAR.get())

        if (self.cwSettingsWindow.delay_starting_tx_value_VAR.get() != self.delay_starting_tx_value_VAR.get()):
            # self.delay_starting_tx_value_VAR.set(self.cwSettingsWindow.delay_starting_tx_value_VAR.get())
            self.Radio_Set_CW_Delay_Starting_TX(self.cwSettingsWindow.delay_starting_tx_value_VAR.get())

        if (self.cwSettingsWindow.delay_returning_to_rx_value_VAR.get() != self.delay_returning_to_rx_value_VAR.get()):
            # self.delay_returning_to_rx_value_VAR.set(self.cwSettingsWindow.delay_returning_to_rx_value_VAR.get())
            self.Radio_Set_CW_Delay_Returning_To_RX(self.cwSettingsWindow.delay_returning_to_rx_value_VAR.get())

    #
    #   This routine makes requests from the MCU for all the Channel Frequencies, Mode, and Labels
    #   The actual setting of the corresponding values awaits the response of the eeprom
    #   packages sent by the MCU via the "sh_UX_Get_Memory" function
    #
    def displayChannelWindow(self):
        if self.channelWindow == None:
            self.channelWindow = channels(self.master, self, self.refresh_CB, self.configData)
            self.channelWindow.transient(self.master)
            self.channelWindow.update_Current_Frequency (self.primary_VFO_VAR.get())
            self.channelWindow.update_Current_Mode (self.primary_Mode_VAR.get())
            self.Radio_Req_Channel_Freqs()
            self.Radio_Req_Channel_Labels()
            self.Radio_Req_Channel_Show_Labels()
        else:
            self.channelWindow.deiconify()
            self.channelWindow.current_Channel_VAR.set("Not Saved")

    def displayClassic_uBITXControlWindow(self):
        self.classic_uBITX_ControlWindow  = tk.Toplevel(self.master)
        self.classic_uBITX_ControlWindowObj=Classic_uBITX_Control(self.classic_uBITX_ControlWindow)
        self.classic_uBITX_ControlWindowObj.pack()

        toplevel_offsetx, toplevel_offsety = self.master.winfo_x(), self.master.winfo_y()
        padx = 350  # the padding you need.
        pady = 250
        self.classic_uBITX_ControlWindow.geometry(f"+{toplevel_offsetx + padx}+{toplevel_offsety + pady}")

        self.classic_uBITX_ControlWindow.grab_set()
        self.classic_uBITX_ControlWindow.transient(self.master)  # Makes the cw settings appear above the mainwindow

    def displayLine1Classic_uBITX_Control(self, value):
        self.classic_uBITX_ControlWindowObj.greenBoxSelection_VAR.set(value)

    def displayLine2Classic_uBITX_Control(self, value):
        self.classic_uBITX_ControlWindowObj.greenBoxInstructions_VAR.set(value)
    #
    def refresh_CB(self):
        self.channelWindow.destroy()
        self.channelWindow = None
        self.displayChannelWindow()

    def Radio_Req_Channel_Freqs(self):

        base = self.EEPROM_Mem_Address["channel_freq_Mode"][self.lsb]
        for i in range(self.EEPROM_Mem_Address["channel_freq_Mode"][self.totalSlots]):
            command = [self.toRadioCommandDict["TS_CMD_READMEM"],
                       base,
                       self.EEPROM_Mem_Address["channel_freq_Mode"][self.msb],
                       self.EEPROM_Mem_Address["channel_freq_Mode"][self.memLength],
                       self.EEPROM_Mem_Address["channel_freq_Mode"][self.charFlag]
                       ]
            # print("command=", command)
            self.theRadio.sendCommandToMCU(bytes(command))
            base += self.EEPROM_Mem_Address["channel_freq_Mode"][self.memOffset]

        base = self.EEPROM_Mem_Address["channel_freq_Mode"][self.lsb]

    def Radio_Req_Channel_Labels(self):
        base = self.EEPROM_Mem_Address["channel_Label"][self.lsb]
        for i in range(self.EEPROM_Mem_Address["channel_Label"][self.totalSlots]):
            command = [self.toRadioCommandDict["TS_CMD_READMEM"],
                       base,
                       self.EEPROM_Mem_Address["channel_Label"][self.msb],
                       self.EEPROM_Mem_Address["channel_Label"][self.memLength],
                       self.EEPROM_Mem_Address["channel_Label"][self.charFlag]
                       ]
            self.theRadio.sendCommandToMCU(bytes(command))
            base += self.EEPROM_Mem_Address["channel_Label"][self.memOffset]

        base = self.EEPROM_Mem_Address["channel_Label"][self.lsb]

    def Radio_Req_Channel_Show_Labels(self):
        base = self.EEPROM_Mem_Address["channel_ShowLabel"][self.lsb]
        for i in range(self.EEPROM_Mem_Address["channel_ShowLabel"][self.totalSlots]):
            command = [self.toRadioCommandDict["TS_CMD_READMEM"],
                       base,
                       self.EEPROM_Mem_Address["channel_ShowLabel"][self.msb],
                       self.EEPROM_Mem_Address["channel_ShowLabel"][self.memLength],
                       self.EEPROM_Mem_Address["channel_ShowLabel"][self.charFlag]
                       ]
            self.theRadio.sendCommandToMCU(bytes(command))
            base += self.EEPROM_Mem_Address["channel_ShowLabel"][self.memOffset]

        base = self.EEPROM_Mem_Address["channel_ShowLabel"][self.lsb]



    def vfo_CB(self):
        self.Radio_Toggle_VFO()

    def mode_lsb_CB(self):
        self.Radio_Set_Mode(self.Text_To_ModeNum["LSB"])

    def mode_usb_CB(self):
        self.Radio_Set_Mode(self.Text_To_ModeNum["USB"])


    def mode_cwl_CB(self):
        self.Radio_Set_Mode(self.Text_To_ModeNum["CWL"])


    def mode_cwu_CB(self):
        self.Radio_Set_Mode(self.Text_To_ModeNum["CWU"])

    def band_up_CB(self):
         self.Radio_Change_Band(self.Text_To_BandChange["UP"])

    def band_down_CB(self):
         self.Radio_Change_Band(self.Text_To_BandChange["DOWN"])

    def cwSettings_CB(self, event=None):
       if (not self.lock_Button_On):
           self.displayCWSettingsWindow()

    def tuning_Preset_5_CB(self):
        self.Radio_Set_Tuning_Preset(5)
        self.tuning_Preset_Selection_Frame.grid_remove()

    def tuning_Preset_4_CB(self):
        self.Radio_Set_Tuning_Preset(4)
        self.tuning_Preset_Selection_Frame.grid_remove()

    def tuning_Preset_3_CB(self):
        self.Radio_Set_Tuning_Preset(3)
        self.tuning_Preset_Selection_Frame.grid_remove()

    def tuning_Preset_2_CB(self):
        self.Radio_Set_Tuning_Preset(2)
        self.tuning_Preset_Selection_Frame.grid_remove()

    def tuning_Preset_1_CB(self):
        self.Radio_Set_Tuning_Preset(1)
        self.tuning_Preset_Selection_Frame.grid_remove()


    def tuning_Preset_Select_CB(self):
        #
        #   check if frame containing radiobuttons is displayed
        #   if not, display it. If currently displayed, remove it
        #
        if (self.tuning_Preset_Selection_Frame.winfo_ismapped()):
            self.tuning_Preset_Selection_Frame.grid_remove()
        else:
            self.tuning_Preset_Selection_Frame.grid()

    def tuning_Jogwheel_CB(self):
        # if self.DeepDebug:
        #     print("tuning_Jogwheel_CB called")
        #     print("self.currentVFO_Tuning_Rate=", self.currentVFO_Tuning_Rate)
        #     print("self.tuning_Jogwheel.get()=",self.tuning_Jogwheel.get())
        #     print("self.baselineJogValue=", self.baselineJogValue)
        #     print("self.primary_VFO_VAR.get()", self.primary_VFO_VAR.get())
        #
        #   Get current Frequency and adjust back to baseline
        #
        newFreq =  int(self.primary_VFO_VAR.get()) - (self.currentVFO_Tuning_Rate * self.baselineJogValue)
        newFreq += self.currentVFO_Tuning_Rate * self.tuning_Jogwheel.get()
        # if self.DeepDebug:
        #     print("new freq from jog = ", newFreq)
        self.Radio_Set_New_Frequency(newFreq)


    def find_msd_position(self, number_string):
        # Finds the index of the most significant digit from the right in a string representation of a number.

        # Returns:
        #     int or None: The index of the most significant digit, or None if no non-zero digit is found.

        reversed_number_string = number_string[::-1].strip()  # neat trick to reverse a string

        for i, char in enumerate(reversed_number_string):
            if char.isdigit() and char != '0':
                return i
        return None

    #
    #   this function returns a single digit integer that occupies the position
    #   corresponding to the current selected rate.
    #   Conveniently, presets are allocated to position 0,
    #   which is always zero in CEC and not setable
    #

    def getVFOdigit(self):
        #
        #   get the VFO currently displayed
        #
        currentVFO = self.primary_VFO_VAR.get()

        #
        #   reverse it so that least significant is in position 0
        #
        reversedVFO = currentVFO[::-1].strip()      # neat trick to reverse a string

        #
        #   pad it on right with zeros so we have 8 characters
        #
        reversedVFO = reversedVFO.ljust(8,"0")

        if (self.currentDigitPos == 0):
            if (self.currentVFO_Tuning_Rate != 0):
                pos=self.find_msd_position(str(self.currentVFO_Tuning_Rate))
                return int(reversedVFO[pos])
            else:
                return int(reversedVFO[2])
        else:
            #
            #   now we can just return the character of the selected rate
            #
            return int(reversedVFO[self.currentDigitPos])
    #
    #   This routine handles switching between Direct and "Preset" tuning mode
    #   The complexity here comes from the original CEC software using the current
    #   preset-1 (i.e. if Preset 3 was 100 and Preset 2 was 50, and we were on preset 3,
    #   everything below Preset 3 would be zero'ed out. This means to allow direct
    #   tune mode on the tens digit, we must first make the preset the lowest # (i.e. 1)
    #   so that the tens digit is not masked out and turned to zero.
    #   As a result, we need to save the state of the preset when we move to Direct Tune,
    #   and then restore it as we exit Direct Tune and go into Preset mode.
    #   Since the MCU can also force changes in preset, we must temporarily turn off
    #   the updating of the label
    #
    def toggle_Tuning_Mode(self, mode):
        if (mode == "direct tune"):
            if (self.saved_tuning_Preset_Selection == None):        #None value indicates we *were* in "direct tune" mode
                #
                #   save state prior to going into Direct Mode
                #
                self.saved_tuning_Preset_Selection = self.tuning_Preset_Selection_VAR.get()
                self.saved_tuning_Preset_VAR = self.tuning_Preset_Label_VAR.get()
                #
                #   Sets label that displays current present with "Direct Tune" string
                #
                self.tuning_Preset_Label_VAR.set("Direct Tune")
                #   turn off any changes in the label due to a change in preset coming from the radio
                self.update_Tuning_Preset_Button_Label = False
                #   Disable the tuning rate button so selected preset cannot be changed while in direct tune
                self.tuning_Preset_Button.configure(state='disabled')
                #
                #   Select the lowest tuning rate of the presets. The need to do this is the result of the original
                #   CEC software using the rate preselects to truncate digits below the preset. For example.
                #   if a preset of 100 was selected, then it would be impossible to set the dial in increments of 20
                #   or 10 because it would be truncated to lower 100.
                #
                self.Radio_Set_Tuning_Preset(1)

        else:       # Switching into pre-set tuning mode and have to restore the state
            if (self.saved_tuning_Preset_Selection != None):          # dont restore unless it was previously saved
                #   Allow updating of the Label for the selected preset
                self.update_Tuning_Preset_Button_Label = True
                #   Restore the saved states
                self.tuning_Preset_Label_VAR.set(self.saved_tuning_Preset_VAR)
                self.Radio_Set_Tuning_Preset(int(self.saved_tuning_Preset_Selection))
                #   Re-enable the button to select a preset
                self.tuning_Preset_Button.configure(state='enabled')
                #   indicate the saved states are now invalid
                self.saved_tuning_Preset_Selection = None


    def toggle_Digit_Highlight(self, light, Status):

        if (Status):
            if (isinstance(light, ttk.Button)):
                light.configure(style='GreenButton2b.TButton')
                self.toggle_Tuning_Mode("preset tune")      # go into preset tune mode

            else:
                light.configure(style='OnLED.TLabel')
                self.toggle_Tuning_Mode("direct tune")      # go into direct tune mode

        else:
            if (isinstance(light, ttk.Button)):
                light.configure(style='Button2b.TButton')
            else:
                light.configure(style='OffLED.TLabel')


    #
    #   When the tuning_Multiplier is clicked, it cycles through the digits in the VFO to allow them to be
    #   manually tuned. The initial case the use of the preset tuning cycles is used, much in the same
    #   way it would be if you are adjusting the physical tuning knob.
    #
    def tuning_Multiplier_Button_CB(self):
        #
        #   First turn off the old LED, turn on new LED indicator for tuning
        #
        self.updateLEDTuningHighlight()
        #
        #   Update rate multiplier for jogwheel
        #
        self.updateRateMultiplier()
        #
        #   set tracking variables for new rate change
        #
        self.updateJogTracking()
        #
        #   Update the label on the tuning button selector
        #
        self.updateLabelTuning_Multiplier()


    def updateLEDTuningHighlight(self):
        #
        #   First turn off the old LED
        #
        self.toggle_Digit_Highlight(self.rate_selection[self.currentDigitPos], False)
        #
        #   Increment to the next slot and turn its LED on, check for rollover
        #
        self.currentDigitPos += 1
        if self.currentDigitPos > len(self.rate_selection)-1:
            self.currentDigitPos = 0
        self.toggle_Digit_Highlight(self.rate_selection[self.currentDigitPos], True)

    def updateRateMultiplier(self):
        #
        #   Set the frequency multiplier
        #
        self.currentVFO_Tuning_Rate = self.DigitPos_to_Powers_of_Ten[self.currentDigitPos]
        #
        #   Special case 0, which is the current value of the preset
        #
        if (self.currentVFO_Tuning_Rate == 0):
           if self.tuning_Preset_Label_VAR.get() == "Direct Tune":
               self.Radio_Set_Tuning_Preset(1)
           else:
               self.currentVFO_Tuning_Rate = int(self.tuning_Preset_Label_VAR.get())

    def updateJogTracking(self,newBaseline=True):
        # if self.DeepDebug:
        #     print("updating jogwheel, digit=", self.getVFOdigit())
        #     print("current jogwheel position =", self.tuning_Jogwheel.get())

        self.tuning_Jogwheel.setSpecial(self.getVFOdigit())
        if(newBaseline):
            self.baselineJogValue = self.tuning_Jogwheel.get()

    def updateLabelTuning_Multiplier(self):
        if (self.currentVFO_Tuning_Rate < 1000):
            multiplier_string = str(int(self.currentVFO_Tuning_Rate)) + "Hz"
        elif (self.currentVFO_Tuning_Rate < 1000000):
            multiplier_string = str(int(self.currentVFO_Tuning_Rate / 1000)) + "KHz"
        else:
            multiplier_string = str(int(self.currentVFO_Tuning_Rate / 1000000)) + "MHz"

        #   Now set the text on the multiplier button to reflect the new rate
        #
        self.tuning_Multiplier_VAR.set("Tuning Factor\nx" + multiplier_string)

#
#   This function sends to the Radio a notice that a screen lock has been requested
#   The actual locking of the screen waits until the Radio sends back a commond
#   to lock the screen. This ensures that the screen is not locked by the UX
#   and the Radio never gets the request for some reason.
#   The actual locking of screen is set performed by cl_UX_Lock_Screen()
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



    def channels_CB(self):
        self.displayChannelWindow()
    #
    #   The following routines handles the ATT jogwheel.
    #   Basically any click with no movement will toggle
    #   the ATT on or off. When turned on it remembers the last value
    #   (or 70 if this is the first time)
    #   The two "ButtonPressed_CB" and "ButtonReleased" are used to
    #   capture the initial value when first clicked and then when
    #   the jogwheel is released, a check is made on whether there was
    #   a change in value.
    #   The routines in this area just send a command to the Radio via the
    #   self.Radio_Set_ATT (value) routine. Zero turns it off, any other value turns it on.
    #   Note that although the UX is updated as the jogwheel is moved, the real value is set
    #   self.vf_UX_ATT_Level routine which is kicked off when the Radio(MCU) sends a "vf"
    #   command to the screen
    #
    def ATT_Jogwheel_ButtonPressed_CB(self, event=None):
        if(self.lock_Button_On == False):                           # Have to check explictly for lock button because of
                                                                    # Release callbacks
            self.ATT_Jogwheel.lastValue = self.ATT_Jogwheel.get()

    def ATT_Jogwheel_ButtonReleased_CB(self, event=None):
        if(self.lock_Button_On == False):
            currentValue = self.ATT_Jogwheel.get()
            if (self.ATT_Jogwheel.lastValue == currentValue) :
                self.toggleATT_State()
            else:
                self.Radio_Set_ATT(currentValue)

    #
    #   toggle ATT state to on if it was off, off it it was on
    #
    def toggleATT_State(self):
        if self.ATT_Jogwheel.state == "disabled":
            self.Radio_Set_ATT(self.ATT_Jogwheel.lastValue)     # Signal radio ATT on and last value
        else:
            self.Radio_Set_ATT(self.ATT_Status_Off)             # Signal radio ATT turning off

    #
    #   Send Radio/MCU the updated value for the  ATT. Although the UX reflects the new
    #   value up front, it gets re-set when the radio/mcu sends the "real" value via the "vf"
    #   command.  This means that the wheel might do a little forward/back dance depending
    #   on the speed of the MCU
    #
    def updateATTValue_CB(self):

        self.Radio_Set_ATT(self.ATT_Jogwheel.get())


    #
    #   The following handles the IFS Jogwheel. This is basically the same pattern
    #   as the ATT jogwheel above, except IFS hastwo functions (on/off and
    #   value set) where the ATT command only has one value with a "Zero" indicating ON/OFF.
    #

    def IFS_Jogwheel_ButtonPressed_CB(self, event=None):
        if (self.lock_Button_On == False):
            self.IFS_Jogwheel.lastValue = self.IFS_Jogwheel.get()

    def IFS_Jogwheel_ButtonReleased_CB(self, event=None):
        if (self.lock_Button_On == False):
            currentValue = self.IFS_Jogwheel.get()
            if self.IFS_Jogwheel.lastValue == currentValue:
                self.toggleIFS_State()
            else:
                self.Radio_Set_IFS_Level(currentValue)


    def toggleIFS_State(self):
        self.Radio_Toggle_IFS()

    def updateIFSValue_CB(self):
        self.Radio_Set_IFS_Level(self.IFS_Jogwheel.get())




########################################################################################
#   End of Callbacks executed by the UX
########################################################################################

#   Radio Commands
########################################################################################
#   These routines are called to tell the MCU that an action has happened in the UX.
#   Typically these should be used by the UX Callbacks
########################################################################################
    def Radio_Freq_Encode(self, freq):
        encodedBytes = bytearray()
        intFreq = int(freq)
        encodedBytes.append(intFreq & 0xff)

        intFreq = (intFreq >> 8)
        encodedBytes.append(intFreq & 0xff)

        intFreq = (intFreq >> 8)
        encodedBytes.append(intFreq & 0xff)

        intFreq = (intFreq >> 8)
        encodedBytes.append(intFreq & 0xff)

        return encodedBytes
    #
    #   This convert a 16 bit number (either string or int) to an array of 2 bytes
    #
    # def convert16BitToBytes(self, int16):
    #     encodedBytes = bytearray()
    #     number16 = int(int16)    # convert any strings to integer
    #     encodedBytes.append(number16 & 0xff)
    #
    #     number16 = (number16 >> 8)
    #     encodedBytes.append(number16 & 0xff)
    #
    #     return encodedBytes

    #
    #   This function tells the Radio that a new mode has been selected for
    #   the primary (displayed) VFO. After receiving the new mode, the
    #   Radio will separately send back the mode to the UX
    #
    def Radio_Set_Tuning_Preset(self, rate: bytes):
        command = [self.toRadioCommandDict["TS_CMD_TUNESTEP"], rate, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Set_New_Frequency(self, value):
        fourBytes = self.Radio_Freq_Encode(value)
        command = [self.toRadioCommandDict["TS_CMD_FREQ"],fourBytes[0],fourBytes[1],fourBytes[2],fourBytes[3]]
        self.theRadio.sendCommandToMCU(bytes(command))

    #
    #   This function tells the Radio that a new mode has been selected for
    #   the primary (displayed) VFO. After receiving the new mode, the
    #   Radio will separately send back the mode to the UX
    #
    def Radio_Set_Mode(self, newMode):
        command = [self.toRadioCommandDict["TS_CMD_MODE"], newMode, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    #
    #   This function tells the Radio that a button up or down has been pushed
    #   in the UX. After receiving this command the radio will send back a new frequency
    #   and mode for the displayed VOF
    #
    def Radio_Change_Band(self, direction):
        command = [self.toRadioCommandDict["TS_CMD_BAND"], direction, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Tuning_Rate(self,value: bytes):
        command = [self.toRadioCommandDict["TS_CMD_TUNESTEP"], value, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_VFO(self):
        command = [self.toRadioCommandDict["TS_CMD_VFO"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Lock(self):
        command = [self.toRadioCommandDict["TS_CMD_LOCK"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Speaker(self):
        command = [self.toRadioCommandDict["TS_CMD_SDR"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Stop(self):
        command = [self.toRadioCommandDict["TS_CMD_TXSTOP"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_Split(self):
        command = [self.toRadioCommandDict["TS_CMD_SPLIT"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_RIT(self):
        command = [self.toRadioCommandDict["TS_CMD_RIT"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Set_ATT(self, value: bytes):
        command = [self.toRadioCommandDict["TS_CMD_ATT"], value, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Toggle_IFS(self):
        command = [self.toRadioCommandDict["TS_CMD_IFS"], 0, 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))



    def Radio_Set_IFS_Level(self, level):
        encodedBytes = self.Radio_Freq_Encode(str(level))

        command = [self.toRadioCommandDict["TS_CMD_IFSVALUE"], encodedBytes[0], encodedBytes[1], encodedBytes[2], 0]
        self.theRadio.sendCommandToMCU(bytes(command))


    def Radio_Set_CW_Tone(self, tone):
        # command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"], 0, 0, 0, 0, 0, 0, 0, 0]
        # self.theRadio.sendCommandToMCU(bytes(command))
        pass

    def Radio_Set_CW_Key_Type(self, keyType):
        #
        #   first send command to officially change the keytype
        #
        command = [self.toRadioCommandDict["TS_CMD_KEYTYPE"], self.CW_KeyValue[keyType], 0, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))
        #
        #   Now have to write it to EEPROM as this is not one of the values that are automatically saved to EEPROM
        #

        checksum = (self.EEPROM_Mem_Address["cw_key_type"][self.lsb] + self.EEPROM_Mem_Address["cw_key_type"][self.msb]
                    + self.EEPROM_Mem_Address["cw_key_type"][self.memLength]) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   self.EEPROM_Mem_Address["cw_key_type"][self.lsb],
                   self.EEPROM_Mem_Address["cw_key_type"][self.msb],
                   self.EEPROM_Mem_Address["cw_key_type"][self.memLength],
                   checksum,
                   self.CW_KeyValue[keyType]
                   ]
        self.theRadio.sendCommandToMCU(bytes(command))




    def Radio_Set_CW_Key_Speed(self, keySpeed):

        #
        #
        #   first send command to officially change the key speed
        #   wpm directly saved. It is the dot length which is 1200/wpm
        #

        dotLength_ms = int(1200 / int(keySpeed))
        command = [self.toRadioCommandDict["TS_CMD_WPM"], dotLength_ms, 0, 0]
        self.theRadio.sendCommandToMCU(bytes(command))

        #
        #   Now have to write it to EEPROM as this is not one of the values that are automatically saved to EEPROM
        #

        checksum = (self.EEPROM_Mem_Address["cw_wpm"][self.lsb] + self.EEPROM_Mem_Address["cw_wpm"][self.msb]
                    + self.EEPROM_Mem_Address["cw_wpm"][self.memLength]) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   self.EEPROM_Mem_Address["cw_wpm"][self.lsb],
                   self.EEPROM_Mem_Address["cw_wpm"][self.msb],
                   self.EEPROM_Mem_Address["cw_wpm"][self.memLength],
                   checksum,
                   dotLength_ms,                # Eeprom allows up to two bytes for adjusted key,
                                                    # but keychage without reboot only 1 byte
                   0,0,0
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))


    def Radio_Set_CW_Delay_Starting_TX(self, startTXDelay):
        #
        #   Requires reboot to take effect
        #
        #
        # adjust the wpm speed to format of EEPROM
        #
        adjustedStartTXDelay = int(int(startTXDelay)/2)

        #
        #   write it to EEPROM as will be picked up on next reboot
        #

        checksum = (self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.lsb] + self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.msb]
                    + self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.memLength]) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.lsb],
                   self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.msb],
                   self.EEPROM_Mem_Address["cw_Delay_Starting_TX"][self.memLength],
                   checksum,
                   adjustedStartTXDelay
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Set_CW_Delay_Returning_To_RX(self, returnRXDelay):
        # value stored to eeprom needs to divided by 10
        #
        #   Requires reboot to take effect
        #
        #
        # adjust the wpm speed to format of EEPROM
        #
        adjustedReturnToRXDelay = int(int(returnRXDelay) / 10)

        #
        #   write it to EEPROM as will be picked up on next reboot
        #

        checksum = (self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.lsb] +
                    self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.msb]
                    + self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.memLength]) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.lsb],
                   self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.msb],
                   self.EEPROM_Mem_Address["cw_Delay_Returning_to_RX"][self.memLength],
                   checksum,
                   adjustedReturnToRXDelay
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Write_EEPROM_Channel_FreqMode (self, channelNum, freq, mode ):

        encoded_data = (int(freq) & 0x1FFFFFFF) + ((int(self.Text_To_ModeNum[mode])& 0x7)<<29)

        encodedBytes = self.Radio_Freq_Encode(str(encoded_data))

        lsb = (channelNum*self.EEPROM_Mem_Address["channel_freq_Mode"][self.memOffset]) + self.EEPROM_Mem_Address["channel_freq_Mode"][self.lsb]
        msb = self.EEPROM_Mem_Address["channel_freq_Mode"][self.msb]
        totalBytes = self.EEPROM_Mem_Address["channel_freq_Mode"][self.memLength]


        checksum = (lsb + msb + totalBytes) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   lsb,
                   msb,
                   totalBytes,
                   checksum,
                   encodedBytes[0], encodedBytes[1], encodedBytes[2], encodedBytes[3]
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Write_EEPROM_Channel_Label (self, channelNum, label ):

        if channelNum > self.EEPROM_Mem_Address["channel_ShowLabel"][self.totalSlots]:
            return

        lsb = ((channelNum * self.EEPROM_Mem_Address["channel_Label"][self.memOffset]) +
               self.EEPROM_Mem_Address["channel_Label"][self.lsb])
        msb = self.EEPROM_Mem_Address["channel_Label"][self.msb]
        totalBytes = self.EEPROM_Mem_Address["channel_Label"][self.memLength]

        # strip blanks
        noBlankLabel = label.strip()
        labelBytes = bytes(noBlankLabel.ljust(totalBytes), 'utf-8')


        checksum = (lsb + msb + totalBytes) % 256

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   lsb,
                   msb,
                   totalBytes,
                   checksum,
                   labelBytes[0], labelBytes[1], labelBytes[2], labelBytes[3], labelBytes[4]
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))

    def Radio_Write_EEPROM_Channel_ShowLabel (self, channelNum, showLabel ):

        #
        #   Don't write to EEPROMs showLabels 10+
        #
        if channelNum > self.EEPROM_Mem_Address["channel_ShowLabel"][self.totalSlots]:
            return

        lsb = (channelNum * self.EEPROM_Mem_Address["channel_ShowLabel"][self.memOffset]) + \
              self.EEPROM_Mem_Address["channel_ShowLabel"][self.lsb]
        msb = self.EEPROM_Mem_Address["channel_ShowLabel"][self.msb]
        totalBytes = self.EEPROM_Mem_Address["channel_ShowLabel"][self.memLength]

        checksum = (lsb + msb + totalBytes) % 256

        if showLabel == 'Yes':
            value = 0x3
        else:
            value = 0x0

        command = [self.toRadioCommandDict["TS_CMD_WRITEMEM"],
                   lsb,
                   msb,
                   totalBytes,
                   checksum,
                   value
                   ]

        self.theRadio.sendCommandToMCU(bytes(command))


#   MCU Commands
#########################################################################################
####    Start of command processing sent by Radio(MCU) to Screen
#########################################################################################

    #
    #   The "v1" command is used for smallest tuning rate
    #

    def v1_UX_Set_Tuning_Preset_1(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_1_VAR.set(value)


    #
    #   The "v2" command is used for smallest tuning rate
    #
    def v2_UX_Set_Tuning_Preset_2(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_2_VAR.set(value)

    #
    #   The "v3" command 1s used for the third (middle) tuning rate
    #
    def v3_UX_Set_Tuning_Preset_3(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_3_VAR.set(value)

    #
    #   The "v4" command 1s used for the next largest tuning rate
    #
    def v4_UX_Set_Tuning_Preset_4(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_4_VAR.set(value)


    #
    #   The "v5" command 1s used for the largest tuning rate
    #
    def v5_UX_Set_Tuning_Preset_5(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_5_VAR.set(value)

    #
    #   The "cn" command indicates which tuning step is active (1(smallest) - 5(largest)
    #
    def cn_UX_Set_Active_Tuning_Preset(self, buffer):

        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tuning_Preset_Selection_VAR.set(value)

        match value:
            case "5":
                if (self.update_Tuning_Preset_Button_Label):
                    self.tuning_Preset_Label_VAR.set(self.tuning_Preset_5_VAR.get())
                self.tuning_Preset_Selection_VAR.set(5)
                self.currentVFO_Tuning_Rate = int(self.tuning_Preset_5_VAR.get())

            case "4":
                if (self.update_Tuning_Preset_Button_Label):
                    self.tuning_Preset_Label_VAR.set(self.tuning_Preset_4_VAR.get())
                self.tuning_Preset_Selection_VAR.set(4)
                self.currentVFO_Tuning_Rate = int(self.tuning_Preset_4_VAR.get())
            case "3":
                if (self.update_Tuning_Preset_Button_Label):
                    self.tuning_Preset_Label_VAR.set(self.tuning_Preset_3_VAR.get())
                self.tuning_Preset_Selection_VAR.set(3)
                self.currentVFO_Tuning_Rate = int(self.tuning_Preset_3_VAR.get())
            case "2":
                if (self.update_Tuning_Preset_Button_Label):
                    self.tuning_Preset_Label_VAR.set(self.tuning_Preset_2_VAR.get())
                self.tuning_Preset_Selection_VAR.set(2)
                self.currentVFO_Tuning_Rate = int(self.tuning_Preset_2_VAR.get())
            case "1":
                if (self.update_Tuning_Preset_Button_Label):
                    self.tuning_Preset_Label_VAR.set(self.tuning_Preset_1_VAR.get())
                self.tuning_Preset_Selection_VAR.set(1)
                self.currentVFO_Tuning_Rate = int(self.tuning_Preset_1_VAR.get())

        self.updateRateMultiplier()
        self.updateJogTracking()
        self.updateLabelTuning_Multiplier()


    #
    #   The "ch" command originates from the EEPROM and is added to the frequency to shift it
    #
    def chGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

    #
    #   The "vh" command originates from the EEPROM and is added to the frequency to shift it
    #
    def vhGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

    #
    #   The "vo" command originates from the EEPROM and is added to the frequency to shift it
    #
    def voGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

    #
    #   The "vp" command originates from the EEPROM and is added to the frequency to shift it
    #
    def vpGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        print("vp get called:", "buffer =", buffer)
        print("vp related to display shift")
        print("value=", value, sep='*', end='*')
        print("\n")

    #
    #   The "vq" command is referred to as display option 2 in EEPROM
    #
    def vqGet(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        print("vq get called:", "buffer =", buffer)
        print("vq related to display shift")
        print("value=", value, sep='*', end='*')
        print("\n")


    #
    #   The "sv" command is stores the text of the firmware version
    #
    def sv_UX_Set_SW_Version(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        print("sv get called:", "buffer =", buffer)
        print("sv software version")
        print("value=", value, sep='*', end='*')
        print("\n")


    #
    #   The "sc" command is stores the text of the operators callsign
    #
    def sc_UX_Set_User_Callsign(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
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
        print("cm get called:", "buffer =", buffer)
        print("cm display version and callsign?")
        print("value=", value, sep='*', end='*')
        print("\n")


    #
    #   The "c0" command determines whether we are in text (yellow box) or graphics mode
    #
    def c0_UX_Toggle_Classic_uBITX_Control(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        print("c0 get called:", "buffer =", buffer)
        print("value=", value, sep='*', end='*')
        print(type(value), sep='*', end='*')
        print("\n")
        if value == "0":
            print(" exiting Classic uBITX control")
            if self.classic_uBITX_ControlWindowObj != None:
                self.classic_uBITX_ControlWindowObj.pack_forget()
                self.classic_uBITX_ControlWindowObj = None
            if self.classic_uBITX_ControlWindow != None:
                self.classic_uBITX_ControlWindow.destroy()
                self.classic_uBITX_ControlWindow = None

        else:
            print(" entering classic uBITX control")
            self.displayClassic_uBITXControlWindow()


    #
    # The purpose of this command is a little puzzling
    # code talks about this being used to eliminate duplicate data
    # Only sent on the first attempt to lock the screen
    # Also contains the text for the speaker button
    #
    def s0_UX_Greenbox_Line1(self, buffer):
        print("s0 called")
        print("buffer=", buffer)
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.displayLine1Classic_uBITX_Control(value)


    def s1_UX_Greenbox_Line2(self, buffer):
        print("s1 called")
        print("buffer=", buffer)
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.displayLine2Classic_uBITX_Control(value)


    def sh_UX_Get_Memory(self, buffer):

        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if (self.memReadingState == "Freq"):
            freq = int(value,16) & 0x1FFFFFFF
            mode = (int(value,16) >> 29) & 0x7

            self.channelWindow.EEPROM_SetChanneFreqMode(
                self.EEPROM_Current_Slot_Freq,
                freq,
                mode)
            self.EEPROM_Current_Slot_Freq += 1
            if (self.EEPROM_Current_Slot_Freq ==
                    self.EEPROM_Mem_Address["channel_freq_Mode"][self.totalSlots]):
                self.EEPROM_Current_Slot_Freq = 0
                self.memReadingState = "Label"
        elif (self.memReadingState == "Label"):

            self.channelWindow.EEPROM_SetChannelLabel(
                self.EEPROM_Current_Slot_Label,
                value)
            # if self.EEPROM_Current_Slot_Label == 9:
            #         print("label slot=", self.EEPROM_Current_Slot_Label, "value=", value, sep='*', end='*')
            self.EEPROM_Current_Slot_Label += 1
            if (self.EEPROM_Current_Slot_Label ==
                    self.EEPROM_Mem_Address["channel_Label"][self.totalSlots]):
                self.EEPROM_Current_Slot_Label = 0
                self.memReadingState = "ShowLabel"
        elif (self.memReadingState == "ShowLabel"):
            if (ord(value) == 0):
                # print("show label is a 0")
                self.channelWindow.EEPROM_SetChannelShowLabel(
                    self.EEPROM_Current_Slot_ShowLabel,
                    "No")

            else:
                # print("show label is a 3")
                self.channelWindow.EEPROM_SetChannelShowLabel(
                    self.EEPROM_Current_Slot_ShowLabel,
                    "Yes")

            self.EEPROM_Current_Slot_ShowLabel += 1
            if (self.EEPROM_Current_Slot_ShowLabel ==
                    self.EEPROM_Mem_Address["channel_ShowLabel"][self.totalSlots]):
                self.EEPROM_Current_Slot_ShowLabel = 0
                self.memReadingState = "Freq"
        else:
            print("unknown memory fetch state")



    def vn_UX_ACK_Memory_Write(self, buffer):
        # if (pm.vn.val == 358) // key Type Write Complete
        # {
        #     nSendProcess.val = 11
        # } else if (pm.vn.val == 28) // key Type Write Complete
        # {
        #     nSendProcess.val = 12
        # } else if (pm.vn.val == 24) // key Type Write Complete
        # {
        #     nSendProcess.val = 13
        # } else if (pm.vn.val == 258) // key Type Write Complete
        # {
        #     nSendProcess.val = 14
        # } else if (pm.vn.val == 259) // key Type Write Complete
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        if self.CurrentDebug:
            print("vn get called:", "buffer =", buffer)
            print("buffer=", buffer)
            if (int(value) == 358):
                print("write complete for keychange, mem=", int(value))
            elif (int(value) == 28):
                print("write complete for new WPM, mem=", int(value))
            elif (int(value) == 259):
                print("write complete for new RX->TX, mem=", int(value))
            elif (int(value) == 258):
                print("write complete for new TX->RX, mem=", int(value))
            else:
                print("memory location write complete, mem=", int(value))





    def cl_UX_Lock_Screen(self, buffer):

        if (self.lock_Button_On):
            self.lock_Button_On = False
            self.lock_Button.configure(style='Button2b.TButton', state="normal")
            self.lock_VAR.set("\nLOCK\n")
            self.unlockUX()
        else:
            self.lock_Button_On = True
            self.lock_Button.configure(style='RedButton2b.TButton', state='pressed')
            self.lock_VAR.set("\nLOCKED\n")
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
        # self.store_Button.configure(state="disabled")
        # self.recall_Button.configure(state="disabled")
        self.tuning_Preset_Button.configure(state="disabled")
        self.ATT_Jogwheel.setStateDisabled()
        self.IFS_Jogwheel.setStateDisabled()
        self.tuning_Jogwheel.setStateDisabled()

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
        # self.store_Button.configure(state="normal")
        # self.recall_Button.configure(state="normal")
        self.tuning_Preset_Button.configure(state="normal")
        if (self.ATT_Button_On == True):
            self.ATT_Jogwheel.setStateNormal()
        if (self.IFS_Button_On == True):
            self.IFS_Jogwheel.setStateNormal()
        self.tuning_Jogwheel.setStateNormal()

    # def labelScale_Set_State(self, labeledScale, newstate):
    #     #
    #     #   disabling/enabling a label scale requires disabling its children
    #     #
    #     for child in labeledScale.winfo_children():
    #         if hasattr(child,'state'):
    #             child.configure(state=newstate)


    def cj_UX_Speaker_Toggle(self, buffer):

        if (self.speaker_Button_On):
            self.speaker_Button_On = False
            self.speaker_Button.configure(style='Button2b.TButton', state="normal")
            self.speaker_VAR.set("\nSPEAKER\n")
        else:
            self.speaker_Button_On = True
            self.speaker_Button.configure(style='RedButton2b.TButton', state="pressed")
            self.speaker_VAR.set("\nSPK MUTED\n")


    def cs_UX_SPLIT_Toggle(self, buffer):
        if (self.split_Button_On):
            self.split_Button_On = False
            self.split_Button.configure(style='Button2b.TButton', state="normal")
        else:
            self.split_Button_On = True
            self.split_Button.configure(style='GreenButton2b.TButton', state="pressed")
    #
    #   This appears to be a no-op command. If the last rit TX frequency does not equal
    #   the current frequency, this is called to set the VFO to the RIT TX frequency which happens to be
    #   the current vfo setting anyway.
    #
    def vr_UX_Update_RIT_Freq(self, buffer):
        if self.CurrentDebug:
            print("vr called")  # command is rit related
            print(buffer)


    def cr_UX_RIT_Toggle(self, buffer):
        if (self.rit_Button_On):
            self.rit_Button_On = False
            self.rit_Button.configure(style='Button2b.TButton', state="normal")
        else:
            self.rit_Button_On = True
            self.rit_Button.configure(style='GreenButton2b.TButton', state="pressed")

    def vf_UX_ATT_Level(self, buffer):
        print("vf called")
        print(buffer)
        value = int(self.extractValue(buffer, 10, len(buffer) - 3))

        #
        #   Zero Value indicated Radio turning off the ATT
        #
        if (value == 0):
            self.ATT_Jogwheel.setStateDisabled()
            self.ATT_Status_VAR.set("ATT (OFF)")
            self.ATT_Button_On = False
        else:
            if self.ATT_Jogwheel.state == 'disabled':
                self.ATT_Jogwheel.setStateNormal()
                self.ATT_Status_VAR.set("ATT (ON)")
                self.ATT_Button_On = True
            #
            # mjh normally ux should be set to the value ack-ed by mcu. Problem with this
            # with jog wheels is that they jerk around too much because of all the callbacks
            # This can also cause oscillation where are reported and stored in jogwheel
            # much after and so when correcting generate more old traffic.
            # On balance the chance of a lost packet is pretty low, so best option is to not
            # repond to the ack-ed value from the MCU
            #
            # BUT...
            # In Classic mode, still need to update the jogwheel...
            #
            if self.classic_uBITX_ControlWindow != None:
                self.ATT_Jogwheel.set(value)            # Set UX to value acked by MCU


    def ci_UX_IFS_State_Set(self, buffer):
        print("ci called")
        print(buffer)
        value = int(self.extractValue(buffer, 10, len(buffer) - 3))

        if (value == 0):                            # Zero value indicates IFS being turned off
            self.IFS_Jogwheel.setStateDisabled()
            self.IFS_Status_VAR.set("IFS (OFF)")
            self.IFS_Button_On = False
        else:
            self.IFS_Jogwheel.setStateNormal()
            self.IFS_Status_VAR.set("IFS (ON)")
            self.IFS_Button_On = True


    def vi_UX_IFS_Level(self, buffer):      #verification by MCU of new value
        print("vi called")
        print(buffer)

        value = int(self.extractValue(buffer, 10, len(buffer) - 3))
        #
        # mjh normally ux should be set to the value ack-ed by mcu. Problem with this
        # with jog wheels is that they jerk around too much because of all the callbacks
        # This can also cause oscillation where are reported and stored in jogwheel
        # much after and so when correcting generate more old traffic.
        # On balance the chance of a lost packet is pretty low, so best option is to not
        # repond to the ack-ed value from the MCU
        #
        #BUT.....
        # Need to respond when in Classic UX Mode. Can use a check for null to figure out whether we update or not
        #
        #
        # print("MCU Reporting vi_UX_IFS_Level", value)
        if self.classic_uBITX_ControlWindow != None:
            self.IFS_Jogwheel.set(value)
        # print("MCU After setting vi_UX_IFS_Level get", self.IFS_Jogwheel.get())


    def cx_UX_TX_Stop_Toggle(self, buffer):
        if (self.stop_Button_On):
            self.stop_Button_On = False
            self.stop_Button.configure(style='Button2b.TButton', state="normal")
        else:
            self.stop_Button_On = True
            self.stop_Button.configure(style='RedButton2b.TButton', state="pressed")

    #
    #   The "vc" command indicates a new frequency for the Primary
    #
    def vc_UX_Set_Primary_VFO_Frequency(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.primary_VFO_VAR.set(value)
        if self.channelWindow != None:      #  Only update frequency if the channel window has been created once
            self.channelWindow.update_Current_Frequency(self.primary_VFO_VAR.get())

        self.updateJogTracking()

    #
    #   The "cc" command indicates a change to a new mode for primary (e.g. USB, LSB, etc.)
    #
    def cc_UX_Set_Primary_Mode(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.primary_Mode_VAR.set(self.modeNum_To_TextDict[value])
        if self.channelWindow != None:
            # Only update frequency if the channel window has been created once
            self.channelWindow.update_Current_Mode(self.primary_Mode_VAR.get())


    #
    #   The "va" command indicates assignment of vfoA to new frequency
    #
    def va_UX_Set_VFO_A_Frequency(self, buffer):
        if (self.channelWindow != None) and (self.channelWindow.scanRunning):
            print("***Ignoring va command as we're scanning***")
            return  # ignore the VFO A command during scanning as it can be out of order

        value = self.extractValue(buffer, 10, len(buffer) - 3)

        print("***va get called:***", "buffer =", buffer)
        print("va assign vfo a frequency")
        print("value=", value, sep='*', end='*')
        print("\n")

        if (self.vfo_VAR.get()== self.VFO_A):       #update displayed frequency
            self.primary_VFO_VAR.set(value)
            print("Updating primary vfo", value, sep='*', end='*')
            print("\n")
        else:
            self.secondary_VFO_VAR.set(value)
            print("Updating secondary vfo", value, sep='*', end='*')
            print("\n")



    #
    #   The "ca" command indicates assignment of a new mode to vfoA
    #
    def ca_UX_Set_VFO_A_Mode(self, buffer):
        if (self.channelWindow != None) and (self.channelWindow.scanRunning):
            print("***Ignoring ca command as we're scanning***")
            return  # ignore the VFO A command during scanning  as it can be out of order

        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if (self.vfo_VAR.get()== self.VFO_A):       #update displayed frequency
            self.primary_Mode_VAR.set(self.modeNum_To_TextDict[value])
        else:
            self.secondary_Mode_VAR.set(self.modeNum_To_TextDict[value])


        print("***ca get called:***", "buffer =", buffer)
        print("ca assign mode for vfoA frequency")
        print("value=", value, sep='*', end='*')
        print("\n")

    #
    #   The "vb" command indicates assignment of vfoB to new frequency
    #
    def vb_UX_Set_VFO_B_Frequency(self, buffer):

        if (self.channelWindow != None) and (self.channelWindow.scanRunning):
            return  # ignore the VFO B command during scanning as it can be out of order

        value = self.extractValue(buffer, 10, len(buffer) - 3)


        if (self.vfo_VAR.get()== self.VFO_B):       #update displayed frequency
            self.primary_VFO_VAR.set(value)
        else:
            self.secondary_VFO_VAR.set(value)

        print("***vb get called:***", "buffer =", buffer)
        print("vb assign vfo b frequency")
        print("value=", value, sep='*', end='*')
        print("\n")
    #
    #   This sets VFO B to a new mode
    #
    def cb_UX_Set_VFO_B_Mode(self, buffer):

        if (self.channelWindow != None) and (self.channelWindow.scanRunning):
            return  # ignore the VFO B command during scanning as it can be out of order

        value = self.extractValue(buffer, 10, len(buffer) - 3)

        if (self.vfo_VAR.get()== self.VFO_B):       #update displayed frequency
            self.primary_Mode_VAR.set(self.modeNum_To_TextDict[value])
        else:
            self.secondary_Mode_VAR.set(self.modeNum_To_TextDict[value])

        print("***cb get called:***", "buffer =", buffer)
        print("cb assign mode for vfoB frequency")
        print("value=", value, sep='*', end='*')
        print("\n")

    #
    #   The "vt" command stores the CW tone
    #
    def vt_UX_SET_CW_Tone(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.tone_value_VAR.set(value)


    #
    #   The "ck" command stores which cw key is being used
    #
    def ck_UX_Set_CW_Key_Type(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.key_type_value_VAR.set(self.CW_KeyType[value])

    #
    #   The "vs" command stores words/minute
    #
    def vs_UX_Set_CW_Speed(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.key_speed_value_VAR.set(str(int(1200/int(value))))


    #
    #   The "vy" command stores delay returning after last cw character
    #
    def vy_UX_Set_CW_Delay_Returning_to_RX(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.delay_returning_to_rx_value_VAR.set(str(int(value)*10))



    #
    #   The "ve" command stores delay prior to TX 1st cw character
    #
    def ve_UX_Set_CW_Delay_Starting_TX(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)
        self.delay_starting_tx_value_VAR.set(str(int(value)*2))

    #
    #   Returns active VFO, VFO-A=0, VFO-B=1
    #
    def cv_UX_VFO_Toggle(self, buffer):
        value = self.extractValue(buffer, 10, len(buffer) - 3)

        self.vfo_VAR.set(self.Text_To_VFO[value])
        saveSecondary_VFO = self.secondary_VFO_VAR.get()
        saveSecondary_Mode = self.secondary_Mode_VAR.get()

        self.secondary_VFO_VAR.set(self.primary_VFO_VAR.get())
        self.secondary_Mode_VAR.set(self.primary_Mode_VAR.get())

        self.primary_VFO_VAR.set(saveSecondary_VFO)
        self.primary_Mode_VAR.set(saveSecondary_Mode)

########################################################################################
#   End processing of commands sent by MCU to Screen
########################################################################################


