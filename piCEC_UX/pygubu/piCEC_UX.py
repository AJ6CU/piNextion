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
import globalvars as gv




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

root = None
mainWindow = None
comPort = None
myRadio = None




def gotValidPort ():
    if comPort.openSelectedComPort():
        comPort.comportMessage_Frame.pack_forget()
        startMainWindow()
#
#   once a valid port is found, then we can start the main window.
#

def startMainWindow():
    mainWindow.place(x=0, y=0)                          # place the mainWindow on the screen
    gv.config.setComPort(comPort.getSelectedComPort())  # update the config file if necessary because of comport selection
    myRadio = piRadio(comPort.getComPortDesc(), mainWindow, gv.config) # Initialize the Radio object with selected port

    mainWindow.attachRadio(myRadio)         # tell the mainWindow how to talk to the radio

    myRadio.rebootRadio()                   # We reboot the radio because it sends a bunch of initialization values on startup
                                            # to the Nextion screen. We need to capture them

    myRadio.readALLValues()                 # Now after reboot, read in the initialization values

    mainWindow.initUX()                     # With the initialization values read in, we can perform some initialization functions
                                            # like setting up tuning rate
    myRadio.updateData()                    # This process looks for new Radio data. It is scheduled to be run again after completion


#
#   Main program and loop
#

root = tk.Tk()
root.geometry("1070x660")
root.title("PiCEC - A Nextion Emulator for CEC Software")

gv.config = configuration(root)                    # Read in config data, if missing preload with defaults
                                                # Root is passed to allow popup error messages


mainWindow = piCECNextion(root)
comPort = comportManager(root, gotValidPort)
comPort.place(relx=0.835, rely=1.0, anchor="s")
#
#   First try to use the port in config. If valid, just open it
#

if comPort.validateComPort(gv.config.getComPort()):                #test if config port exists in list of ports
    if (comPort.forceUseOfThisPort(gv.config.getComPort())):                          #force it and try to open, if good, then we can start main
        gotValidPort()

root.mainloop()
