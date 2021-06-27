from tkinter import Entry, Frame, Text, Tk, StringVar, Toplevel, XView
from tkinter.constants import END, HORIZONTAL, INSERT, TOP, X, Y
from tkinter.ttk import Progressbar, Scrollbar

from .constants import DEFAULT_ROW_WIDTH


class StatusWidget():
    def __init__(self, window: Tk) -> None:
        self._frame = Frame(window, width=DEFAULT_ROW_WIDTH, height=20)
        self.__initialText = "Click Scrape to Start"
        self.__statusText = Text(self._frame,
                                 height=5,
                                 width=DEFAULT_ROW_WIDTH)
        self.__statusText.pack(fill=X, side=TOP)
        self.__statusText.insert(INSERT, self.__initialText)
        # Scrollbar(self.__statusEntry, orient="vertical", ).pack(side=RIGHT)

        self.__progressBar = Progressbar(
            self._frame, orient=HORIZONTAL, mode='indeterminate')

    def startLoading(self):
        self.__progressBar.pack(fill=Y)
        self.__progressBar.anchor('e')
        self.__progressBar.start()

    def finishLoading(self):
        self.__progressBar.stop()
        self.__progressBar.pack_forget()
        self.__statusText.insert(END, "...COMPLETED!"+"\n\n")
        self.__statusText.insert(END, self.__initialText+"\n")
        self.__statusText.see("end")

    def getWidget(self):
        return self._frame

    def updateStatusReadout(self, text: str):
        self.__statusText.insert(END, "\n"+text)
        self.__statusText.see("end")
