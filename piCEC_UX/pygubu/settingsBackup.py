#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


import settingsBackupui as baseui
from configuration import configuration
import globalvars as gv
from time import sleep

from tkinter import messagebox


#
# Manual user code
#

class settingsBackupToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Backup Key Radio Settings")
        self.popup.minsize(500,450)
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsBackupWindow = settingsBackup(self.popup, self.master, **kw)
        self.settingsBackupWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsBackup(baseui.settingsBackupUI):
    def __init__(self, master=None,mainWindow=None, **kw):
        super().__init__(master, **kw)
        self.mainWindow = mainWindow

        self.ConfigFile_Master_Cal_VAR.set(self.get_ConfigFile_Master_Cal())
        self.ConfigFile_SSB_BFO_VAR.set(self.get_ConfigFile_SSB_BFO())
        self.ConfigFIle_CW_BFO_VAR.set(self.get_ConfigFile_CW_BFO())
        self.ConfigFile_CW_Keytype_VAR.set(self.get_ConfigFile_CW_Keytype())
        self.ConfigFIle_CW_Speed_VAR.set(self.get_ConfigFile_CW_Speed())
        self.ConfigFile_CW_Sidetone_VAR.set(self.get_ConfigFile_CW_Sidetone())
        self.ConfigFile_CW_Delay_Before_TX_VAR.set(self.get_ConfigFile_CW_Delay_Before_TX())
        self.ConfigFIle_CW_Delay_Returning_To_RX_VAR.set(self.get_ConfigFile_CW_Delay_Returning_To_RX())

        gv.formatCombobox(self.from_Combobox, "Arial", "18", "bold")
        gv.formatCombobox(self.to_Combobox, "Arial", "18", "bold")

        self.from_Combobox_VAR.set("Select")
        self.to_Combobox_VAR.set("Select")
        #
        #   The following are know values and we just need to load the ones that currently exist
        #
        self.EEPROM_Current_CW_Keytype_VAR.set(self.get_Current_CW_Keytype())
        self.EEPROM_Current_CW_Speed_VAR.set(self.get_Current_CW_Speed())
        self.EEPROM_Current_CW_Sidetone_VAR.set(self.get_Current_CW_Sidetone())
        self.EEPROM_Current_CW_Delay_Before_TX_VAR.set(self.get_Current_CW_Delay_Before_TX())
        self.EEPROM_Current_CW_Delay_Returning_To_RX_Label_VAR.set(self.get_Current_CW_Delay_Returning_To_RX())

        #
        #   Following a little complex as we have to request that the radio perform EEPROM Memory reads
        #

        mainWindow.Radio_Req_Master_Cal(self.load_Current_Master_Cal)
        mainWindow.Radio_Req_SSB_BFO(self.load_Current_SSB_BFO)
        mainWindow.Radio_Req_CW_BFO(self.load_Current_CW_BFO)

        mainWindow.Radio_Req_Factory_Master_Cal(self.load_Factory_Master_Cal)
        mainWindow.Radio_Req_Factory_SSB_BFO(self.load_Factory_SSB_BFO)
        mainWindow.Radio_Req_Factory_CW_Speed(self.load_Factory_CW_Speed)
        mainWindow.Radio_Req_Factory_CW_Sidetone(self.load_Factory_CW_Sidetone)
        sleep(.5)
    #
    #   Master Cal getters/setters
    #

    #       Current Master Cal getters/setters
    def load_Current_Master_Cal(self, value):
        self.EEPROM_Current_Master_Cal_VAR.set(value)

    def get_Current_Master_Cal(self):
        return self.EEPROM_Current_Master_Cal_VAR.get()

    def set_Current_Master_Cal(self,value):
        print("setting current master cal=", value)

    #       ConfigFile Master Cal getters/setters
    def get_ConfigFile_Master_Cal(self):
        return gv.config.get_Master_Cal()

    def set_ConfigFile_Master_Cal(self, value):
        gv.config.set_Master_Cal(value)



    #
    #   SSB_BFO getters/setters
    #

    #       Current SSB_BFO Cal getters/setters
    def load_Current_SSB_BFO(self, value):
        self.EEPROM_Current_SSB_BFO_VAR.set(value)

    def get_Current_SSB_BFO(self):
        return self.EEPROM_Current_SSB_BFO_VAR.get()

    def set_Current_SSB_BFO(self,value):
        print("setting current SSB_BFO cal=", value)

    #       ConfigFile SSB_BFO Cal getters/setters
    def get_ConfigFile_SSB_BFO(self):
        return gv.config.get_SSB_BFO()

    def set_ConfigFile_SSB_BFO(self, value):
        gv.config.set_SSB_BFO(value)


    #
    #   CW_BFO getters/setters
    #

    #       Current CW_BFO Cal getters/setters
    def load_Current_CW_BFO(self, value):
        self.EEPROM_Current_CW_BFO_VAR.set(value)

    def get_Current_CW_BFO(self):
        return self.EEPROM_Current_CW_BFO_VAR.get()

    def set_Current_CW_BFO(self,value):
        print("setting current CW_BFO cal=", value)


    #       ConfigFile CW_BFO Cal getters/setters
    def get_ConfigFile_CW_BFO(self):
        return gv.config.get_CW_BFO()

    def set_ConfigFile_CW_BFO(self,value):
        return gv.config.set_CW_BFO(value)


    #
    #   CW Key Type getters/setters
    #

    #       Current Key_type getters/setters
    def get_Current_CW_Keytype(self):
        return self.mainWindow.key_type_value_VAR.get()

    def set_Current_CW_Keytype(self, value):
        print("setting current Key_type=", value)

    #       ConfigFile Key_Type getters/setters
    def get_ConfigFile_CW_Keytype(self):
        return gv.config.get_Keytype()

    def set_ConfigFile_CW_Keytype(self, value):
        gv.config.set_Keytype(value)


    #
    #   Factory: Master Cal getters
    #
    def load_Factory_Master_Cal(self, value):
        self.EEPROM_Factory_Master_Cal_VAR.set(value)

    def get_Factory_Master_Cal(self):
        return self.EEPROM_Factory_Master_Cal_VAR.get()

    #
    #   Factory SSB_BFO getters
    #
    def load_Factory_SSB_BFO(self, value):
        self.EEPROM_Factory_SSB_BFO_VAR.set(value)

    def get_Factory_SSB_BFO(self):
        return self.EEPROM_Factory_SSB_BFO_VAR.get()

    #
    #   Factory CW Speed getters
    #
    def load_Factory_CW_Speed(self, value):
        self.EEPROM_Factory_CW_Speed_VAR.set(value)

    def get_Factory_CW_Speed(self):
        return self.EEPROM_Factory_CW_Speed_VAR.get()

    #
    #   CW_Speed getters/setters
    #


    def get_Current_CW_Speed(self):
        return self.mainWindow.key_speed_value_VAR.get()

    def set_Current_CW_Speed(self,value):
        print("setting current CW_Speed=", value)


    def get_ConfigFile_CW_Speed(self):
        return gv.config.get_CW_Speed()

    def set_ConfigFile_CW_Speed(self,value):
        gv.config.set_CW_Speed(value)

    #
    #   Factory CW Sidetone getters
    #
    def load_Factory_CW_Sidetone(self, value):
        self.EEPROM_Factory_CW_Sidetone_VAR.set(value)

    def get_Factory_CW_Sidetone(self):
        return self.EEPROM_Factory_CW_Sidetone_VAR.get()

    #
    #   CW_Speed getters/setters
    #

    #       Current CW_Sidetone getters/setters
    def get_Current_CW_Sidetone(self):
        return self.mainWindow.tone_value_VAR.get()

    def set_Current_CW_Sidetone(self, value):
        print("setting current CW_Sidetone=", value)

    #       ConfigFile CW_Sidetone getters/setters
    def get_ConfigFile_CW_Sidetone(self):
        return gv.config.get_CW_Tone()

    def set_ConfigFile_CW_Sidetone(self,value):
        gv.config.set_CW_Tone(value)


    #
    #   Delay_Before_TX_Value getters/setters
    #

    #       Current Delay_Before_TX_Value getters/setters
    def get_Current_CW_Delay_Before_TX(self):
        return self.mainWindow.delay_starting_tx_value_VAR.get()

    def set_Current_CW_Delay_Before_TX(self, value):
        print("setting current Delay_Before_TX_Value=", value)

    #       ConfigFile Delay_Before_TX_Value getters/setters
    def get_ConfigFile_CW_Delay_Before_TX(self):
        return gv.config.get_CW_Delay_Before_TX()

    def set_ConfigFile_CW_Delay_Before_TX(self, value):
        gv.config.set_CW_Delay_Before_TX(value)

    #
    #   Delay_Returning_To_RX_Value getters/setters
    #

    #       Current Delay_Returning_To_RX_Value getters/setters
    def get_Current_CW_Delay_Returning_To_RX(self):
        return self.mainWindow.delay_returning_to_rx_value_VAR.get()

    def set_Current_CW_Delay_Returning_To_RX(self, value):
        print("setting current Delay_Returning_To_RX_Value=", value)

    #       ConfigFile Delay_Returning_To_RX_Value getters/setters
    def get_ConfigFile_CW_Delay_Returning_To_RX(self):
        return gv.config.get_CW_Delay_Returning_to_RX()

    def set_ConfigFile_CW_Delay_Returning_To_RX(self, value):
        print("setting current Delay_Returning_To_RX_Value=", value)
        gv.config.set_CW_Delay_Returning_to_RX(value)



    def select_All_Checkbutton_CB(self):
        if self.select_All_Checked_VAR.get() == "1":
            self.Master_Cal_Checked_VAR.set("1")
            self.SSB_BFO_Checked_VAR.set("1")
            self.CW_BFO_Checked_VAR.set("1")
            self.CW_Keytype_Checked_VAR.set("1")
            self.CW_Speed_Checked_VAR.set("1")
            self.CW_Sidetone_Checked_VAR.set("1")
            self.CW_Delay_Before_TX_Checked_VAR.set("1")
            self.CW_Delay_Returning_To_RX_Checked_VAR.set("1")

            self.select_All_Checked_Text_VAR.set("Uncheck to Deselect All")


        else:
            self.Master_Cal_Checked_VAR.set("0")
            self.SSB_BFO_Checked_VAR.set("0")
            self.CW_BFO_Checked_VAR.set("0")
            self.CW_Keytype_Checked_VAR.set("0")
            self.CW_Speed_Checked_VAR.set("0")
            self.CW_Sidetone_Checked_VAR.set("0")
            self.CW_Delay_Before_TX_Checked_VAR.set("0")
            self.CW_Delay_Returning_To_RX_Checked_VAR.set("0")

            self.select_All_Checked_Text_VAR.set("Select All")







    def copy_CB(self):
        print("Applying settings")

        if self.from_Combobox_VAR.get() == "Select":
            messagebox.showinfo(message="Must select a source for the copy", parent=self)
            return
        elif self.to_Combobox_VAR.get() == "Select":
            messagebox.showinfo(message="Must select a destination for the copy", parent=self)
            return
        elif self.from_Combobox_VAR.get() == self.to_Combobox_VAR.get():
            messagebox.showinfo(message="Source and Destination must be different", parent=self)
            return
        else:
            print("passed validation tests")

        #
        #   Build dictionary of source,destination
        #
        selectedValues = {}

        source = self.from_Combobox_VAR.get()
        destination = self.to_Combobox_VAR.get()

        print("Source: ", source)
        print("Destination: ", destination)

        #
        #   Process each line that is checked assigning read/writing file using the infamous "getattr" magic
        #
        if self.Master_Cal_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_Master_Cal", None)
            writeFunction = getattr(self, "set_"+destination+"_Master_Cal", None)

            if readFunction != None and writeFunction != None:
                selectedValues["Master_Cal"] = [writeFunction, readFunction]
                print("adding to dictionary: Master_Cal")

        if self.SSB_BFO_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_SSB_BFO", None)
            writeFunction = getattr(self, "set_"+destination+"_SSB_BFO", None)





            if readFunction != None and writeFunction != None:
                selectedValues["SSB_BFO"] = [writeFunction, readFunction]
                print("adding to dictionary: SSB_BFO")


        if self.CW_BFO_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_CW_BFO", None)
            writeFunction = getattr(self, "set_"+destination+"_CW_BFO", None)

            if readFunction != None and writeFunction != None:
                selectedValues["CW_BFO"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_BFO")


        if self.CW_Keytype_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_CW_Keytype", None)
            writeFunction = getattr(self, "set_"+destination+"_CW_Keytype", None)

            if readFunction != None and writeFunction != None:
                selectedValues["CW_Keytype"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_Keytype")


        if self.CW_Speed_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_CW_Speed", None)
            writeFunction = getattr(self, "set_"+destination+"_CW_Speed", None)

            if readFunction != None and writeFunction != None:
                selectedValues["CW_Speed"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_Speed")


        if self.CW_Sidetone_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_"+source+"_CW_Sidetone", None)
            writeFunction = getattr(self, "set_"+destination+"_CW_Sidetone", None)


            if readFunction != None and writeFunction != None:
                selectedValues["CW_Sidetone"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_Sidetone")


        if self.CW_Delay_Before_TX_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_" + source + "_CW_Delay_Before_TX", None)
            writeFunction = getattr(self, "set_" + destination + "_CW_Delay_Before_TX", None)

            if readFunction != None and writeFunction != None:
                selectedValues["CW_Delay_Before_TX"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_Delay_Before_TX")

        if self.CW_Delay_Returning_To_RX_Checked_VAR.get() == "1":
            readFunction = getattr(self, "get_" + source + "_CW_Delay_Returning_To_RX", None)
            writeFunction = getattr(self, "set_" + destination + "_CW_Delay_Returning_To_RX", None)

            print("CW_Delay_Returning_To_RX: ",  "get_" + source + "_CW_Delay_Returning_To_RX",
                  "set_" + destination + "_CW_Delay_Returning_To_RX")

            if readFunction != None and writeFunction != None:
                selectedValues["CW_Delay_Returning_To_RX"] = [writeFunction, readFunction]
                print("adding to dictionary: CW_Delay_Returning_To_RX")



        if len(selectedValues) == 0:
            messagebox.showinfo(message="Nothing Selected to Copy\n\n"+
                                "Did you forget to check what you wanted to backup?", parent=self)
            return

        warningMessage = "The following Settings in " + destination + " will be overwritten by values from the " + source + " settings:\n\n"
        for key in selectedValues:
            warningMessage = warningMessage +  key  + "\n"

        if(messagebox.askokcancel(title="Confirm Copy", message=warningMessage, parent=self, icon="warning")):
            for key in selectedValues:
                selectedValues[key][0](selectedValues[key][1]())
                print("key=", key, "selectedValues=", selectedValues[key][1]())







        # if int(self.MCU_Command_Headroom_VAR.get()) != self.saveMCU_Command_Headroom:
        #     gv.config.set_MCU_Command_Headroom(int(self.MCU_Command_Headroom_VAR.get())/1000)
        #
        #
        # if int(self.MCU_Update_Period_VAR.get()) != self.saveMCU_Update_Period:
        #     gv.config.set_MCU_Update_Period(int(self.MCU_Update_Period_VAR.get()))

        self.master.destroy()

    def cancel_CB(self):
        print("Cancelling settings")
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsBackup(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
