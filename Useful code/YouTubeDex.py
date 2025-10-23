# dependencies
import requests
import json
from bs4 import BeautifulSoup


class YouTubeDex:
    def __init__(self):
        pass

    # function that collect json data from web with suitable YouTube channel
    def get_json_data(
            channel_handle: str, 
            save = False,
            file_name = None
        ) -> str | None :

        
        # setting url
        url = f"https://www.youtube.com/@{channel_handle}/videos"
        print(url)

        # setting file name
        if file_name == None:
            file_name = f"{channel_handle}.json"
        else:
            file_name = file_name + ".json"

        # fetching html content
        response = requests.get(url)
        # creating an object of BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # fetching json content
        json_str = soup.find_all('script')[24].text.split(" = ")[1].replace(';','') # this statement may be generate any error in future
        
        if save:
            # saving json content
            with open(file_name,'w', encoding='utf-8') as file:
                file.write(json_str)
        else:
            return json_str


if __name__ == "__main__":
    tseries_data = YouTubeDex.get_json_data("TSeriesBhaktiSagar")

