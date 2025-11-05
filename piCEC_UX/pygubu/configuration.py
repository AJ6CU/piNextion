
import json
import os
import platform
import tkinter as tk
from tkinter import messagebox

import serial

configuration_file = ".piCEC.ini"

class configuration:

    def __init__(self, master=None, **kw):
        try:
            config_file=open(configuration_file, 'r+')

            if (os.stat(configuration_file).st_size == 0):
                # top = tk.Toplevel(master)
                messagebox.showinfo("Information", "Empty configuration file was found\n" +
                                                    "Default values saved in" + configuration_file +
                                                    "\nReview and edit this file if needed",
                                                    parent=master)
                self.writeDefaults()
            else:
                self.config_data = json.load(config_file)
                config_file.close()
        except FileNotFoundError:
            # top = tk.Toplevel(master)
            messagebox.showinfo("Information", "No configuration file was found\n" +
                                                "Default values saved in" + configuration_file +
                                                "\nReview and edit this file if needed",
                                                parent=master)

            self.writeDefaults()

    def writeDefaults(self):
        if platform.system() == 'Windows':
            serialPort = "com6"

        elif platform.system() == 'Darwin':
            serialPort = "/dev/cu.usbserial-00000000"

        else:
            serialPort = "/dev/ttyS0"

        #
        #   The default for scanSet Settings is all "None"
        #
        self.config_data = {"Serial Port": serialPort,

                            "Scan Settings": {
                                "Scan Set Settings": [
                                    [0,"None"], [1,"None"], [2, "None"], [3, "None"], [4, "None"],
                                    [5, "None"], [6, "None"], [7, "None"], [8, "None"], [9, "None"],
                                    [10, "None"], [11, "None"], [12, "None"], [13, "None"], [14, "None"],
                                    [15, "None"], [16, "None"], [17, "None"], [18, "None"], [19, "None"]],
                                "Scan On Station Time":10000},

                            "Advanced Settings": {
                                "MCU Command Headroom": .01
                            },

                            "Misc Settings": {
                                "Number Delimiter": ".",
                                "TXOffset": "EEPROM"
                            },

                            "Backup": {
                                "masterCal": "",
                                "ssbBFO": "",
                                "cwBFO": ""
                            }
                            }
        self.saveConfig()

    def getComPort(self):
        return self.config_data["Serial Port"]
    def setComPort(self,port):
        self.config_data ["Serial Port"] = port

    # def updateComPort(self, port):
    #     if (self.config_data["Serial Port"] != port):
    #         self.setComPort(port)
    #         self.saveConfig()
    #

    def get_ScanSet_Settings(self, channel):
        return self.config_data["Scan Settings"]["Scan Set Settings"][channel][1]

    def set_ScanSet_Settings(self, channel, scanSet):
        self.config_data["Scan Settings"]["Scan Set Settings"][channel][1] = scanSet
        self.saveConfig()


    def get_Scan_On_Station_Time(self):
        return self.config_data["Scan Settings"]["Scan On Station Time"]

    def set_Scan_On_Station_Time(self, time):
        self.config_data["Scan Settings"]["Scan On Station Time"] = time
        self.saveConfig()


    def get_Advanced_Settings(self, item):
        return self.config_data["Advanced Settings"][item]

    def set_Advanced_Settings(self, item, value):
        self.config_data["Advanced Settings"][item] = value
        self.saveConfig()


    def get_Misc_Settings(self, item):
        return self.config_data["Misc Settings"][item]

    def set_Misc_Settings(self, item, value):
        self.config_data["Misc Settings"][item] = value
        self.saveConfig()


    def get_Backup_Settings(self, item):
        return self.config_data["Backup"][item]

    def set_Misc_Settings(self, item, value):
        self.config_data["Backup"][item] = value
        self.saveConfig()

        


    def saveConfig(self):
        config_file = open(configuration_file, 'w')
        json.dump(self.config_data, config_file)
        config_file.close()