#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from piCEC_UX import piCECNextion


#
# Builder definition section
#

class piCECNextionBO(BuilderObject):
    class_ = piCECNextion


_builder_id = "projectcustom.piCECNextion"
register_widget(
    _builder_id, piCECNextionBO, "piCECNextion", ("ttk", "Project Widgets")
)
