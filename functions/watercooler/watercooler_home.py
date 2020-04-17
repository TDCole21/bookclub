from flask import Flask, render_template, request, redirect, url_for
import os
import re
import datetime
from calendar import monthrange

app = Flask(__name__) #__name__ is for best practice

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def last_weekday(d, weekday):
    cmon = d.month

    last_thursday = d
    while d.month == cmon:
        d += datetime.timedelta(days=1)
        if d.weekday()==weekday: #this is Thursday 
            last_thursday = d
    return last_thursday

def home_home():
    books_temp=[]
    Books=[]
    books_file = open("./data/watercooler/Books.txt", "r")
    for x in books_file:
        books_temp.extend(x.split(";"))
    for i in books_temp:
        Books.append(i.split(":"))
    books_file.close()

    del Books[-1]

    games_temp=[]
    Games=[]
    games_file = open("./data/watercooler/Games.txt", "r")
    for x in games_file:
        games_temp.extend(x.split(";"))
    for i in games_temp:
        Games.append(i.split(":"))
    games_file.close()

    del Games[-1]

    films_temp=[]
    Films=[]
    films_file = open("./data/watercooler/Films.txt", "r")
    for x in films_file:
        films_temp.extend(x.split(";"))
    for i in films_temp:
        Films.append(i.split(":"))
    films_file.close()

    del Films[-1]

    tvshows_temp=[]
    TVShows=[]
    tvshows_file = open("./data/watercooler/TVShows.txt", "r")
    for x in tvshows_file:
        tvshows_temp.extend(x.split(";"))
    for i in tvshows_temp:
        TVShows.append(i.split(":"))
    tvshows_file.close()

    del TVShows[-1]

    books_choice = []
    games_choice = []
    films_choice = []
    tvshows_choice = []

    for i in Books:
        if int(i[2])==1:
            books_choice.append(i)
    
    if len(books_choice) == 0:
        books_choice.append(["None Selected", "None Selected", "None Selected"])

    for i in Games:
        if int(i[3])==1:
            games_choice.append(i)
    
    if len(games_choice) == 0:
        games_choice.append(["None Selected", "None Selected", "None Selected"])

    for i in Films:
        if int(i[3])==1:
            films_choice.append(i)
    
    if len(films_choice) == 0:
        films_choice.append(["None Selected", "None Selected", "None Selected"])

    for i in TVShows:
        if int(i[3])==1:
            tvshows_choice.append(i)
    
    if len(tvshows_choice) == 0:
        tvshows_choice.append(["None Selected", "None Selected", "None Selected"])

    d = datetime.date.today()
    next_thursday = next_weekday(d, 3).strftime('%A %d %B, %Y')
    last_thursday = last_weekday(d, 3).strftime('%A %d %B, %Y')
    
    return (books_choice, games_choice, films_choice, tvshows_choice, next_thursday, last_thursday)