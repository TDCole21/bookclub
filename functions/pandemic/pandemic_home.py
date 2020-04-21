import random
from flask import Flask, render_template, request, redirect, url_for
import os
import re

######################################################################################################################################################################
#####################################################################    HOME    ##############################################################################
######################################################################################################################################################################

def pandemic_home():
  # Read in Players from Players file
  Players_temp=[]
  Players=[]
  player_hands=[]
  Players_file = open("./data/pandemic/Players.txt", "r")
  for x in Players_file:
    Players_temp.extend(x.split(";"))
    for i in Players_temp:
      Players.append(i.split(":"))
  Players_file.close()

  if len(Players)!=0:
      del Players[-1]

  # Read in Epidemics from Epidemics file
  Epidemics=[]
  Epidemics_temp=[]
  Epidemics_file = open("./data/pandemic/Epidemics.txt", "r")
  for x in Epidemics_file:
    Epidemics_temp.extend(x.split(";"))
    for i in Epidemics_temp:
      Epidemics.append(i.split(":"))
  Epidemics_file.close()

  if len(Epidemics)!=0:
    del Epidemics[-1]

  # Read in Roles from roles file
  Roles=[]
  Roles_temp=[]
  Roles_file = open("./data/pandemic/Roles.txt", "r")
  for x in Roles_file:
    Roles_temp.extend(x.split(";"))
    for i in Roles_temp:
      Roles.append(i.split(":"))
  Roles_file.close()

  if len(Roles)!=0:
    del Roles[-1]

  Roles_Taken=[]
  for i in range(len(Roles)):
    for n in range(len(Players)):
      if Roles[i][0]==Players[n][1]:
        Roles_Taken.append(Roles[i][0])

  Roles_Available=[]
  for i in range(len(Roles)):
    if Roles[i][0] not in Roles_Taken:
      Roles_Available.append(Roles[i])



  player_hands.append(Roles_Available) 
  player_hands.append(Epidemics)
  player_hands.append(Players)

  
  for i in Players:
    temp=[]
    name=i
    file = open("./data/pandemic/"+str(i[0])+".txt", "r")
    for x in file:
      temp.extend(x.split(";"))
      for i in temp:
        name.append(i.split(":"))
    file.close()

    if len(name)!=0:
      del name[-1]
    player_hands.append(name)


  return player_hands

######################################################################################################################################################################
########################################################################    OUTBREAK    ################################################################################
######################################################################################################################################################################

def pandemic_outbreak():
  if request.method == "POST":
    details=request.form
    Epidemics=[]
    Epidemics_temp=[]
    Epidemics_file = open("./data/pandemic/Epidemics.txt", "r")
    for x in Epidemics_file:
      Epidemics_temp.extend(x.split(";"))
      for i in Epidemics_temp:
        Epidemics.append(i.split(":"))
    Epidemics_file.close()

    if len(Epidemics)!=0:
      del Epidemics[-1] 

    if details['action']=="↑":
      Epidemics[0][1]=str(int(Epidemics[0][1])+1)
    elif details['action']=="↓":
      Epidemics[0][1]=str(int(Epidemics[0][1])-1)

    Epidemics_file = open("./data/pandemic/Epidemics.txt", "w")
    for i in range(len(Epidemics)):
      Epidemics_file.write(Epidemics[i][0]+":"+Epidemics[i][1]+":"+Epidemics[i][2]+";")
    Epidemics_file.close()

  
######################################################################################################################################################################
##################################################################    NEW GAME    #########################################################################
######################################################################################################################################################################


