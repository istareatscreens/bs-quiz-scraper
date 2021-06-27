from CustomGridWidget import CustomGridWidget
from tkinter import Tk, Button, Label, Entry, Frame, filedialog
from tkinter.constants import LEFT, SUNKEN
from constants import LEFT_ALIGN, PADDING_X_SMALL, PADDING_Y_SMALL, DEFAULT_ROW_WIDTH


class ScraperWidget(CustomGridWidget):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.folderPath = ""

        # Marking Page URL Input
        Label(self._frame, anchor=LEFT_ALIGN, text="Marking Page URL:", width=DEFAULT_ROW_WIDTH).grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            sticky=LEFT_ALIGN,
            row=self._incrementAndGetRow(), column=0)
        self.__markingPageURLEntry = Entry(self._frame)
        self.__markingPageURLEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)

        # Output Directory Input
        Button(self._frame, text="Select Output Directory",
               command=self.__getOutputPath
               ).grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            sticky=LEFT_ALIGN,
            row=self._incrementAndGetRow(), column=0)
        self.__outputDirectoryEntry = Entry(self._frame)
        self.__outputDirectoryEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)

    def getScraperWidget(self):
        return self._frame

    # internal functions
    def __getOutputPath(self):
        self.folderPath = filedialog.askdirectory()
        self.__browserFilePathEntry.insert(
            0, self.folderPath)
