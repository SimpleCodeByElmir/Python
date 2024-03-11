import requests
from bs4 import BeautifulSoup
from time import sleep


# Collect info about all product-cards from the site from each page.

headers = {"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}


# Download images

def download(url):
    resp = requests.get(url, stream=True)  # "stream" coz pages can have a big size and we don't need to download them
    r = open("/home/elmir/python_projects/parsing/artifacts/images/" + url.split("/")[-1], "wb")  # "wb" - write bytes;
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()
    

def get_url():
    for i in range(1, 7):

        url = f"https://scrapingclub.com/exercise/list_basic/?page={i}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")  # html to readable format by 'lxml' parser
        data = soup.find_all("div", "w-full rounded border")  # all found 'div' objects
        #print(data)

        for j in data:
            fall_in_card = "https://scrapingclub.com" + j.find("a").get("href")
            yield fall_in_card


def array():
    for k in get_url():

        response = requests.get(k, headers=headers)
        #sleep(3)  # stop for 3 secs

        soup = BeautifulSoup(response.text, "lxml")  # html to readable format by 'lxml' parser
        data = soup.find("div", "my-8 w-full rounded border")  # firts found 'div' object

        name = data.find("h3", "card-title").text
        price = data.find("h4", "my-4 card-price").text
        description = data.find("p", "card-description").text
        card_image_url = "https://scrapingclub.com" + data.find("img", "card-img-top").get("src")
        download(card_image_url)
        yield name, price, description, card_image_url

