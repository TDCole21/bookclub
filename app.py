from flask import Flask, render_template, request, redirect, url_for, session
import os
import re
import sys

sys.path.insert(1, './functions')
from users import users_edit, users_home
sys.path.insert(1, './functions/watercooler')
from watercooler_books import books_edit, books_home
from watercooler_films import films_edit, films_home
from watercooler_games import games_edit, games_home
from watercooler_tvshows import tvshows_edit, tvshows_home
from watercooler_home import home_home
sys.path.insert(1, './functions/pandemic')
from pandemic_home import pandemic_game_setup, pandemic_home, pandemic_outbreak, pandemic_draw_card, pandemic_use_card, pandemic_shareknowledge
from pandemic_rules import pandemic_rules
from pandemic_infectioncards import pandemic_infectioncards_discard, pandemic_infectioncards_remove, pandemic_infectioncards_infect, pandemic_infectioncards_epidemic, pandemic_infectioncards_recover
from pandemic_playercards import pandemic_playercards_discard, pandemic_playercards_recover
sys.path.insert(1, '../..')

app = Flask(__name__) #__name__ is for best practice


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
    next_thursday=home_home()[4]
    last_thursday=home_home()[5]
    return render_template("watercooler/watercooler_home.html", name="Watercooler: Home", books_choice=books_choice, games_choice=games_choice, films_choice=films_choice, tvshows_choice=tvshows_choice, next_thursday=next_thursday, last_thursday=last_thursday)


######################################################################################################################################################################
###########################################################################    WATERCOOLER BOOKS     #################################################################
######################################################################################################################################################################

@app.route('/watercooler/books', methods=['GET', 'POST']) 
def __watercooler_books_home__():
    books_home()
    books_upcoming_selection=books_home()[0]
    users_selection=books_home()[1]
    books_finished_selection=books_home()[2]
    books_chosen_selection=books_home()[3]
    return render_template("watercooler/books.html", name="Watercooler: Books", books_upcoming_selection=books_upcoming_selection, users_selection=users_selection, books_finished_selection=books_finished_selection, books_chosen_selection=books_chosen_selection)

@app.route('/watercooler/books/edit', methods=['GET', 'POST']) # Create function
def __watercooler_books_edit__():
    books_edit()
    return redirect(url_for('__watercooler_books_home__'))


#######################################################################################################################################################################
############################################################################    WATERCOOLER FILMS     #################################################################
#######################################################################################################################################################################


@app.route('/watercooler/films', methods=['GET', 'POST']) 
def __watercooler_films_home__():
    films_home()
    films_upcoming_selection=films_home()[0]
    users_selection=films_home()[1]
    streaming_platforms_selection=films_home()[2]
    films_finished_selection=films_home()[3]
    films_chosen_selection=films_home()[4]

    return render_template("watercooler/films.html", name="Watercooler: Films", films_upcoming_selection=films_upcoming_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection, films_finished_selection=films_finished_selection, films_chosen_selection=films_chosen_selection)


@app.route('/watercooler/films/edit', methods=['GET', 'POST']) # Create function
def __watercooler_films_edit__():
    films_edit()
    return redirect(url_for('__watercooler_films_home__'))


######################################################################################################################################################################
###########################################################################    WATERCOOLER GAMES     #################################################################
######################################################################################################################################################################

@app.route('/watercooler/games', methods=['GET', 'POST']) 
def __watercooler_games_home__():
    games_home()
    games_upcoming_selection=games_home()[0]
    users_selection=games_home()[1]
    consoles_selection=games_home()[2]
    games_finished_selection=games_home()[3]
    games_chosen_selection=games_home()[4]

    return render_template("watercooler/games.html", name="Watercooler: Games", games_upcoming_selection=games_upcoming_selection, consoles_selection=consoles_selection, users_selection=users_selection, games_finished_selection=games_finished_selection, games_chosen_selection=games_chosen_selection)


@app.route('/watercooler/games/edit', methods=['GET', 'POST']) # Create function
def __watercooler_games_edit__():
    games_edit()
    return redirect(url_for('__watercooler_games_home__'))


######################################################################################################################################################################
###########################################################################    WATERCOOLER TVSHOWS     ###############################################################
######################################################################################################################################################################

