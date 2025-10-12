#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from memToVFO import memToVFO


#
# Builder definition section
#

class memToVFOBO(BuilderObject):
    class_ = memToVFO


_builder_id = "projectcustom.memToVFO"
register_widget(
    _builder_id, memToVFOBO, "memToVFO", ("ttk", "Project Widgets")
)
