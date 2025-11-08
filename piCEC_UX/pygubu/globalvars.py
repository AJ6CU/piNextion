import os
import tkinter.font as font

#application required files################################################
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# to use pyinstaller we need to get the resource not the path
# resource_path is in globalvars
#

config = None

RELOADICON = resource_path("img_Reload-24x24.png")
BAUD = 9600
NUMBER_DELIMITER = ""               # Loaded with value from configuration file


#   VFO Formatting Functions
#####################################################################################
### Start VFO Formatting Functions
#   These are methods are used to format the VFO with a delimiter (typically a period)
#   And to offset the VFO if we are in CW mode and the user has selected to see the TX freq
#####################################################################################

def formatVFO(VFO):
    global NUMBER_DELIMITER
    reversed_VFO = VFO[::-1]  # Reverse the string
    new_string_parts = []
    for i, char in enumerate(reversed_VFO):
        new_string_parts.append(char)
        # Insert the character after every 'n' characters, except at the very end
        if (i + 1) % 3 == 0 and (i + 1) != len(reversed_VFO):
            new_string_parts.append(NUMBER_DELIMITER)

    return "".join(new_string_parts[::-1])  # Join parts and reverse back

def updateNUMBER_DELIMITER(value):
    global NUMBER_DELIMITER
    NUMBER_DELIMITER = value
    print("update Number Delimiter, now = ", NUMBER_DELIMITER)


def formatFrequency(vfoStrVar, frequency, freqOffset=0):
    temp = str(int(frequency) + freqOffset)
    vfoStrVar.set(formatVFO(temp))


def unformatFrequency(vfoStrVar, includeOffset=False, freqOffset=0):
    if includeOffset:
        return (vfoStrVar.get().replace(NUMBER_DELIMITER, ""))
    else:
        return (str(int(vfoStrVar.get().replace(NUMBER_DELIMITER, "")) - freqOffset))

def formatCombobox( combobox, family="Arial", size="36", weight="bold"):
    combobox.configure(font=font.Font(family=family, size=size, weight=weight))
    #
    #   The following is pure magic....  Found after hours of search. Basically the first command
    #   discovers the handle to the ListBox that is hidden below the combobox
    #   with this handle you can then set the drop down to the fonts used by the combobox.
    #   grab (create a new one or get existing) popdown
    popdown = combobox.tk.eval('ttk::combobox::PopdownWindow %s' % combobox)
    #   configure popdown font
    combobox.tk.call('%s.f.l' % popdown, 'configure', '-font', combobox['font'])