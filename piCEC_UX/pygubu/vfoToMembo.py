#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from vfoToMem import vfoToMem


#
# Builder definition section
#

class vfoToMemBO(BuilderObject):
    class_ = vfoToMem


_builder_id = "projectcustom.vfoToMem"
register_widget(
    _builder_id, vfoToMemBO, "vfoToMem", ("ttk", "Project Widgets")
)
