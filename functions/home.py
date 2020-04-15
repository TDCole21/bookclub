from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from data import info
import os
import re
import random
from datetime import datetime, timedelta




app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = os.environ['MYSQL_HOST']
app.config["MYSQL_USER"] = os.environ['MYSQL_USER']
app.config["MYSQL_PASSWORD"] = os.environ['MYSQL_PASSWORD']
app.config["MYSQL_DB"] = os.environ['MYSQL_DB']



mysql = MySQL(app)


######################################################################################################################################################################
###########################################################################     HOME     ###########################################################################
######################################################################################################################################################################


def home_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Books.Books_Name, Users.Users_Name FROM Books INNER JOIN Users ON Books.Users_ID=Users.Users_ID WHERE Books.Books_Finished=1")
    mysql.connection.commit()
    books_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary

    cur.execute("SELECT Games.Games_Name, Users.Users_Name, Consoles.Consoles_Name FROM ((Games INNER JOIN Users ON Games.Users_ID=Users.Users_ID) INNER JOIN Consoles ON Games.Consoles_ID=Consoles.Consoles_ID) WHERE Games.Games_Finished=1")
    mysql.connection.commit()
    games_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary

    cur.execute("SELECT Films.Films_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((Films INNER JOIN Users ON Films.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON Films.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID) WHERE Films.Films_Finished=1")
    mysql.connection.commit()
    films_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary

    cur.execute("SELECT TVShows.TVShows_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((TVShows INNER JOIN Users ON TVShows.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON TVShows.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID) WHERE TVShows.TVShows_Finished=1")
    mysql.connection.commit()
    tvshows_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary

    cur.close()

    books_choice = []
    games_choice = []
    films_choice = []
    tvshows_choice = []

    for row in books_names_chosen:
        books_choice.append(row)
    
    if len(books_choice) == 0:
        books_choice.append(["None Selected", "None Selected", "None Selected"])

    for row in games_names_chosen:
        games_choice.append(row)
    
    if len(games_choice) == 0:
        games_choice.append(["None Selected", "None Selected", "None Selected"])

    for row in films_names_chosen:
        films_choice.append(row)
    
    if len(films_choice) == 0:
        films_choice.append(["None Selected", "None Selected", "None Selected"])

    for row in tvshows_names_chosen:
        tvshows_choice.append(row)
    
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

