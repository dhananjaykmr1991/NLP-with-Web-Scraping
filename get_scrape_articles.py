from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


# Read input data from google sheet
gsheetid = '1D7QkDHxUSKnQhR--q0BAwKMxQlUyoJTQ'
sheet_name = 'Sheet1'
gsheet_url = f"https://docs.google.com/spreadsheets/d/{gsheetid}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(gsheet_url)


def get_scrape_data():
    for i in range(len(df)):
            req = requests.get(df.URL[i])
            print('Scraping...'+df.URL[i]+'\n')
            soup = BeautifulSoup(req.text, "html.parser")

            try:
                if soup.find('div', attrs={'class': 'td-post-content tagdiv-type'}):
                    raw_text = soup.find('div', attrs={'class': 'td-post-content tagdiv-type'})
                    raw_text.pre.decompose()
                    raw_text1 = raw_text.text
                else:
                    raw_text = soup.find('div', attrs={'data-td-block-uid':'tdi_130'})
                    raw_text.pre.decompose()
                    raw_text1 = raw_text.text
            except:
                raw_text1 = ""

            corpus = re.sub("[^0-9a-zA-Z '-.]+", " ", raw_text1
                            ).lower().replace('- ', ' ').replace(' -', ' ')

        # Creating a file for each article and writing it
            filename = f"articles/{df.URL_ID[i]}.txt"
            with open(filename, "w",encoding="utf-8") as file:
                print('Creating & Writing into...'+filename+'\n')
                file.write(corpus)
                file.close()







