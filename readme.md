# bs-quiz-scraper

Cross platform Brightspace (LMS) quiz scraper made for plagarism analysis writen in python3 using BS4, Selenium and tkinter.

Pulls all non-true/false questions as individual files with a specified file extension to a specified output directory for a specified quiz on brightspace LMS.

## Instructions

### General Notes

- **Do not minimize the browser while it is running. It will stop scraping!**
- If you click start and you messed something up just close and reopen it

### Binary

Download it from releases and run it

### Command Prompt:

Using a terminal opened in the project directory run the following commands:

For Mac/Linux:

```
pip install virtualenv
python venv ./venv
source ./venv/Scripts/activate
pip install
python bsQuizScraper.py
```

For Windows:

```
pip install virtualenv
python venv .\venv #windows
start .\venv\Scripts\activate.bat
#In newly launched cmd window run:
pip install
python bsQuizScraper.py
```

### Build Instructions

1. cd to project directory then run:

```
pip install pyinstaller
pip install -r requirements.txt
```

2. to create binary run:

```
pyinstaller --onefile --windowed .\bsQuizScraper.spec
```

3. you can find the .exe file in the dist file

### Run Instructions

![Interface Explanation](./docs/InterfaceExplanation.PNG)

#### Browser Driver Executables

I recommend using Mozillas GeckoDriver it is what this program was tested with. You can download the executable from:

https://github.com/mozilla/geckodriver/releases

Driver can be loaded from menu location is saved by config file