def pandemic_game_setup():
  if request.method == "POST":
    details=request.form

    # Convert difficulty into number of Epidemic cards
    Difficulty=details['difficulty']
    if Difficulty == "No Threat":
      Difficulty=0
    elif Difficulty == "Introduction":
      Difficulty=1
    elif Difficulty == "Easy":
      Difficulty=2
    elif Difficulty == "Moderate":
      Difficulty=3
    elif Difficulty == "Normal":
      Difficulty=4
    elif Difficulty == "Advanced":
      Difficulty=5
    elif Difficulty == "Expert":
      Difficulty=6

    # Resetting gameboard
    Epidemics_file = open("./data/pandemic/Epidemics.txt", "w")
    Epidemics_file.write("0:0:"+str(Difficulty)+";")
    Epidemics_file.close()


     # Read in Cities from cities file
    Cities=[]
    Cities_temp=[]
    Cities_file = open("./data/pandemic/Cities.txt", "r")
    for x in Cities_file:
      Cities_temp.extend(x.split(";"))
      for i in Cities_temp:
        Cities.append(i.split(":"))
    Cities_file.close()

    if len(Cities)!=0:
      del Cities[-1] 


    # Read in Events from events file
    Events=[]
    Events_temp=[]
    Events_file = open("./data/pandemic/Events.txt", "r")
    for x in Events_file:
      Events_temp.extend(x.split(";"))
      for i in Events_temp:
        Events.append(i.split(":"))
    Events_file.close()

    if len(Events)!=0:
      del Events[-1]   

    # Read in Roles from roles file
    Roles=[]
    Roles_temp=[]
    Roles_file = open("./data/pandemic/Roles.txt", "r")
    for x in Roles_file:
      Roles_temp.extend(x.split(";"))
      for i in Roles_temp:
        Roles.append(i.split(":"))
    Roles_file.close()

    if len(Roles)!=0:
      del Roles[-1]  
      random.shuffle(Roles)


    # Read all possible Users from users file
    Users=[]
    Users_temp=[]
    Users_file = open("./data/Users.txt", "r")
    for x in Users_file:
      Users_temp.extend(x.split(";"))
      for i in Users_temp:
        Users.append(i.split(":"))
    Users_file.close()

    if len(Users)!=0:
      del Users[-1]   

    for n in range(len(Users)):
      if os.path.exists("./data/pandemic/"+str(Users[n][0])+".txt"):
        os.remove("./data/pandemic/"+str(Users[n][0])+".txt")
      # if os.path.exists("./templates/pandemic/"+str(Users[n][0])+".html"):
      #   os.remove("./templates/pandemic/"+str(Users[n][0])+".html")



    # Reset Deck/Hands
    Players=details.getlist('players')
    PlayerCards_Deck=open("./data/pandemic/PlayerCards_Deck.txt", "w")

    PlayerCards_Discard=open("./data/pandemic/PlayerCards_Discard.txt", "w")
    PlayerCards_Discard.close()

    InfectionCards_Deck=open("./data/pandemic/InfectionCards_Deck.txt", "w")
    for i in range(len(Cities)):
      InfectionCards_Deck.write(Cities[i][0]+":"+Cities[i][1]+":"+Cities[i][2]+";")
    InfectionCards_Deck.close()

    InfectionCards_Discard=open("./data/pandemic/InfectionCards_Discard.txt", "w")
    InfectionCards_Discard.close()

    InfectionCards_Removed=open("./data/pandemic/InfectionCards_Removed.txt", "w")
    InfectionCards_Removed.close()


    # Write Players.txt
    Players_file=open("./data/pandemic/Players.txt", "w")
    for i in range(len(Players)):
      Players_file.write(Players[i]+":"+Roles[i][0]+":"+Roles[i][1]+";")
    Players_file.close()



    Start_PlayerCards_Deck=[]
    temp=[]



    Start_PlayerCards_Deck.extend(Cities)
    Start_PlayerCards_Deck.extend(Events) # puts the cities and event cards into the playercards_deck

    random.shuffle(Start_PlayerCards_Deck)

    number_of_players=len(Players)
    deck_size=len(Start_PlayerCards_Deck)

    if number_of_players>=4:
      for n in range(len(Players)):
        Players[n]=open("./data/pandemic/"+Players[n]+".txt", "w")
        for i in range(n,number_of_players*2,number_of_players):
          Players[n].write(Start_PlayerCards_Deck[i][0]+":"+Start_PlayerCards_Deck[i][1]+":"+Start_PlayerCards_Deck[i][2]+";")
        Players[n].close()
      del Start_PlayerCards_Deck[0:(number_of_players*4)-1]

    elif number_of_players==3:
      for n in range(len(Players)):
        Players[n]=open("./data/pandemic/"+Players[n]+".txt", "w")
        for i in range(n,number_of_players*3,number_of_players):
          Players[n].write(Start_PlayerCards_Deck[i][0]+":"+Start_PlayerCards_Deck[i][1]+":"+Start_PlayerCards_Deck[i][2]+";")
        Players[n].close()
      del Start_PlayerCards_Deck[0:(number_of_players*4)-1]

    elif number_of_players==2:
      for n in range(len(Players)):
        Players[n]=open("./data/pandemic/"+Players[n]+".txt", "w")
        for i in range(n,number_of_players*4,number_of_players):
          Players[n].write(Start_PlayerCards_Deck[i][0]+":"+Start_PlayerCards_Deck[i][1]+":"+Start_PlayerCards_Deck[i][2]+";")
        Players[n].close()
      del Start_PlayerCards_Deck[0:(number_of_players*4)-1]

    elif number_of_players==1:
      for n in range(len(Players)):
        Players[n]=open("./data/pandemic/"+Players[n]+".txt", "w")
        for i in range(n,number_of_players*5,number_of_players):
          Players[n].write(Start_PlayerCards_Deck[i][0]+":"+Start_PlayerCards_Deck[i][1]+":"+Start_PlayerCards_Deck[i][2]+";")
        Players[n].close()
      del Start_PlayerCards_Deck[0:(number_of_players*4)-1]

    PlayerCards_Deck_temp=[]
    if Difficulty ==0:
      quater=Start_PlayerCards_Deck
      random.shuffle(quater)
      for n in range(len(quater)):
        PlayerCards_Deck.write(quater[n][0]+":"+quater[n][1]+":"+quater[n][2]+";")

    else:
      for i in range(1,Difficulty+1):
        quater=Start_PlayerCards_Deck[int(i*(deck_size/Difficulty)-deck_size/Difficulty):int(i*deck_size/Difficulty)]
        quater.append(["Epidemic","","Increase, Infect, Intensify"])
        random.shuffle(quater)
        for n in range(len(quater)):
          PlayerCards_Deck.write(quater[n][0]+":"+quater[n][1]+":"+quater[n][2]+";")


    PlayerCards_Deck.close()

