from tkinter import Tk, Label, StringVar
from tkinter.constants import E, HORIZONTAL, W
from tkinter.ttk import Progressbar

from constants import LEFT_ALIGN, PADDING_X_SMALL, PADDING_Y_SMALL, DEFAULT_ROW_WIDTH
from CustomGridWidget import CustomGridWidget


class StatusWidget(CustomGridWidget):
    def __init__(self, window: Tk) -> None:
        super().__init__(window)
        self.__initialText = "Click Scrape to Start"
        self.__statusText = StringVar()
        self.__statusText.set(self.__initialText)
        self.__statusLabel = Label(self._frame, textvariable=self.__statusText,
                                   anchor=LEFT_ALIGN,
                                   width=DEFAULT_ROW_WIDTH+11)
        self.__statusLabel.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._incrementAndGetRow(), column=0)

        self.__progressBar = Progressbar(
            self._frame, orient=HORIZONTAL, length=50, mode='indeterminate')

    def startLoading(self):
        self.__progressBar.grid(row=self._row, column=1, sticky='E')
        self.__progressBar.anchor('e')
        self.__progressBar.start()

    def finishLoading(self):
        self.__progressBar.stop()
        self.__progressBar.grid_remove()

    def updateStatusReadout(self, text: str):
        self.__statusText.set(text)
