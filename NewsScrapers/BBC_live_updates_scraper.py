from bs4 import BeautifulSoup
import requests

url = "https://www.bbc.com/sport/football/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
elements = soup.find_all("li",class_="ssrcss-rs7w2i-ListItem e1gp961v0")
counter = 0
for element in elements:
    a_tag = element.find("a")
    link = (f"https://bbc.com{a_tag['href']}")
    
    if "live" in link:
        live_link = requests.get(link)
        live_soup = BeautifulSoup(live_link.text,"html.parser")
        sources = live_soup.find_all("article", class_="ssrcss-1qgzj2j-ContentPost e6wdqbx1")
        for source in sources:
            print(source.text)
            print("")



    