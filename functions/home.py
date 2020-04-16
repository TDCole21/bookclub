from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random
# from datetime import datetime, timedelta


app = Flask(__name__) #__name__ is for best practice



######################################################################################################################################################################
###########################################################################     HOME     ###########################################################################
######################################################################################################################################################################


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

    
    
    return (books_choice, games_choice, films_choice, tvshows_choice)

######################################################################################################################################################################
###########################################################################     BOOKS     ###########################################################################
######################################################################################################################################################################


def home_books_edit():
    if request.method == "POST":
        details=request.form
        if details['action'] == 'Shuffle':
            #BOOK SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Books SET Books_Finished = 0 WHERE Books_Finished=1")
            mysql.connection.commit()
            cur.execute("SELECT Books_Name FROM Books WHERE Books_Finished=0")
            mysql.connection.commit()
            books_shuffle = cur.fetchall()


            books_choice = []

            for row in books_shuffle:
                books_choice.append(row)
            
            random.shuffle(books_choice)

            if len(books_choice) != 0:
                cur.execute("UPDATE Books SET Books_Finished = 1 WHERE Books_Name=(%s)",[[books_choice][0][0]])
                mysql.connection.commit()
                cur.close()

        elif details['action'] == 'Finished':
            #BOOK SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Books SET Books_Finished = 2 WHERE Books_Finished=1")
            mysql.connection.commit()
            cur.close()

######################################################################################################################################################################
###########################################################################     Games     ###########################################################################
######################################################################################################################################################################

def home_games_edit():
    if request.method == "POST":
        details=request.form
        if details['action'] == 'Shuffle':
            #GAMES SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Games SET Games_Finished = 0 WHERE Games_Finished=1")
            mysql.connection.commit()
            cur.execute("SELECT Games_Name FROM Games WHERE Games_Finished=0")
            mysql.connection.commit()
            games_shuffle = cur.fetchall()


            games_choice = []

            for row in games_shuffle:
                games_choice.append(row)
            
            random.shuffle(games_choice)

            if len(games_choice) != 0:
                cur.execute("UPDATE Games SET Games_Finished = 1 WHERE Games_Name=(%s)",[[games_choice][0][0]])
                mysql.connection.commit()
                cur.close()


        elif details['action'] == 'Finished':
            #GAMES SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Games SET Games_Finished = 2 WHERE Games_Finished=1")
            mysql.connection.commit()
            cur.close()

######################################################################################################################################################################
###########################################################################     Films     ###########################################################################
######################################################################################################################################################################

def home_films_edit():
    if request.method == "POST":
        details=request.form
        if details['action'] == 'Shuffle':
            #FILMS SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Films SET Films_Finished = 0 WHERE Films_Finished=1")
            mysql.connection.commit()
            cur.execute("SELECT Films_Name FROM Films WHERE Films_Finished=0")
            mysql.connection.commit()
            films_shuffle = cur.fetchall()


            films_choice = []

            for row in films_shuffle:
                films_choice.append(row)
            
            random.shuffle(films_choice)

            if len(films_choice) != 0:
                cur.execute("UPDATE Films SET Films_Finished = 1 WHERE Films_Name=(%s)",[[films_choice][0][0]])
                mysql.connection.commit()
                cur.close()


        elif details['action'] == 'Finished':
            #FILMS SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Films SET Films_Finished = 2 WHERE Films_Finished=1")
            mysql.connection.commit()
            cur.close()

######################################################################################################################################################################
###########################################################################     TVShows     ###########################################################################
######################################################################################################################################################################


def home_tvshows_edit():
    if request.method == "POST":
        details=request.form
        if details['action'] == 'Shuffle':
            #TVSHOWS SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE TVShows SET TVShows_Finished = 0 WHERE TVShows_Finished=1")
            mysql.connection.commit()
            cur.execute("SELECT TVShows_Name FROM TVShows WHERE TVShows_Finished=0")
            mysql.connection.commit()
            tvshows_shuffle = cur.fetchall()


            tvshows_choice = []

            for row in tvshows_shuffle:
                tvshows_choice.append(row)
            
            random.shuffle(tvshows_choice)

            if len(tvshows_choice) != 0:
                cur.execute("UPDATE TVShows SET TVShows_Finished = 1 WHERE TVShows_Name=(%s)",[[tvshows_choice][0][0]])
                mysql.connection.commit()
                cur.close()


        elif details['action'] == 'Finished':
            #TVSHOWS SELECTION#
            cur = mysql.connection.cursor()
            cur.execute("UPDATE TVShows SET TVShows_Finished = 2 WHERE TVShows_Finished=1")
            mysql.connection.commit()
            cur.close()

