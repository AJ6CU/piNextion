import os

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

RELOADICON = resource_path("img_Reload-24x24.png")
BAUD = 9600