@app.route('/watercooler/tvshows', methods=['GET', 'POST']) 
def __watercooler_tvshows_home__():
    tvshows_home()
    tvshows_upcoming_selection=tvshows_home()[0]
    users_selection=tvshows_home()[1]
    streaming_platforms_selection=tvshows_home()[2]
    tvshows_finished_selection=tvshows_home()[3]
    tvshows_chosen_selection=tvshows_home()[4]

    return render_template("watercooler/tvshows.html", name="Watercooler: TV Shows", tvshows_upcoming_selection=tvshows_upcoming_selection, streaming_platforms_selection=streaming_platforms_selection, users_selection=users_selection, tvshows_finished_selection=tvshows_finished_selection, tvshows_chosen_selection=tvshows_chosen_selection)


@app.route('/watercooler/tvshows/edit', methods=['GET', 'POST']) # Create function
def __watercooler_tvshows_edit__():
    tvshows_edit()
    return redirect(url_for('__watercooler_tvshows_home__'))


#####################################################################################################################################################################
###########################################################################     USERS     ###########################################################################
#####################################################################################################################################################################

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
###########################################################################     PANDEMIC HOME     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/home', methods=['GET', 'POST']) 
def __pandemic_home__():
    PandemicHome=pandemic_home()
    Cal=PandemicHome[0]
    Nick=PandemicHome[1]
    James=PandemicHome[2]
    Cole=PandemicHome[3]
    Epidemics=PandemicHome[4]
    Players=PandemicHome[5]

    return render_template("pandemic/pandemic_home.html", name="Pandemic: Home", Nick=Nick, Cole=Cole, Cal=Cal, James=James, Epidemics=Epidemics, Players=Players)

