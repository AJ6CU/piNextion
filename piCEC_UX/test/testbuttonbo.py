#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from testbutton import testButtonClass


#
# Builder definition section
#

class testButtonClassBO(BuilderObject):
    class_ = testButtonClass


_builder_id = "projectcustom.testButtonClass"
register_widget(
    _builder_id, testButtonClassBO, "testButtonClass", (
        "ttk", "Project Widgets")
)
