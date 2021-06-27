from tkinter import Tk, Button, Label, Entry, Frame
from tkinter.constants import SUNKEN
from tkinter.font import BOLD


class SettingsWidget:

    def __init__(self, window):
        self.row = -1
        anchor = 'W'
        padx = 5
        pady = 5
        self.frame = Frame(window, bd=1, relief=SUNKEN)

        # Login Page
        Label(self.frame, text="Login Page URL:").grid(
            sticky=anchor,
            pady=pady, padx=padx,
            row=self._incrementAndGetRow(), column=0)
        Entry(self.frame).grid(
            pady=pady, padx=padx,
            row=self.row, column=1)

        # Login Asset
        Label(self.frame, text="Login Asset URL:").grid(
            pady=pady, padx=padx,
            sticky=anchor,
            row=self._incrementAndGetRow(), column=0)
        Entry(self.frame).grid(
            pady=pady, padx=padx,
            row=self.row, column=1)

        # Browser Driver
        Button(self.frame, text="Get Browser Driver Executable").grid(
            pady=pady, padx=padx,
            sticky=anchor,
            row=self._incrementAndGetRow(), column=0)
        Entry(self.frame).grid(
            pady=pady, padx=padx,
            row=self.row, column=1)

    def _incrementAndGetRow(self):
        self.row += 1
        return self.row

    def getSettingsWidget(self):
        return self.frame
