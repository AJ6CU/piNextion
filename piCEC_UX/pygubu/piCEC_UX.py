#!/usr/bin/python3
import pathlib
import sys
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
from tkinter import messagebox


root = None
mainWindow = None
comPort = None
myRadio = None


#
#   once a valid port is found, then we can start the main window.
#
def startMainWindow(comPortName, comPort):

    mainWindow.place(x=0, y=0)                          # place the mainWindow on the screen
    # mainWindow.pack()
    mainWindow.update_idletasks()
    mainWindow_width = mainWindow.winfo_width()
    print("mainWindow_width:", mainWindow_width)
    mainWindow_height = mainWindow.winfo_height()
    print("mainWindow_height:", mainWindow_height)

    geo = str(mainWindow_width) +"x"+ str(mainWindow_height)
    print("geo:",geo)

    root.geometry(geo)

    gv.config.setComPort(comPortName)  # update the config file if necessary because of comport selection
    print(" radio:", comPortName)
    # comPort.setComPort(comPortName)
    myRadio = piRadio(comPortName, comPort, mainWindow)  # Initialize the Radio object with selected port



    mainWindow.attachRadio(myRadio)         # tell the mainWindow how to talk to the radio

    myRadio.rebootRadio()                   # We reboot the radio because it sends a bunch of initialization values on startup
                                            # to the Nextion screen. We need to capture them

    myRadio.readALLValues()                 # Now after reboot, read in the initialization values


    mainWindow.initUX()                     # With the initialization values read in, we can perform some initialization functions
                                            # like setting up tuning rate

    myRadio.updateData()  # This process read any data available, but dont schedule followup

#
#   Main program and loop
#
root = tk.Tk()

# root.minsize(1020, 800)
# root.minsize(775, 800)
# root.geometry("1020x800")
root.title("PiCEC - A Nextion Emulator for CEC Software")


gv.config = configuration(root)                    # Read in config data, if missing preload with defaults
                                                # Root is passed to allow popup error messages

root.update()

mainWindow_x_pos = root.winfo_x()
print(mainWindow_x_pos)


mainWindow_y_pos = root.winfo_y()
print(mainWindow_y_pos)



mainWindow = piCECNextion(root)
mainWindow.update()
comPort = comportManager(root,startMainWindow)
#
# root.update()
#
# mainWindow_x_pos = root.winfo_x()
# print(mainWindow_x_pos)
#
#
# mainWindow_y_pos = root.winfo_y()
# print(mainWindow_y_pos)
#
# mainWindow.update_idletasks()
# mainWindow_width = mainWindow.winfo_width()
# print("mainWindow_width:",mainWindow_width)
# mainWindow_height = mainWindow.winfo_height()
# print("mainWindow_height:",mainWindow_height)
#
# comPortWindow_width = comPort.winfo_width()
# print("comPortWindow_width:",comPort.winfo_width())
# comPortWindow_height = comPort.winfo_height()
# print("comPortWindow_height:",comPort.winfo_height())
#
comPort.place(relx=0.80, rely=1, anchor="s")
# x_pos = mainWindow_x_pos + mainWindow_width -10 - comPortWindow_width
# y_pos = mainWindow_y_pos + mainWindow_height -10 - comPortWindow_height
#
# print(x_pos,y_pos)

# comPort.place(x=x_pos, y=y_pos)

if not comPort.getComPort():
    root.after(500, comPort.retry() )           # If we failed to get a comport the easy way, try again

root.mainloop()