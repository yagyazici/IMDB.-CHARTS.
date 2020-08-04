from bs4 import BeautifulSoup
import requests
from os import system
from imdbmostpopularmovies import mostpopularmovies
from imdbtopmovies import topmovies
from imdbmostpopulartv import mostpopulartv
from imdbtopseries import topseries
system("cls")

run = True

while run:
    print("IMDb Charts".center(30,"*"))
    print("1-Most Popular Movies\n2-Top Rated Movies\n3-Most Popular Shows\n4-Top Rated Shows")

    choice = input(">")

    if choice == "1":
        system("cls")
        mostpopularmovies()
        print("1-IMDb Charts\n2-Exit")
        choice2 = input(">")
        if choice2 == "1":
            system("cls")
            continue
        elif choice2 == "2":
            system("cls")
            print("Done")
            run = False
    elif choice == "2":
        system("cls")
        topmovies()
        print("1-IMDb Charts\n2-Exit")
        choice2 = input(">")
        if choice2 == "1":
            system("cls")
            continue
        elif choice2 == "2":
            system("cls")
            print("Done")
            run = False
    elif choice == "3":
        system("cls")
        mostpopulartv()
        print("1-IMDb Charts\n2-Exit")
        choice2 = input(">")
        if choice2 == "1":
            system("cls")
            continue
        elif choice2 == "2":
            system("cls")
            print("Done")
            run = False
    elif choice == "4":
        system("cls")
        topseries()
        print("1-IMDb Charts\n2-Exit")
        choice2 = input(">")
        if choice2 == "1":
            system("cls")
            continue
        elif choice2 == "2":
            system("cls")
            print("Done")
            run = False
    else:
        system("cls")
        print("Invalid Choice".center(30,"=").upper())
        continue