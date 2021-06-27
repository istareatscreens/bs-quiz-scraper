from tkinter import Tk, Button, Label, Entry, Frame

from Settings import Settings
from SettingsWidget import SettingsWidget


def run():
    window = Tk()  # instantiate window
    # window styling
    window.title("bs-quiz-scraper")
    # Settings Pane
    Label(window, text="Settings").pack(
        padx=10,
        anchor="w")
    settingsWidget = SettingsWidget(window)
    settingsWidget.getSettingsWidget().pack(
        padx=10)

    window.mainloop()  # render window


if __name__ == '__main__':
    run()
