#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from testMe import testMe1


#
# Builder definition section
#

class testMe1BO(BuilderObject):
    class_ = testMe1


_builder_id = "projectcustom.testMe1"
register_widget(
    _builder_id, testMe1BO, "testMe1", ("ttk", "Project Widgets")
)
