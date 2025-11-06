#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import comportManagerui as baseui

import serial.tools.list_ports              # Used to get a list of com ports

import tkinter.messagebox

from time import sleep
from globalvars import *



#
# Manual user code
#

class comportManager(baseui.comportManagerUI):

    waitTime = 5


    def __init__(self, master=None, actionButtonStateChange=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.img_img_Reload24x24 = tk.PhotoImage(file=RELOADICON)
        self.comPortListRefresh.configure(image=self.img_img_Reload24x24)
        self.open_com_port = None

        self.actionButton_CB = actionButtonStateChange         # Callback function invoked when state change

        self.updateComPorts()               #preload the available com ports
        self.comPortsOptionMenu.configure(width=15)

    def validateComPort(self, port):
        #
        #   if it is valid, it will be on list of updated comports
        #
        if (port in self.comPortList):
            return True
        else:
            return False

    def forceUseOfThisPort(self, port):
        savePort = self.availableComPorts_VAR.get()
        self.availableComPorts_VAR.set(port)
        if(self.openSelectedComPort()):
            return True
        else:
            #
            #   Reset selected port
            #
            self.availableComPorts_VAR.set(savePort)
            return False


    def openSelectedComPort (self):
        comPort = self.getSelectedComPort()                    # get the selected com port

        try:
            RS232 = serial.Serial(comPort, BAUD, timeout=5, stopbits=1, parity=serial.PARITY_NONE, xonxoff=0, rtscts=0)
        except: # FileNotFoundError:
            return False
        else:
            self.open_com_port = RS232
            self.comPortsOptionMenu.configure(state="disabled")         # disable selection for life of run
            self.comPortListRefresh.configure(state="disabled")
            # sleep (comportManager.waitTime)                # this does not seem to be required for at least the pico
            return True


    def getComPortDesc (self):
        return self.open_com_port


    def updateComPorts(self, *args):

        ports = serial.tools.list_ports.comports()          #Gets list of ports
        self.comPortList =[("Select Serial Port")]          #Seeds option list with Selection instructions

        for p in ports:                                 #this used to strip down to just the com port# or path
            self.comPortList.append(p.device)
        self.comPortsOptionMenu.set_menu(*self.comPortList)  # put found ports into the option menu


    def radioSerialPortSelected_CB(self, *args):                # callback specified by UX, connected to main
        self.actionButton_CB()





    def getSelectedComPort(self):
        return self.availableComPorts_VAR.get()

