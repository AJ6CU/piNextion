#!/usr/bin/python3
import tkinter as tk
import memToVFOui as baseui


#
# Manual user code
#

class memToVFO(baseui.memToVFOUI):
    channelList = []
    currentChannel = 0

    def __init__(self, master=None, mainWindow=None, **kw):


        super().__init__(master, **kw)
        self.mainWindow = mainWindow

        for child in self.scrolledMemoryFrame.innerframe.winfo_children():
            memToVFO.channelList.append(child)
        # print("channel name =", self.channelList[1].channel_Label_VAR.get())
        print("total channels=", len(self.channelList))

    def setChannelLabel(self, label):
        memToVFO.channelList[memToVFO.currentChannel].Label_VAR.set(label)
        memToVFO.currentChannel += 1
        if memToVFO.currentChannel == 9:
            memToVFO.currentChannel = 0

    def setChanneFreqMode(self, freq, mode):

        memToVFO.channelList[memToVFO.currentChannel].Freq_VAR.set(str(freq))
        memToVFO.channelList[memToVFO.currentChannel].Mode_VAR.set(self.mainWindow.modeNum_To_TextDict[str(mode)])
        memToVFO.currentChannel += 1
        if memToVFO.currentChannel == len(self.channelList):
            memToVFO.currentChannel = 0

    def apply_CB(self):
        print("memToVFO apply CB")
        self.destroy()

    def cancel_CB(self):
        print("memToVFO cancel CB")
        self.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = memToVFO(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
