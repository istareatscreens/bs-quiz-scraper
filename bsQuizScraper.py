from tkinter import Tk, Button, Label, Entry, Frame
from tkinter.constants import BOTH

from Settings import Settings
from SettingsWidget import SettingsWidget
from ScraperWidget import ScraperWidget


def run():
    window = Tk()  # instantiate window
    window.resizable(width=False, height=False)

    # window styling
    window.title("bs-quiz-scraper")
    # Settings Pane
    Label(window, text="Settings").pack(
        padx=10)
    settingsWidget = SettingsWidget(window)
    settingsWidget.getSettingsWidget().pack(
        expand=True,
        fill=BOTH,
        padx=10)

    Label(window, text="Scraper Settings").pack(
        expand=True,
        fill=BOTH,
        padx=10)
    scraperWidget = ScraperWidget(window)
    scraperWidget.getScraperWidget().pack(
        expand=True,
        fill=BOTH,
        padx=10)

    window.mainloop()  # render window


if __name__ == '__main__':
    run()
