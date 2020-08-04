from bs4 import BeautifulSoup
import requests
from os import system

def mostpopulartv():
    url = "https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv"

    html = requests.get(url).content
    soup = BeautifulSoup(html,"html.parser")
    list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit = 250)
    i=0
    for tr in list:
        i += 1
        name = tr.find("td",{"class":"titleColumn"}).find("a").text
        year = tr.find("td",{"class":"titleColumn"}).find("span").text
        rating = tr.find("td",{"class":"ratingColumn imdbRating"}).text
        print(f"{i} {name} {year} {rating}")
        print("="*20)
