from bs4.element import ResultSet
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
import platform
import time
import traceback

from .xpath_soup import xpath_soup

# Set path seperator based on os
SLASH = "\\" if platform.system() == 'Windows' else "/"


def scrape(markingPageURL,
           outputPath,
           loginPageURL,
           browserDriver,
           fileExtension,
           printToWindow):

    try:
        rootDir = Path(outputPath + SLASH + "output")
        rootDir.mkdir(exist_ok=True)
    except:
        traceback.print_exc()
        printToWindow("Error creating/accessing output directory")

    driver = webdriver.Firefox(executable_path=browserDriver)
    webdriver.support.ui.WebDriverWait(driver, 100000).until(
        lambda d: d.execute_script("return document.readyState") == "complete")
    driver.get(loginPageURL)
    driver.find_element_by_tag_name('a').click()

    # Wait for user login
    printToWindow("Please login")
    wait = WebDriverWait(driver, 1000)
    element = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'd2l-navigation-s-link')))

    # *** Start Scraping ***

    # Initiate scraper

    # Foward to grade quiz page
    driver.get(markingPageURL)

    # Get main page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Get all exam links
    examSubmissions = []
    wait = WebDriverWait(driver, 1000)
    # soup.find_all(class_="d2l-link d2l-link-inline"):
    printToWindow("Loading...")
    for link in __waitUntilLoad("d2l-link d2l-link-inline", lambda element: soup.find_all(class_=element)):
        if len(link.contents) > 0 and (link.contents[0]).find("attempt") != -1:
            examSubmissions.append(link)

    # Go to test link found by beautiful soup and converted to an xpath
    for sub in examSubmissions:
        try:
            link = xpath_soup(sub)
            (__waitUntilLoad(
                link, lambda element: driver.find_element_by_xpath(element).click()))
            __scrapeQuiz(driver, rootDir, fileExtension, printToWindow)
            driver.back()
        except Exception:
            traceback.print_exc()
            printToWindow("ERROR Scraping Page")

    driver.close()


def __convertToString(value):
    # Remove non-ascii characters
    return value if (isinstance(value, str)) else ((value.name.replace('br', '\n').replace(' ', ' ')).encode('UTF-8', 'ignore')).decode('ASCII')


def __waitUntilLoad(element, callback):
    # Used to wait until bs4 or selenium has loaded element
    while True or element == '':
        try:
            result = callback(element)
            if isinstance(result, ResultSet) and len(result) == 0 or result == []:
                continue
            return result
        except:
            time.sleep(0.05)
            continue


def __makeDirectory(path, rootDir, printToWindow):
    outputPath = Path(rootDir._str + SLASH + path)
    try:
        outputPath.mkdir(exist_ok=True)
    except Exception:
        traceback.print_exc()
        printToWindow("Error creating parent directory")
    return outputPath  # return path


def __scrapeQuiz(driver, rootDir, fileExtension, printToWindow):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Wait for page to load
    WebDriverWait(driver, 1000)
    # get student name to make folder
    name = (__waitUntilLoad(
        '/html/body/div[2]/div/div[3]/div/div/div/form/div/table[2]/tbody/tr[1]/td', driver.find_element_by_xpath)).text.replace(':', '').replace('.', '')
    printToWindow("Scrape: " + name)
    print(name)
    workingPath = __makeDirectory(name, rootDir, printToWindow)
    Answers = __waitUntilLoad(
        "drt d2l-htmlblock d2l-htmlblock-untrusted", lambda element: soup.findAll(class_=element))
    questionNum = 1
    altTF = True
    for answer in Answers:
        if len(answer.contents[0]) < 0 or answer.contents[0] == "":
            continue
        value = answer.contents
        # Avoid saving true and false questions
        if value[0] == "True" or value[0] == "False":
            # alternate true and false to deal with both answers appearing
            if altTF:
                questionNum += 1
                altTF = False
                continue
            altTF = True
        else:
            with open(workingPath._str+SLASH+'Question'+str(int(questionNum))+'.'+fileExtension, 'w', encoding='UTF-8') as file:
                questionNum = questionNum+1
                for text in value:
                    file.write(__convertToString(text))
