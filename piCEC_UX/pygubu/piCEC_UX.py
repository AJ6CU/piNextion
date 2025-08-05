#!/usr/bin/python3
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
# import piCEC_UXui as baseui
from piCECNextion import piCECNextion
from piRadio import piRadio

# import mystyles  # Styles definition module

# PROJECT_PATH = pathlib.Path(__file__).parent
# PROJECT_UI = "piCEC_UX.ui"
# RESOURCE_PATHS = [PROJECT_PATH]
#define conv2BytesToInt32(lsb,msb) (int)((int16_t)((msb<<8) + lsb));
#// 
#// originally it was the following line. But becausee Nano's do arithmatic strangly, this failed
W// perhaps a new compiler issue. Have to cast everything first and then you can add them
W//#define conv4BytesToLong(lsb,lsb1,lsb2,msb) (unsigned long)(((int)(msb<<24)) + ((int)(lsb2<<16)) + ((int)(lsb1<<8))+lsb);
#define conv4BytesToLong(lsb,lsb1,lsb2,msb) (unsigned long)(((long)msb<<24) + ((long)lsb2<<16) + ((long)lsb1<<8)+ (long)lsb);


#
# Manual user code
#

# class piCECNextion(baseui.piCECNextionUI):
#     def __init__(self, master=None, **kw):
#         super().__init__(
#             master,
#             translator=None,
#             on_first_object_cb=mystyles.setup_ttk_styles,
#             theRadio = None
#         )
#         self.theRadio = None
#
#     def attachRadio(self,radio):
#         self.theRadio = radio
#
#     def mode_lsb_CB(self):
#         self.theRadio.ccPut('2')
#         def sendCommandToMCU(self, commandList):pass


#
#   Main program and loop
#




root = tk.Tk()
mainWindow = piCECNextion(root)
mainWindow.pack(expand=True, fill="both")

# myRadio = piRadio("/dev/ttyS0", mainWindow,True)  # linux
myRadio = piRadio("com6", mainWindow,True) # windows
#myRadio = piRadio("/dev/cu.usbserial-00000000", mainWindow,True) # macos

mainWindow.attachRadio(myRadio)
myRadio.openRadio()
myRadio.readALLValues()

root.after(500,myRadio.updateData)
root.mainloop()