######################################################################################################################################################################
######################################################################    CHANGE ROLE    #############################################################################
######################################################################################################################################################################

def pandemic_changerole():
  if request.method == "POST":
    details=request.form
    players_name=details['action']
    role_choice=details['roles_name']

    # Read in Roles from roles file
    Roles=[]
    Roles_temp=[]
    Roles_file = open("./data/pandemic/Roles.txt", "r")
    for x in Roles_file:
      Roles_temp.extend(x.split(";"))
      for i in Roles_temp:
        Roles.append(i.split(":"))
    Roles_file.close()

    if len(Roles)!=0:
      del Roles[-1]  

    # Read in Players from Players file
    Players=[]
    Players_temp=[]
    Players_file = open("./data/pandemic/Players.txt", "r")
    for x in Players_file:
      Players_temp.extend(x.split(";"))
      for i in Players_temp:
        Players.append(i.split(":"))
    Players_file.close()

    if len(Players)!=0:
      del Players[-1]  

    Roles_selected=[players_name]
    for i in range(len(Roles)):
      if Roles[i][0]==role_choice:
        Roles_selected.extend(Roles[i])
    
    for i in range(len(Players)):
      if Players[i][0]==players_name:
        Players[i]=Roles_selected


    Players_file = open("./data/pandemic/Players.txt", "w")
    for i in range(len(Players)):
      Players_file.write(Players[i][0]+":"+Players[i][1]+":"+Players[i][2]+";")
    Players_file.close


######################################################################################################################################################################
######################################################################    ADD PLAYER    #############################################################################
######################################################################################################################################################################

def pandemic_add_player():
  return ""

######################################################################################################################################################################
######################################################################    DRAW CARD    #############################################################################
######################################################################################################################################################################