@app.route('/pandemic/home/outbreak', methods=['GET', 'POST']) 
def __pandemic_outbreak__():
    pandemic_outbreak()
    return redirect(url_for('__pandemic_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC NEW GAME     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/home/newgame', methods=['GET', 'POST']) 
def __pandemic_newgame__():
    users_home()
    Users=users_home()
    return render_template("pandemic/newgame.html", name="Pandemic: New Game", Users=Users, Players=Users)

@app.route('/pandemic/home/newgame/start', methods=['GET', 'POST']) 
def __pandemic_newgame_start__():
    pandemic_game_setup()
    return redirect(url_for('__pandemic_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC NICK     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/nick/home', methods=['GET', 'POST']) 
def __pandemic_Nick_home__():
    PandemicNick=pandemic_home()
    Nick=PandemicNick[1]
    Players=PandemicNick[5][:1]+PandemicNick[5][2:]

    return render_template("pandemic/nick.html", name="Pandemic: Nick", Nick=Nick, Players=Players)


@app.route('/pandemic/nick/drawcard', methods=['GET', 'POST']) 
def __pandemic_nick_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Nick_home__'))

@app.route('/pandemic/nick/usecard', methods=['GET', 'POST']) 
def __pandemic_nick_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Nick_home__'))

@app.route('/pandemic/nick/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_nick_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Nick_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC JAMES     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/james/home', methods=['GET', 'POST']) 
def __pandemic_James_home__():
    PandemicJames=pandemic_home()
    James=PandemicJames[2]
    Players=PandemicJames[5][:2]+PandemicJames[5][3:]

    return render_template("pandemic/james.html", name="Pandemic: James", James=James, Players=Players)


@app.route('/pandemic/james/drawcard', methods=['GET', 'POST']) 
def __pandemic_james_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_James_home__'))

@app.route('/pandemic/james/usecard', methods=['GET', 'POST']) 
def __pandemic_james_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_James_home__'))

@app.route('/pandemic/james/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_james_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_James_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC CAL     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/cal/home', methods=['GET', 'POST']) 
def __pandemic_Cal_home__():
    PandemicCal=pandemic_home()
    Cal=PandemicCal[3]
    Players=PandemicCal[5][:3]+PandemicCal[5][4:]

    return render_template("pandemic/cal.html", name="Pandemic: Cal", Cal=Cal, Players=Players)


@app.route('/pandemic/cal/drawcard', methods=['GET', 'POST']) 
def __pandemic_cal_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cal_home__'))

@app.route('/pandemic/cal/usecard', methods=['GET', 'POST']) 
def __pandemic_cal_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cal_home__'))

@app.route('/pandemic/cal/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_cal_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Cal_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC COLE     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/cole/home', methods=['GET', 'POST']) 
def __pandemic_Cole_home__():
    PandemicCole=pandemic_home()
    Cole=PandemicCole[0]
    Players=PandemicCole[5][1:]

    return render_template("pandemic/cole.html", name="Pandemic: Cole", Cole=Cole, Players=Players)


@app.route('/pandemic/cole/drawcard', methods=['GET', 'POST']) 
def __pandemic_cole_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cole_home__'))

@app.route('/pandemic/cole/usecard', methods=['GET', 'POST']) 
def __pandemic_cole_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cole_home__'))

@app.route('/pandemic/cole/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_cole_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Cole_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC CUNT     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/cunt/home', methods=['GET', 'POST']) 
def __pandemic_Cunt_home__():
    PandemicCunt=pandemic_home()
    Cunt="Not Playing"

    return render_template("pandemic/cunt.html", name="Pandemic: Cunt", Cunt=Cunt)


@app.route('/pandemic/cunt/drawcard', methods=['GET', 'POST']) 
def __pandemic_cunt_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cunt_home__'))

@app.route('/pandemic/cunt/usecard', methods=['GET', 'POST']) 
def __pandemic_cunt_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cunt_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC HARRY     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/harry/home', methods=['GET', 'POST']) 
def __pandemic_Harry_home__():
    PandemicHarry=pandemic_home()
    Harry="Not Playing"

    return render_template("pandemic/harry.html", name="Pandemic: Harry", Harry=Harry)


@app.route('/pandemic/harry/drawcard', methods=['GET', 'POST']) 
def __pandemic_harry_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Harry_home__'))

@app.route('/pandemic/harry/usecard', methods=['GET', 'POST']) 
def __pandemic_harry_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Harry_home__'))

######################################################################################################################################################################
###########################################################################     PANDEMIC RULES     ###################################################################
######################################################################################################################################################################

@app.route('/pandemic/rules', methods=['GET', 'POST']) 
def __pandemic_rules__():
    PandemicRules=pandemic_rules()
    Actions=PandemicRules[0]
    Roles=PandemicRules[1]
    PandemicHome=pandemic_home()
    Players=PandemicHome[5]
    return render_template("pandemic/rules.html", name="Pandemic Rules", Actions=Actions, Roles=Roles, Players=Players)


######################################################################################################################################################################
###########################################################################     PANDEMIC PLAYER CARDS     ############################################################
######################################################################################################################################################################

@app.route('/pandemic/playercards', methods=['GET', 'POST']) 
def __pandemic_playercards__():
    PandemicPlayerCards=pandemic_playercards_discard()
    PlayerCardsDiscardPile=PandemicPlayerCards[0]
    Players=PandemicPlayerCards[1]
    return render_template("pandemic/pandemic_playercards.html", name="Pandemic Player Cards", PlayerCardsDiscardPile=PlayerCardsDiscardPile, Players=Players)

@app.route('/pandemic/playercards/recover', methods=['GET', 'POST']) 
def __pandemic_playercards_recover__():
    pandemic_playercards_recover()
    return redirect(url_for('__pandemic_playercards__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC INFECTION CARDS     #########################################################
######################################################################################################################################################################

@app.route('/pandemic/infectioncards', methods=['GET', 'POST']) 
def __pandemic_infectioncards__():
    PandemicInfectionCards=pandemic_infectioncards_discard()
    InfectDiscardPile=PandemicInfectionCards[0]
    InfectRemovedPile=PandemicInfectionCards[1]
    Epidemics=PandemicInfectionCards[2]
    PandemicHome=pandemic_home()
    Players=PandemicHome[5]
    return render_template("pandemic/pandemic_infectioncards.html", name="Pandemic Infection Cards", Players=Players, InfectDiscardPile=InfectDiscardPile, InfectRemovedPile=InfectRemovedPile, Epidemics=Epidemics)

@app.route('/pandemic/infectioncards/remove', methods=['GET', 'POST']) 
def __pandemic_infectioncards_remove__():
    pandemic_infectioncards_remove()
    return redirect(url_for('__pandemic_infectioncards__'))

@app.route('/pandemic/infectioncards/infect', methods=['GET', 'POST']) 
def __pandemic_infectioncards_infect__():
    pandemic_infectioncards_infect()
    return redirect(url_for('__pandemic_infectioncards__'))

@app.route('/pandemic/infectioncards/epidemic', methods=['GET', 'POST']) 
def __pandemic_infectioncards_epidemic__():
    pandemic_infectioncards_epidemic()
    return redirect(url_for('__pandemic_infectioncards__'))

@app.route('/pandemic/infectioncards/recover', methods=['GET', 'POST']) 
def __pandemic_infectioncards_recover__():
    pandemic_infectioncards_recover()
    return redirect(url_for('__pandemic_infectioncards__'))

#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
