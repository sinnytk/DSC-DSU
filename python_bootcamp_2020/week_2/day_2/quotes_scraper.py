from typing import Dict
import requests
from bs4 import BeautifulSoup
from csv import DictWriter

def return_raw_html(url):
    res = requests.get(url)
    return res.content.decode()

def scrap_quotes():
    base_url = "https://quotes.toscrape.com/"
    page_url = ""
    output = []
    while(True):
        print(page_url)
        content = return_raw_html(base_url+page_url)
        soup = BeautifulSoup(content,'html.parser')
        quotes = soup.select(".quote")
        for quote in quotes:
            quote_text= quote.select_one('span[itemprop="text"]').text
            quote_author= quote.select_one('small[itemprop="author"]').text
            output.append({"text":quote_text, "author":quote_author})
        page_url_raw = soup.select_one("li.next a")
        if page_url_raw == None:
            break
        page_url = page_url_raw['href']
    return output

def main():
    quotes = scrap_quotes()
    with open("quotes.csv","w") as file:
        writer = DictWriter(file, fieldnames=["author","text"])
        writer.writeheader()
        for q in quotes:
            writer.writerow(q)
if __name__ == "__main__":
    main()