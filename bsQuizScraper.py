from constants import LEFT_ALIGN, PADDING_X_LARGE, PADDING_Y_LARGE
from tkinter import Tk, Button, Label, Entry, Frame
from tkinter.constants import BOTH, DISABLED, NORMAL
import threading
import time

from scraper import scrape
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
    runButton = Button(window, text="Scrape", font='bold',
                       command=lambda: handleRunButton(scraperWidget, settingsWidget, statusWidget, runButton))
    runButton.pack(
        pady=PADDING_Y_LARGE,
        expand=True)

    window.mainloop()  # render window


def handleRunButton(scraperWidget: ScraperWidget, settingsWidget: SettingsWidget, statusWidget: StatusWidget, runButton):
    runButton.state = NORMAL
    time.sleep(1)  # Wait 2 seconds to prevent accidental double click
    runButton.state = DISABLED
    statusWidget.startLoading()
    # scrape(*(scraperWidget.getSettings()),
    #       *(settingsWidget.getAndSaveSettings()),
    #       statusWidget.updateStatusReadout)
    thread = threading.Thread(target=executeScrape, args=[
        scraperWidget, settingsWidget, statusWidget])
    thread.start()


def executeScrape(scraperWidget: ScraperWidget, settingsWidget: SettingsWidget, statusWidget: StatusWidget):
    scrape(*(scraperWidget.getSettings()),
           *(settingsWidget.getAndSaveSettings()),
           statusWidget.updateStatusReadout)
    statusWidget.finishLoading()


if __name__ == '__main__':
    run()
