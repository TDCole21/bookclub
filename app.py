from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import os
import re
import sys

sys.path.insert(1, './functions/')
from books import books_edit, books_home
from films import films_edit, films_home
from games import games_edit, games_home
from tvshows import tvshows_edit, tvshows_home
from users import users_edit, users_home
from home import home_home
from pandemic import pandemic_game_setup, pandemic_home, pandemic_draw_card, pandemic_use_card
sys.path.insert(1, '../..')

app = Flask(__name__) #__name__ is for best practice
mysql = MySQL(app)


#####################################################################################################################################################################
######################################################################    WATERCOOLER HOME     ######################################################################
#####################################################################################################################################################################

@app.route('/')
@app.route('/index')
@app.route('/watercooler/home', methods=['GET', 'POST']) 
def __watercooler_home__():
    home_home()
    books_choice=home_home()[0]   
    games_choice=home_home()[1]   
    films_choice=home_home()[2]   
    tvshows_choice=home_home()[3]   
    return render_template("watercooler/watercooler_home.html", name="Home", books_choice=books_choice, games_choice=games_choice, films_choice=films_choice, tvshows_choice=tvshows_choice)

@app.route('/watercooler/home/books/edit', methods=['GET', 'POST']) # Create function
def __watercooler_home_books_edit__():
    home_books_edit()
    return redirect(url_for('__home_home__'))

@app.route('/watercooler/home/games/edit', methods=['GET', 'POST']) # Create function
def __watercooler_home_games_edit__():
    home_games_edit()
    return redirect(url_for('__home_home__'))

@app.route('/watercooler/home/films/edit', methods=['GET', 'POST']) # Create function
def __watercooler_home_films_edit__():
    home_films_edit()
    return redirect(url_for('__home_home__'))

@app.route('/watercooler/home/tvshows/edit', methods=['GET', 'POST']) # Create function
def __watercooler_home_tvshows_edit__():
    home_tvshows_edit()
    return redirect(url_for('__home_home__'))


######################################################################################################################################################################
###########################################################################    WATERCOOLER BOOKS     ###########################################################################
######################################################################################################################################################################

@app.route('/watercooler/books', methods=['GET', 'POST']) 
def __watercooler_books_home__():
    books_home()
    books_upcoming_selection=books_home()[0]
    users_selection=books_home()[1]
    books_finished_selection=books_home()[2]
    books_chosen_selection=books_home()[3]
    return render_template("watercooler/books.html", name="Books", books_upcoming_selection=books_upcoming_selection, users_selection=users_selection, books_finished_selection=books_finished_selection, books_chosen_selection=books_chosen_selection)

@app.route('/watercooler/books/edit', methods=['GET', 'POST']) # Create function
def __watercooler_books_edit__():
    books_edit()
    return redirect(url_for('__watercooler_books_home__'))



#######################################################################################################################################################################
############################################################################    WATERCOOLER FILMS     ############################################################################
#######################################################################################################################################################################


@app.route('/watercooler/films', methods=['GET', 'POST']) 
def __watercooler_films_home__():
    films_home()
    films_upcoming_selection=films_home()[0]
    users_selection=films_home()[1]
    streaming_platforms_selection=films_home()[2]
    films_finished_selection=films_home()[3]
    films_chosen_selection=films_home()[4]

    return render_template("watercooler/films.html", name="Films", films_upcoming_selection=films_upcoming_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection, films_finished_selection=films_finished_selection, films_chosen_selection=films_chosen_selection)


@app.route('/watercooler/films/edit', methods=['GET', 'POST']) # Create function
def __watercooler_films_edit__():
    films_edit()
    return redirect(url_for('__watercooler_films_home__'))


######################################################################################################################################################################
###########################################################################    WATERCOOLER GAMES     ###########################################################################
######################################################################################################################################################################

@app.route('/watercooler/games', methods=['GET', 'POST']) 
def __watercooler_games_home__():
    games_home()
    games_upcoming_selection=games_home()[0]
    users_selection=games_home()[1]
    consoles_selection=games_home()[2]
    games_finished_selection=games_home()[3]
    games_chosen_selection=games_home()[4]

    return render_template("watercooler/games.html", name="Games", games_upcoming_selection=games_upcoming_selection, consoles_selection=consoles_selection, users_selection=users_selection, games_finished_selection=games_finished_selection, games_chosen_selection=games_chosen_selection)


@app.route('/watercooler/games/edit', methods=['GET', 'POST']) # Create function
def __watercooler_games_edit__():
    games_edit()
    return redirect(url_for('__watercooler_games_home__'))


######################################################################################################################################################################
###########################################################################    WATERCOOLER TVSHOWS     ###########################################################################
######################################################################################################################################################################

@app.route('/watercooler/tvshows', methods=['GET', 'POST']) 
def __watercooler_tvshows_home__():
    tvshows_home()
    tvshows_upcoming_selection=tvshows_home()[0]
    users_selection=tvshows_home()[1]
    streaming_platforms_selection=tvshows_home()[2]
    tvshows_finished_selection=tvshows_home()[3]
    tvshows_chosen_selection=tvshows_home()[4]

    return render_template("watercooler/tvshows.html", name="TV Shows", tvshows_upcoming_selection=tvshows_upcoming_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection, tvshows_finished_selection=tvshows_finished_selection, tvshows_chosen_selection=tvshows_chosen_selection)


@app.route('/watercooler/tvshows/edit', methods=['GET', 'POST']) # Create function
def __watercooler_tvshows_edit__():
    tvshows_edit()
    return redirect(url_for('__watercooler_tvshows_home__'))


######################################################################################################################################################################
###########################################################################     USERS     ###########################################################################
######################################################################################################################################################################

@app.route('/users', methods=['GET', 'POST']) 
def __users_home__():
    users_home()
    users_selection=users_home()
    return render_template("users.html", name="Users", users_selection=users_selection)


@app.route('/users/edit', methods=['GET', 'POST']) # Create function
def __users_edit__():
    users_edit()
    return redirect(url_for('__users_home__'))

######################################################################################################################################################################
###########################################################################     PANDEMIC HOME     ###########################################################################
######################################################################################################################################################################

@app.route('/pandemic/home', methods=['GET', 'POST']) 
def __pandemic_home__():
    PandemicHome=pandemic_home()
    James=PandemicHome[0]
    Cole=PandemicHome[1]
    Nick=PandemicHome[2]
    Cal=PandemicHome[3]
    Deck=PandemicHome[4]

    return render_template("pandemic/pandemic_home.html", name="Pandemic", Nick=Nick, Cole=Cole, Cal=Cal, James=James, Deck=Deck)


@app.route('/pandemic/home/newgame', methods=['GET', 'POST']) 
def __pandemic_newgame__():
    pandemic_game_setup()
    return redirect(url_for('__pandemic_home__'))

@app.route('/pandemic/home/drawcard', methods=['GET', 'POST']) 
def __pandemic_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_home__'))

@app.route('/pandemic/home/usecard', methods=['GET', 'POST']) 
def __pandemic_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_home__'))


#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
