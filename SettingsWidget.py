from tkinter import Tk, Button, Label, Entry, Frame, filedialog
from Settings import Settings
from constants import DEFAULT_ROW_WIDTH, PADDING_Y_SMALL, PADDING_X_SMALL, LEFT_ALIGN
from CustomGridWidget import CustomGridWidget


class SettingsWidget(CustomGridWidget):

    def __init__(self, window: Tk):
        super().__init__(window)
        # Render Settings widget
        self.__settings = Settings()

        # Login Page URL Input
        Label(self._frame, width=DEFAULT_ROW_WIDTH, anchor=LEFT_ALIGN, text="Login Page URL:").grid(
            sticky=LEFT_ALIGN,
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._incrementAndGetRow(), column=0)
        self.__loginPageURLEntry = Entry(self._frame)
        self.__loginPageURLEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)
        self.__loginPageURLEntry.insert(0, self.__settings.loginPageURL)

        # Login Asset Input
        Label(self._frame, text="Login Asset URL:").grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            sticky=LEFT_ALIGN,
            row=self._incrementAndGetRow(), column=0)
        self.__loginAssetURLEntry = Entry(self._frame)
        self.__loginAssetURLEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)
        self.__loginAssetURLEntry.insert(0, self.__settings.loginAssetURL)

        # Browser Driver Input
        Button(self._frame, text="Get Browser Driver Executable",
               command=self.__getBrowserDriverExecutableFilePath
               ).grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            sticky=LEFT_ALIGN,
            row=self._incrementAndGetRow(), column=0)
        self.__browserFilePathEntry = Entry(self._frame)
        self.__browserFilePathEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)
        self.__browserFilePathEntry.insert(
            0, self.__settings.browserDriverPath)

        # File Extension Input
        Label(self._frame, anchor=LEFT_ALIGN, text="File Extension:", width=DEFAULT_ROW_WIDTH).grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            sticky=LEFT_ALIGN,
            row=self._incrementAndGetRow(), column=0)
        self.__fileExtensionEntry = Entry(self._frame)
        self.__fileExtensionEntry.grid(
            pady=PADDING_Y_SMALL, padx=PADDING_X_SMALL,
            row=self._row, column=1)
        self.__fileExtensionEntry.insert(
            0, self.__settings.fileExtension)

    def getWidget(self):
        self.__settings.saveConfigFile()
        return self._frame

    def getAndSaveSettings(self):
        self.__getSettingsFromEntries()  # Update settings object
        self.__settings.saveConfigFile()  # Save Settings
        return self.__settings.loginPageURL, self.__settings.browserDriverPath, self.__settings.fileExtension

    # Internal functions
    def __getSettingsFromEntries(self):
        self.__settings.browserDriverPath = self.__browserFilePathEntry.get()
        self.__settings.loginPageURL = self.__loginPageURLEntry.get()
        self.__settings.loginAssetURL = self.__loginAssetURLEntry.get()
        self.__settings.fileExtension = self.__fileExtensionEntry.get()

    def __getBrowserDriverExecutableFilePath(self):
        self.__settings.browserDriverPath = filedialog.askopenfilename()
        self.__browserFilePathEntry.delete(0, 'end')
        self.__browserFilePathEntry.insert(
            0, self.__settings.browserDriverPath)