def pandemic_draw_card():
  if request.method == "POST":
    details=request.form

    PlayerCards_deck_temp=[]
    PlayerCards_Deck=[]
    PlayerCards_deck_file = open("./data/pandemic/PlayerCards_Deck.txt", "r")
    for x in PlayerCards_deck_file:
      PlayerCards_deck_temp.extend(x.split(";"))
      for i in PlayerCards_deck_temp:
        PlayerCards_Deck.append(i.split(":"))
    PlayerCards_deck_file.close()

    if len(PlayerCards_Deck)!=0:
      del PlayerCards_Deck[-1] 


    Hand_temp=[]
    Hand=[]
    Hand_file = open("./data/pandemic/"+details['action']+".txt", "r")
    for x in Hand_file:
      Hand_temp.extend(x.split(";"))
      for i in Hand_temp:
        Hand.append(i.split(":"))
    Hand_file.close()

    if len(Hand)!=0:
      del Hand[-1] 

    if len(Hand)<=8:
      file=open("./data/pandemic/"+details['action']+".txt", "a")
      file.write(PlayerCards_Deck[0][0]+":"+PlayerCards_Deck[0][1]+":"+PlayerCards_Deck[0][2]+";")
      file.close()

      del PlayerCards_Deck[0]
      PlayerCards_Deck_file = open("./data/pandemic/PlayerCards_Deck.txt", "w")
      for i in range(len(PlayerCards_Deck)):
        PlayerCards_Deck_file.write(PlayerCards_Deck[i][0]+":"+PlayerCards_Deck[i][1]+":"+PlayerCards_Deck[i][2]+";")
      PlayerCards_Deck_file.close


######################################################################################################################################################################
###################################################################    USE CARD    #######################################################################
######################################################################################################################################################################


def pandemic_use_card():
  if request.method == "POST":
    details=request.form
    names=details['action']
    info=names.split(":")

    Hand_temp=[]
    Hand=[]
    Hand_file = open("./data/pandemic/"+str(info[0])+".txt", "r")
    for x in Hand_file:
      Hand_temp.extend(x.split(";"))
      for i in Hand_temp:
        Hand.append(i.split(":"))
    Hand_file.close()

    if len(Hand)!=0:
      del(Hand[-1])
    
    card=str(info[1])
    for i in range(len(Hand)):
        if Hand[i][0]==card:
            PlayerCards_Discard_file = open("./data/pandemic/PlayerCards_Discard.txt", "a")
            PlayerCards_Discard_file.write(Hand[i][0]+":"+Hand[i][1]+":"+Hand[i][2]+";")
            PlayerCards_Discard_file.close()
            del Hand[i]
            break
    
    Hand_file = open("./data/pandemic/"+str(info[0])+".txt", "w")
    for i in range(len(Hand)):
        Hand_file.write(Hand[i][0]+":"+Hand[i][1]+":"+Hand[i][2]+";")
    Hand_file.close()


######################################################################################################################################################################
#########################################################################    SHARE KNOWLEDGE    ##########################################################################
######################################################################################################################################################################

def pandemic_shareknowledge():
  if request.method == "POST":
    details=request.form
    players_name=details['players_name']
    names=details['action']
    info=names.split(":")

    Hand_temp=[]
    Hand=[]
    Hand_file = open("./data/pandemic/"+str(info[0])+".txt", "r")
    for x in Hand_file:
      Hand_temp.extend(x.split(";"))
      for i in Hand_temp:
        Hand.append(i.split(":"))
    Hand_file.close()

    if len(Hand)!=0:
        del(Hand[-1])

    card=str(info[1])
    for i in range(len(Hand)):
        if Hand[i][0]==card:
            file = open("./data/pandemic/"+players_name+".txt", "a")
            file.write(Hand[i][0]+":"+Hand[i][1]+":"+Hand[i][2]+";")
            file.close()
            del Hand[i]
            break

      
    playercards_discard_file = open("./data/pandemic/"+str(info[0])+".txt", "w")
    for i in range(len(Hand)):
        playercards_discard_file.write(Hand[i][0]+":"+Hand[i][1]+":"+Hand[i][2]+";")