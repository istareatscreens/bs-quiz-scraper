from tkinter import Tk, Button, Label, Entry, Frame, filedialog
from tkinter.constants import SUNKEN
from Settings import Settings
from tkinter.font import BOLD


class SettingsWidget:

    def __init__(self, window: Tk):
        # Render Settings widget
        self.__settings = Settings()

        # Style properties
        anchor = 'W'
        padx = 5
        pady = 5

        # Create Frame
        self.__row = -1
        self.__frame = Frame(window, bd=1, relief=SUNKEN)

        # Login Page
        Label(self.__frame, text="Login Page URL:").grid(
            sticky=anchor,
            pady=pady, padx=padx,
            row=self.__incrementAndGetRow(), column=0)
        self.__loginPageURLEntry = Entry(self.__frame)
        self.__loginPageURLEntry.grid(
            pady=pady, padx=padx,
            row=self.__row, column=1)
        self.__loginPageURLEntry.insert(0, self.__settings.loginPageURL)

        # Login Asset
        Label(self.__frame, text="Login Asset URL:").grid(
            pady=pady, padx=padx,
            sticky=anchor,
            row=self.__incrementAndGetRow(), column=0)
        self.__loginAssetURLEntry = Entry(self.__frame)
        self.__loginAssetURLEntry.grid(
            pady=pady, padx=padx,
            row=self.__row, column=1)
        self.__loginAssetURLEntry.insert(0, self.__settings.loginAssetURL)

        # Browser Driver
        Button(self.__frame, text="Get Browser Driver Executable",
               command=self.__getBrowserDriverExecutableFilePath
               ).grid(
            pady=pady, padx=padx,
            sticky=anchor,
            row=self.__incrementAndGetRow(), column=0)
        self.__browserFilePathEntry = Entry(self.__frame)
        self.__browserFilePathEntry.grid(
            pady=pady, padx=padx,
            row=self.__row, column=1)
        self.__browserFilePathEntry.insert(
            0, self.__settings.browserDriverPath)

    def getSettingsWidget(self):
        self.__settings.saveConfigFile()
        return self.__frame

    def getAndSaveSettings(self):
        self.__getSettingsFromEntries()  # Update settings object
        self.__settings.saveConfigFile()  # Save Settings
        return self.__settings

    # Internal functions
    def __incrementAndGetRow(self):
        self.__row += 1
        return self.__row

    def __getSettingsFromEntries(self):
        self.__settings.browserDriverPath = self.__browserFilePathEntry.get()
        self.__settings.loginPageURL = self.__loginPageURLEntry.get()
        self.__settings.loginAssetURL = self.__loginAssetURLEntry.get()

    def __getBrowserDriverExecutableFilePath(self):
        self.__settings.BrowserDriverPath = filedialog.askopenfilename()
        self.__browserFilePathEntry.insert(
            0, self.__settings.browserDriverPath)
