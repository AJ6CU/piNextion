import tkinter as tk


from pygubu.api.v1 import (
    BuilderObject,
    register_widget,
)
from tkdial import ImageKnob


#
# Builder definition section
#

class ImageKnob_UXbo(BuilderObject):
    class_ = ImageKnob


_builder_id = "projectcustom.ImageKnob"
register_widget(
    _builder_id, ImageKnob_UXbo, "ImageKnob", ("tk", "Project Widgets")
)