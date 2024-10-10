import requests
import pandas as pd
import numpy as np
import webbrowser
import pyperclip
import pyautogui as pg
import re

from os import listdir
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


def scrape_github_user_profile(
        usernames: List[str], 
        path: str,
        initial_waiting_time: float = 3,
        inspect_waiting_time: float = 3,
        tab_closing_waiting_time: float = 1,
        verbose: bool = False
        ) -> None:
    """
    Scraping the HTML content of user(in given users list) profile overview page.
    Afterthat storingall content in an HTML file.

    Args:
        usernames (List[str]): _description_
        path (str): _description_
        initial_waiting_time (float, optional): _description_. Defaults to 3.
        inspect_waiting_time (float, optional): _description_. Defaults to 3.
        tab_closing_waiting_time (float, optional): _description_. Defaults to 1.
        verbose (bool, optional): _description_. Defaults to False.
    """
    
    sleep(initial_waiting_time) # waiting before execution of main code given (n-seconds) 

    # loop for each webpage in given pages range
    for user_no, username in enumerate(usernames):
        # updating the url page number
        url = f"https://github.com/{username}"

        # openning the browser with desired url
        webbrowser.open(url)
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
        file_name = f"User {user_no+1} {username}"

        # saving webpage content as a HTML file
        with open(f"{path}\\{file_name}.html", 'w', encoding='utf-8') as f:
            f.write(content)

        if (verbose):
            print(f"File '{file_name}' saved successfully.")



def  user_profile_html_files_to_csv(
        folder_path: str, 
        end_at_file: int, 
        file_starting_no: int, 
        verbose: bool = True
    ) -> pd.DataFrame:

    """_summary_

    Args:
        folder_path (str): _description_
        verbose (bool): _descripton_

    Returns:
        pd.DataFrame: _description_
    """

    # creating an empty dataframe with suitable schema
    df = pd.DataFrame(columns=['username','gender_pronoun','followings','joining_year','last_year_contributions',
                               'achievements_num', 'email','social_link','social_platform'])
        

    # list of all HTML files
    all_files = listdir(folder_path)

    # checking for valid file number
    if file_starting_no >= end_at_file:
        print("'file_starting_no' must be smaller than 'end_of_file'.")
        return None

    file_no = file_starting_no-1

    # iteration for all users files
    for user_file in all_files:

        # increment in file number
        file_no += 1

        if file_no == end_at_file:
            break

        # creating an empty dataframe with suitable schema
        temp_df = pd.DataFrame(columns=df.columns)
        # initialising file path
        file_path = f"{folder_path}\\{user_file}"
        # extracting HTML content into string format
        with open(file_path, 'r', encoding='utf-8') as file_data:
            content = file_data.read()

        # parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(content, 'lxml')

        # # declaring lists for storing user wise data
        usernames = []

        # --------------------------------------- Extracting values -------------------------------------------------------
        
        # initialising variables that useful in this section only
        char_to_remove: str = ",./\n\\- "

        # extracting the whole sidebar information in a single element
        info_box = soup.find('div',class_="js-profile-editable-replace")

        try:
            # extracting username
            username = soup.find('span',class_='vcard-username').text.strip().split('\n')[0]

            # extracting number of conributions of last year
            last_year_contribution = soup.find('h2', class_='f4 text-normal mb-2').text.strip().split(' ')[0]
            last_year_contribution = int(re.sub(f"[{char_to_remove}]", "", last_year_contribution))

            # extracting joining year
            joining_year = int(soup.find_all('a', class_='js-year-link')[-1].text.strip())

            # extracting followings
            user_followings = soup.find('a', class_="Link--secondary no-underline no-wrap").find('span').text

        except AttributeError:
            print(f"Error in file: {user_file}")
            continue
        
        # extracting user's status
        try:
            status = info_box.find('div', class_="user-status-message-wrapper").text.strip()
        except AttributeError:
            status = np.nan

        # extracting user gender pronoun
        try:
            gender_pronoun = info_box.find('span', itemprop='pronouns').text.replace("\n",'')
        except AttributeError:
            gender_pronoun = np.nan

        # extracting email
        try:
            email = soup.find('li', itemprop='email').text.replace("\n",'')
        except AttributeError:
            email = np.nan

        # extracting url
        try:
            social_link = soup.find('li', itemprop='url').text.replace("\n",'')
        except AttributeError:
            social_link = np.nan
        
        # extracting social platform
        try:
            social_platform = soup.find('li', itemprop='social').text.replace("\n",'')
        except AttributeError:
            social_platform = np.nan
        
        # finding total number of achievements
        try:
            achievement_box = info_box.find_all('a', class_="position-relative")
            achievements_num = 0
            # iteration for each achievement badge
            for achievement_anchor in achievement_box[:int(len(achievement_box)/2)]:
                achievement_cardinality = 1
                try:
                    times = achievement_anchor.find('span').text
                    times = int([*times][-1])
                except AttributeError:
                    times = 1
                # updating total number of achievements
                achievements_num += achievement_cardinality * times

        except AttributeError: 
            # if user has no achievement yet
            achievements_num = 0
            
        # ------------------ Updating values -------------
        usernames.append(username)


        data = {
            'username':usernames,
            'gender_pronoun':gender_pronoun,
            'followings':user_followings,
            'joining_year':joining_year,
            'last_year_contributions':last_year_contribution, 
            'achievements_num':achievements_num,
            'email':email,
            'social_link':social_link,
            'social_platform': social_platform,
            'status': status
        }

        
        temp_df = pd.DataFrame(data)
        df = pd.concat([df,temp_df], ignore_index=True) 

        if (verbose):
            print(f"{file_no+1}) {user_file} - extract successfully")



    return df
        


if __name__ == "__main__":
    print(user_profile_html_files_to_csv("E:\\Python\\Data Collection\\Users", end_at_file=6, file_starting_no=4))
