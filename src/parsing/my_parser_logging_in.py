from requests import Session  # Easy save cookies
from bs4 import BeautifulSoup
from time import sleep


# There are cases when we cannot parse a site without logging in.
# For such cases we use POST authorization.
# Cookies are history of actions of a user on a site.

headers = {"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

work = Session()  # Our cookies will be here
work.get("https://quotes.toscrape.com/", headers=headers)  # Imitating human getting on a site

response = work.get("https://quotes.toscrape.com/login", headers=headers)  # Open login page

soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find("input").get("value")  # store here csrf token
data = {"csrf_token": token, "username": "noname", "password": "password"}
result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

#if result.text.__contains__("Logot"):  # we can be sure that we logged in on a site if there is "Logout" word here.
#    print("Successfully logged in.")
#else:
#    print("Could not login.")


# *** A way to parse a site with unknown number of pages *** #

#for i in range(1, 1000):
i = 0
while True:
    i += 1
    resp = work.get(f"https://quotes.toscrape.com/page/{i}/", headers=headers)
    soup_2 = BeautifulSoup(resp.text, "lxml")
    quotes = soup_2.find_all("div", "quote")
    if len(quotes) != 0:  	# when 'quotes' is equal to '0' (empty) it means that there is no quotes left to parse. 
        for j in quotes:
            text = j.find("span", "text").text
            author = j.find("small", "author").text
            print(text + "\n" + author + "\n\n")
    else:
        break
