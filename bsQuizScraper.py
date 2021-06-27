from constants import LEFT_ALIGN, PADDING_X_LARGE, PADDING_Y_LARGE
from tkinter import Tk, Button, Label, Entry, Frame
from tkinter.constants import BOTH, COMMAND

from Settings import Settings
from SettingsWidget import SettingsWidget
from ScraperWidget import ScraperWidget
from StatusWidget import StatusWidget


def run():
    window = Tk()  # instantiate window

    # window styling/settings
    window.title("bs-quiz-scraper")
    window.resizable(width=False, height=False)

    # Settings Widget
    Label(window, font='bold', anchor=LEFT_ALIGN, text="Settings").pack(
        anchor=LEFT_ALIGN,
        padx=PADDING_X_LARGE)
    settingsWidget = SettingsWidget(window)
    settingsWidget.getWidget().pack(
        expand=True,
        fill=BOTH,
        padx=PADDING_X_LARGE)

    # Scraper Widget
    Label(window, font='bold', text="Scraper Settings").pack(
        anchor=LEFT_ALIGN,
        padx=PADDING_X_LARGE)
    scraperWidget = ScraperWidget(window)
    scraperWidget.getWidget().pack(
        expand=True,
        fill=BOTH,
        padx=PADDING_X_LARGE)

    # Status Widget
    Label(window).pack(
        anchor=LEFT_ALIGN,
        padx=PADDING_X_LARGE)
    statusWidget = StatusWidget(window)
    statusWidget.getWidget().pack(
        expand=True,
        fill=BOTH,
        padx=PADDING_X_LARGE)

    # Run Button
    Button(window, text="Scrape", font='bold',
           ).pack(
        pady=PADDING_Y_LARGE,
        expand=True)

    window.mainloop()  # render window


if __name__ == '__main__':
    run()
