from tkinter import PhotoImage, Tk, Button, Label, Entry, Frame
from tkinter.constants import BOTH, DISABLED, NORMAL
import threading
import time

from src.scraper.scraper import scrape
from src.components.SettingsWidget import SettingsWidget
from src.components.ScraperWidget import ScraperWidget
from src.components.StatusWidget import StatusWidget
from src.components.constants import LEFT_ALIGN, PADDING_X_LARGE, PADDING_Y_LARGE


def run():
    # instantiate window
    window = Tk()

    # Load Assets
    icon = PhotoImage(file=r"assets/icon.png")

    # window styling/settings
    window.title("bs-quiz-scraper")
    window.resizable(width=False, height=False)
    window.iconphoto(True, icon)

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
    statusWidget.updateStatusReadout("Starting...")
    runButton.state = DISABLED
    time.sleep(2)  # Wait 2 seconds to prevent accidental double click
    runButton.state = NORMAL
    statusWidget.startLoading()
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
