import requests
import pandas as pd
import numpy as np
import webbrowser
import pyperclip
import pyautogui as pg

from time import sleep
from bs4 import BeautifulSoup
from typing import List, Literal


# variables ----------------------------
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}


def get_html_content(url: str) -> BeautifulSoup:
    """
    Get the HTML content of given url(webpage) using requests library 
    as an object of Beautiful Soup Library

    Args:
        url (str): url of the webpage, example: https://www.example.com/

    Returns:
        BeautifulSoup: Object of Library bs4
    """

    webpage: str = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage)

    return soup


def scrape_github_searching_webpage(
        urls: List[str], 
        path: str,
        last_page_count: int,
        initial_waiting_time: float = 3,
        inspect_waiting_time: float = 3,
        first_page_count: int = 1,
        tab_closing_waiting_time: float = 1,
        verbose: bool = False
        ) -> None:

    """
    Scrape the GitHub searching webpage for the given urls and save the results in the given folder.
    1 Webpage = 1 file

    Args:

    Return:

    """

    
    sleep(initial_waiting_time) # waiting before starting main code

    # loop for each url
    for url_no,url in enumerate(urls):

        # loop for each webpage in given pages range
        for page_no in range(first_page_count,last_page_count+1):

            # updating the url page number
            updated_url = url.replace(f"__page_no__", str(page_no))

            # openning the browser with desired url
            webbrowser.open(updated_url)
            # openning inspect element of suitable webpage
            pg.hotkey('ctrl','shift','i')
            # waiting for inspect element to open
            sleep(inspect_waiting_time)
            # copy the all body tag HTML
            pg.hotkey('ctrl','c')
            # exiting the tab
            pg.hotkey('ctrl','w')
            # waiting for tab to close
            sleep(tab_closing_waiting_time)

            # extracting the copied HTML content as string
            content = pyperclip.paste()
            # generating file name
            file_name = f"Webpage {url_no+1} {page_no}"

            # saving webpage content as a HTML file
            with open(f"{path}\\{file_name}.html", 'w', encoding='utf-8') as f:
                f.write(content)

            if (verbose):
                print(f"File '{file_name}' saved successfully.")



