from bs4 import BeautifulSoup
import requests


url = "https://www.pvas.no/produkter/ammunisjon/rifle"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

data = soup.find_all("div", class_="ProdItem")



for container in data:
    # print(container)
    image_link = container.find("img")["src"]
    print(image_link)
    title = container.find("a", class_="ItemTitleLink")["title"]
    print(title)
    title_link = container.find("a", class_="ItemTitleLink")["href"]
    print(title_link)
    price_string = container.find("span", class_="Price").text
    print(price_string)