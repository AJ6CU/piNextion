
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
                top = tk.Toplevel()
                messagebox.showinfo("Information", "Empty configuration file was found\n" +
                                                    "Default values saved in" + configuration_file +
                                                    "\nReview and edit this file if needed",
                                                    parent=master)
                self.writeDefaults()
            else:
                self.config_data = json.load(config_file)
                config_file.close()
        except FileNotFoundError:
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
        self.config_data = {"serialPort": serialPort,
                       "scanSetSettings": [
                           [0,"None"], [1,"None"], [2, "None"], [3, "None"], [4, "None"],
                           [5, "None"], [6, "None"], [7, "None"], [8, "None"], [9, "None"],
                           [10, "None"], [11, "None"], [12, "None"], [13, "None"], [14, "None"],
                           [15, "None"], [16, "None"], [17, "None"], [18, "None"], [19, "None"]
                       ]}
        # json.dump(config_data, config_file)
        self.saveConfig()

    def getComPort(self):
        return self.config_data["serialPort"]
    def setComPort(self,port):
        self.config_data["serialPort"] = port

    def getscanSetSettings(self, channel):
        return self.config_data["scanSetSettings"][channel][1]
    def setscanSetSettings(self, channel, scanSet):
        self.config_data["scanSetSettings"][channel][1] = scanSet
        self.saveConfig()

    def saveConfig(self):
        config_file = open(configuration_file, 'w')
        json.dump(self.config_data, config_file)
        config_file.close()