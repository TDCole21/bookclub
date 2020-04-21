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
from pandemic_home import pandemic_game_setup, pandemic_home, pandemic_outbreak, pandemic_draw_card, pandemic_use_card, pandemic_shareknowledge, pandemic_changerole
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
    Epidemics=PandemicHome[1]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])

    return render_template("pandemic/pandemic_home.html", name="Pandemic: Home", In_Play=In_Play, Epidemics=Epidemics, Players=Players)

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

@app.route('/pandemic/Nick/home', methods=['GET', 'POST']) 
def __pandemic_Nick_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    
    return render_template("pandemic/"+In_Play[1][0]+".html", name="Pandemic: "+In_Play[1][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/Nick/drawcard', methods=['GET', 'POST']) 
def __pandemic_Nick_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Nick_home__'))

@app.route('/pandemic/Nick/usecard', methods=['GET', 'POST']) 
def __pandemic_Nick_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Nick_home__'))

@app.route('/pandemic/Nick/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_Nick_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Nick_home__'))

@app.route('/pandemic/Nick/changerole', methods=['GET', 'POST']) 
def __pandemic_Nick_changerole__():
    pandemic_changerole()
    return redirect(url_for('__pandemic_Nick_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC JAMES     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/James/home', methods=['GET', 'POST']) 
def __pandemic_James_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    return render_template("pandemic/"+In_Play[2][0]+".html", name="Pandemic: "+In_Play[2][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/James/drawcard', methods=['GET', 'POST']) 
def __pandemic_James_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_James_home__'))

@app.route('/pandemic/James/usecard', methods=['GET', 'POST']) 
def __pandemic_James_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_James_home__'))

@app.route('/pandemic/James/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_James_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_James_home__'))

@app.route('/pandemic/James/changerole', methods=['GET', 'POST']) 
def __pandemic_James_changerole__():
    pandemic_changerole()
    return redirect(url_for('__pandemic_James_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC CAL     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/Cal/home', methods=['GET', 'POST']) 
def __pandemic_Cal_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    return render_template("pandemic/"+In_Play[3][0]+".html", name="Pandemic: "+In_Play[3][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/Cal/drawcard', methods=['GET', 'POST']) 
def __pandemic_Cal_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cal_home__'))

@app.route('/pandemic/Cal/usecard', methods=['GET', 'POST']) 
def __pandemic_Cal_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cal_home__'))

@app.route('/pandemic/cal/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_Cal_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Cal_home__'))

@app.route('/pandemic/cal/changerole', methods=['GET', 'POST']) 
def __pandemic_Cal_changerole__():
    pandemic_changerole()
    return redirect(url_for('__pandemic_Cal_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC COLE     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/Cole/home', methods=['GET', 'POST']) 
def __pandemic_Cole_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    return render_template("pandemic/"+In_Play[0][0]+".html", name="Pandemic: "+In_Play[0][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/Cole/drawcard', methods=['GET', 'POST']) 
def __pandemic_Cole_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cole_home__'))

@app.route('/pandemic/Cole/usecard', methods=['GET', 'POST']) 
def __pandemic_Cole_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cole_home__'))

@app.route('/pandemic/Cole/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_Cole_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Cole_home__'))

@app.route('/pandemic/Cole/changerole', methods=['GET', 'POST']) 
def __pandemic_Cole_changerole__():
    pandemic_changerole()
    return redirect(url_for('__pandemic_Cole_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC CUNT     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/Cunt/home', methods=['GET', 'POST']) 
def __pandemic_Cunt_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    return render_template("pandemic/"+In_Play[4][0]+".html", name="Pandemic: "+In_Play[4][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/Cunt/drawcard', methods=['GET', 'POST']) 
def __pandemic_Cunt_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Cunt_home__'))

@app.route('/pandemic/Cunt/usecard', methods=['GET', 'POST']) 
def __pandemic_Cunt_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Cunt_home__'))

@app.route('/pandemic/Cunt/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_Cunt_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Cunt_home__'))

@app.route('/pandemic/Cunt/changerole', methods=['GET', 'POST']) 
def __pandemic_Cunt_changerole__():
    pandemic_changerole()
    return redirect(url_for('__pandemic_Cunt_home__'))


######################################################################################################################################################################
###########################################################################     PANDEMIC HARRY     ####################################################################
######################################################################################################################################################################

@app.route('/pandemic/Harry/home', methods=['GET', 'POST']) 
def __pandemic_Harry_home__():
    PandemicHome=pandemic_home()
    Roles=PandemicHome[0]
    Players=PandemicHome[2]
    In_Play=[]
    for i in range(len(Players)):
        In_Play.append(PandemicHome[i+3])
    return render_template("pandemic/"+In_Play[5][0]+".html", name="Pandemic: "+In_Play[5][0], In_Play=In_Play, Players=Players, Roles=Roles)


@app.route('/pandemic/Harry/drawcard', methods=['GET', 'POST']) 
def __pandemic_Harry_draw_card__():
    pandemic_draw_card()
    return redirect(url_for('__pandemic_Harry_home__'))

@app.route('/pandemic/Harry/usecard', methods=['GET', 'POST']) 
def __pandemic_Harry_use_card__():
    pandemic_use_card()
    return redirect(url_for('__pandemic_Harry_home__'))

@app.route('/pandemic/Harry/shareknowledge', methods=['GET', 'POST']) 
def __pandemic_Harry_shareknowledge__():
    pandemic_shareknowledge()
    return redirect(url_for('__pandemic_Harry_home__'))

@app.route('/pandemic/Harry/changerole', methods=['GET', 'POST']) 
def __pandemic_Harry_changerole__():
    pandemic_changerole()
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
    Players=PandemicHome[2]
    return render_template("pandemic/rules.html", name="Pandemic Rules", Actions=Actions, Roles=Roles, Players=Players)


######################################################################################################################################################################
###########################################################################     PANDEMIC PLAYER CARDS     ############################################################
######################################################################################################################################################################

@app.route('/pandemic/playercards', methods=['GET', 'POST']) 
def __pandemic_playercards__():
    PandemicPlayerCards=pandemic_playercards_discard()
    PlayerCardsDiscardPile=PandemicPlayerCards
    PandemicHome=pandemic_home()
    Players=PandemicHome[2]
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
    Players=PandemicHome[2]
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
