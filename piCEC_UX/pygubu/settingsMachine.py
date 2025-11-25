#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import settingsMachineui as baseui
from configuration import configuration
import globalvars as gv


#
# Manual user code
#
class settingsMachineToplevel(tk.Toplevel):
    def __init__(self, master=None, **kw):
        self.master = master

        self.popup = tk.Toplevel(self.master)

        self.popup.title("Machine Specific Settings")
        self.popup.minsize(750,350)
        self.popup.wait_visibility()  # required on Linux
        self.popup.grab_set()
        self.popup.transient(self.master)

        self.settingsMachineWindow = settingsMachine(self.popup, self.master, **kw)
        self.settingsMachineWindow.pack(expand=tk.YES, fill=tk.BOTH)

class settingsMachine(baseui.settingsMachineUI):
    def __init__(self, master=None, mainWindow=None, **kw):
        self.master = master
        self.mainWindow = mainWindow

        super().__init__(master, **kw)

        self.saveMCU_Command_Headroom = int(gv.config.get_MCU_Command_Headroom()*1000)
        self.saveMCU_Update_Period = gv.config.get_MCU_Update_Period()

        self.MCU_Command_Headroom_VAR.set(str(self.saveMCU_Command_Headroom))
        self.MCU_Update_Period_VAR.set(str(self.saveMCU_Update_Period))

        gv.formatCombobox(self.MCU_Command_Headroom_Combobox, "Arial", "24", "bold")
        gv.formatCombobox(self.MCU_Update_Period_Combobox, "Arial", "24", "bold")

        self.MCU_Command_Headroom_Combobox.configure(values=gv.MCU_Headroom_Values)
        self.MCU_Update_Period_Combobox.configure(values=gv.Frequency_To_Run_UX_loop)

    def apply_CB(self):
        print("Applying settings")

        if int(self.MCU_Command_Headroom_VAR.get()) != self.saveMCU_Command_Headroom:
            gv.config.set_MCU_Command_Headroom(int(self.MCU_Command_Headroom_VAR.get())/1000)


        if int(self.MCU_Update_Period_VAR.get()) != self.saveMCU_Update_Period:
            gv.config.set_MCU_Update_Period(int(self.MCU_Update_Period_VAR.get()))

        self.master.destroy()

    def cancel_CB(self):
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    widget = settingsMachine(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
