from tkinter import Tk, Button, Label, Entry, Frame, filedialog
from tkinter.constants import SUNKEN


class CustomGridWidget:
    def __init__(self, window) -> None:
        # Create Frame
        self._row = -1
        self._frame = Frame(window, bd=1, relief=SUNKEN)
        self._window = window

    def getWidget(self):
        return self._frame

    def _incrementAndGetRow(self):
        self._row += 1
        return self._row
