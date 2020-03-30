from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from data import info
import os
import re
import sys

sys.path.insert(1, './functions/')
from books import books_create, books_home
from films import films_create, films_home
from games import games_create, games_home
from tvshows import tvshows_create, tvshows_home
from users import users_edit, users_home
from home import home_home
sys.path.insert(1, '../..')

app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = info.MySQLhost
app.config["MYSQL_USER"] = info.MySQLuser
app.config["MYSQL_PASSWORD"] = info.MySQLpassword
app.config["MYSQL_DB"] = info.MySQLdb


mysql = MySQL(app)


######################################################################################################################################################################
############################################################################     HOME     ############################################################################
######################################################################################################################################################################

@app.route('/')
@app.route('/index')
@app.route('/home')
def __home_home__():
    home_home()
    return render_template("home.html", name="Home")


######################################################################################################################################################################
###########################################################################     BOOKS     ###########################################################################
######################################################################################################################################################################

@app.route('/books', methods=['GET', 'POST']) # Read Function
def __books_home__():
    books_home()
    books_upcoming_selection=books_home()[0]
    users_selection=books_home()[1]
    books_finished_selection=books_home()[2]
    return render_template("books.html", name="Books", books_upcoming_selection=books_upcoming_selection, users_selection=users_selection, books_finished_selection=books_finished_selection)

@app.route('/books/create', methods=['GET', 'POST']) # Create function
def __books_create__():
    books_create()
    return redirect(url_for('__books_home__'))



#######################################################################################################################################################################
############################################################################     FILMS     ############################################################################
#######################################################################################################################################################################


@app.route('/films', methods=['GET', 'POST']) # Read Function
def __films_home__():
    films_home()
    films_selection=films_home()[0]
    users_selection=films_home()[1]
    streaming_platforms_selection=films_home()[2]

    return render_template("films.html", name="Films", films_selection=films_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection)


@app.route('/films/create', methods=['GET', 'POST']) # Create function
def __films_create__():
    films_create()
    return redirect(url_for('__films_home__'))


######################################################################################################################################################################
###########################################################################     GAMES     ###########################################################################
######################################################################################################################################################################

@app.route('/games', methods=['GET', 'POST']) # Read Function
def __games_home__():
    games_home()
    games_selection=games_home()[0]
    users_selection=games_home()[1]
    consoles_selection=games_home()[2]

    return render_template("games.html", name="Games", games_selection=games_selection, consoles_selection=consoles_selection, users_selection=users_selection)


@app.route('/games/create', methods=['GET', 'POST']) # Create function
def __games_create__():
    games_create()
    return redirect(url_for('__games_home__'))


######################################################################################################################################################################
###########################################################################     TVSHOWS     ###########################################################################
######################################################################################################################################################################

@app.route('/tvshows', methods=['GET', 'POST']) # Read Function
def __tvshows_home__():
    tvshows_home()
    tvshows_selection=tvshows_home()[0]
    users_selection=tvshows_home()[1]
    streaming_platforms_selection=tvshows_home()[2]

    return render_template("tvshows.html", name="TVShows", tvshows_selection=tvshows_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection)


@app.route('/tvshows/create', methods=['GET', 'POST']) # Create function
def __tvshows_create__():
    tvshows_create()
    return redirect(url_for('__tvshows_home__'))


######################################################################################################################################################################
###########################################################################     USERS     ###########################################################################
######################################################################################################################################################################

@app.route('/users', methods=['GET', 'POST']) # Read Function
def __users_home__():
    users_home()
    users_selection=users_home()
    return render_template("users.html", name="Users", users_selection=users_selection)


@app.route('/users/edit', methods=['GET', 'POST']) # Create function
def __users_edit__():
    users_edit()
    return redirect(url_for('__users_home__'))


#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
