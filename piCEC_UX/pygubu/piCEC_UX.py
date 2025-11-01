#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from time import sleep
# import piCEC_UXui as baseui
from piCECNextion import piCECNextion
from piRadio import piRadio
from configuration import configuration
from comportManager import comportManager



# import mystyles  # Styles definition module

# PROJECT_PATH = pathlib.Path(__file__).parent
# PROJECT_UI = "piCEC_UX.ui"
# RESOURCE_PATHS = [PROJECT_PATH]
#define conv2BytesToInt32(lsb,msb) (int)((int16_t)((msb<<8) + lsb));
#// 
#// originally it was the following line. But becausee Nano's do arithmatic strangly, this failed
# W// perhaps a new compiler issue. Have to cast everything first and then you can add them
# W//#define conv4BytesToLong(lsb,lsb1,lsb2,msb) (unsigned long)(((int)(msb<<24)) + ((int)(lsb2<<16)) + ((int)(lsb1<<8))+lsb);
# define conv4BytesToLong(lsb,lsb1,lsb2,msb) (unsigned long)(((long)msb<<24) + ((long)lsb2<<16) + ((long)lsb1<<8)+ (long)lsb);
# globals(config_Data)
config=None
root = None
mainWindow = None
comPort = None
myRadio = None



def gotValidPort (foundPort):
    if foundPort:
        if comPort.openSelectedComPort():
            comPort.comportMessage_Frame.pack_forget()
            startMainWindow()


def startMainWindow():
    mainWindow.place(x=0, y=0)
    config.updateComPort(comPort.getSelectedComPort())
    print(config.getComPort())
    myRadio = piRadio(comPort.getComPortDesc(), mainWindow, config) # macos
    mainWindow.attachConfig(config)
    mainWindow.attachRadio(myRadio)
    # myRadio.openRadio()

    myRadio.rebootRadio()

    sleep(.5)
    myRadio.readALLValues()
    sleep(2)
    mainWindow.initUX()
    sleep(.5)

    myRadio.updateData()



#
#   Main program and loop
#


config = configuration()


root = tk.Tk()
root.geometry("1086x660")
mainWindow = piCECNextion(root)
comPort = comportManager(root, ###need to test existing port### gotValidPort)
comPort.place(relx=0.8, rely=1.0, anchor="s")

root.mainloop()
