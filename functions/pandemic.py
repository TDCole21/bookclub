import random
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
import re

def pandemic_home():
  cities_temp=[]
  Cities=[]
  cities_file = open("./data/pandemic/Cities.txt", "r")
  for x in cities_file:
    cities_temp.extend(x.split(";"))
    for i in cities_temp:
      Cities.append(i.split(":"))
  cities_file.close()

  events_temp=[]
  Events=[]
  events_file = open("./data/pandemic/Events.txt", "r")
  for x in events_file:
    events_temp.extend(x.split(";"))
    for i in events_temp:
      Events.append(i.split(":"))
  events_file.close()

  nick_temp=[]
  Nick=[]
  nick_file = open("./data/pandemic/Nick.txt", "r")
  for x in nick_file:
    nick_temp.extend(x.split(";"))
    for i in nick_temp:
      Nick.append(i.split(":"))
  nick_file.close()

  cole_temp=[]
  Cole=[]
  cole_file = open("./data/pandemic/Cole.txt", "r")
  for x in cole_file:
    cole_temp.extend(x.split(";"))
    for i in cole_temp:
      Cole.append(i.split(":"))
  cole_file.close()

  cal_temp=[]
  Cal=[]
  cal_file = open("./data/pandemic/Cal.txt", "r")
  for x in cal_file:
    cal_temp.extend(x.split(";"))
    for i in cal_temp:
      Cal.append(i.split(":"))
  cal_file.close()

  james_temp=[]
  James=[]
  james_file = open("./data/pandemic/James.txt", "r")
  for x in james_file:
    james_temp.extend(x.split(";"))
    for i in james_temp:
      James.append(i.split(":"))
  james_file.close()

  deck_temp=[]
  Deck=[]
  deck_file = open("./data/pandemic/Deck.txt", "r")
  for x in deck_file:
    deck_temp.extend(x.split(";"))
    for i in deck_temp:
      Deck.append(i.split(":"))
  deck_file.close()

  return [James, Cole, Nick, Cal, Deck]


def pandemic_game_setup():
  deck_temp=[]
  James=open("./data/pandemic/James.txt", "w")
  Cole=open("./data/pandemic/Cole.txt", "w")
  Nick=open("./data/pandemic/Nick.txt", "w")
  Cal=open("./data/pandemic/Cal.txt", "w")
  Deck=open("./data/pandemic/Deck.txt", "w")
  James.write("")
  Cole.write("")
  Nick.write("")
  Cal.write("")
  James.close()
  Cole.close()
  Nick.close()
  Cal.close()
  Deck.close()

  James=open("./data/pandemic/James.txt", "a")
  Cole=open("./data/pandemic/Cole.txt", "a")
  Nick=open("./data/pandemic/Nick.txt", "a")
  Cal=open("./data/pandemic/Cal.txt", "a")
  Deck=open("./data/pandemic/Deck.txt", "a")
  cities = [["Algiers","Black"],["Atlanta","Blue"],["Baghdad","Black"],["Bangkok","Red"],["Beijing","Red"],["Bogota","Yellow"],["Buenos Aries","Yellow"],["Cairo","Black"],["Chennai","Red"],["Chicago","Blue"],["Delhi","Black"],["Essen","Blue"],["Ho Chi Minh City","Red"],["Hong Kong","Red"],["Istanbul","Black"],["Jakarta","Red"],["Johannesburg","Yellow"],["Karachi","Black"],["Khartoum","Yellow"],["Kinshasa","Yellow"],["Kolkata","Black"],["Lagos","Yellow"],["Lima","Yellow"],["London","Blue"],["Los Angeles","Blue"],["Madrid","Blue"],["Manila","Red"],["Mexico City","Yellow"],["Miami","Yellow"],["Milan","Blue"],["Montreal","Blue"],["Moscow","Black"],["Mumbai","Black"],["New York","Blue"],["Osaka","Red"],["Paris","Blue"],["Riyadh","Black"],["San Francisco","Blue"],["Santiago","Yellow"],["Sao Paulo","Yellow"],["Seoul","Red"],["Shanghai","Red"],["St. Petersburg","Blue"],["Sydney","Red"],["Taipei","Red"],["Tehran","Black"],["Tokyo","Red"],["Washington","Blue"]]
  events = [["Resilient Population","Remove any 1 card in the infection discard pile from the game"],["Forecast","Draw, look at, and rearrange the top 6 cards of the infection deck. Put them back on top"],["Government grant","Add 1 research station to any city (no city card needed)"],["One quiet night","Skip the next infect cities step (do not flip over any infection cards)"],["Airlift","Move an 1 pawn to any city. Get permission before moving another player's pawn"]]
  Start_Deck=[]
  q1=[]
  q2=[]
  q3=[]
  q4=[]
  Start_Deck.extend(cities)
  Start_Deck.extend(events) # puts the cities and event cards into the deck

  random.shuffle(Start_Deck)

  for i in range (0,12,4):
    James.write(Start_Deck[i][0]+":"+Start_Deck[i][1]+";")
    Cole.write(Start_Deck[i+1][0]+":"+Start_Deck[i+1][1]+";")
    Cal.write(Start_Deck[i+2][0]+":"+Start_Deck[i+2][1]+";")
    Nick.write(Start_Deck[i+3][0]+":"+Start_Deck[i+3][1]+";")
  
  for i in range (12,16,4):
    James.write(Start_Deck[i][0]+":"+Start_Deck[i][1])
    Cole.write(Start_Deck[i+1][0]+":"+Start_Deck[i+1][1])
    Cal.write(Start_Deck[i+2][0]+":"+Start_Deck[i+2][1])
    Nick.write(Start_Deck[i+3][0]+":"+Start_Deck[i+3][1])
  
  del Start_Deck[0:15]

  q1=Start_Deck[0:10]
  q1.append(["Epidemic","Increase, Infect, Intensify"])
  random.shuffle(q1)
  q2=Start_Deck[10:20]
  q2.append(["Epidemic","Increase, Infect, Intensify"])
  random.shuffle(q2)
  q3=Start_Deck[20:29]
  q3.append(["Epidemic","Increase, Infect, Intensify"])
  random.shuffle(q3)
  q4=Start_Deck[29:38]
  q4.append(["Epidemic","Increase, Infect, Intensify"])
  random.shuffle(q4)
  deck_temp.extend(q1)
  deck_temp.extend(q2)
  deck_temp.extend(q3)
  deck_temp.extend(q4)

  for i in deck_temp:
    Deck.write(i[0]+":"+i[1]+";")

  James.close()
  Cole.close()
  Nick.close()
  Cal.close()
  Deck.close()


def pandemic_draw_card():
  if request.method == "POST":
    details=request.form
    James=open("./data/pandemic/James.txt", "a")
    Cole=open("./data/pandemic/Cole.txt", "a")
    Nick=open("./data/pandemic/Nick.txt", "a")
    Cal=open("./data/pandemic/Cal.txt", "a")

    deck_temp=[]
    Deck=[]
    deck_file = open("./data/pandemic/Deck.txt", "r")
    for x in deck_file:
      deck_temp.extend(x.split(";"))
      for i in deck_temp:
        Deck.append(i.split(":"))
    deck_file.close()


    if details['action'] == 'James Draw Card':
      James.write(";"+Deck[0][0]+":"+Deck[0][1])
    elif details['action'] == 'Nick Draw Card':
      Nick.write(";"+Deck[0][0]+":"+Deck[0][1])
    elif details['action'] == 'Cole Draw Card':
      Cole.write(";"+Deck[0][0]+":"+Deck[0][1])
    else:
      Cal.write(";"+Deck[0][0]+":"+Deck[0][1])
    
    del Deck[0]
    deck_file = open("./data/pandemic/Deck.txt", "w")
    for i in range(len(Deck)-1):
      deck_file.write(Deck[i][0]+":"+Deck[i][1]+";")
    


    James.close()
    Cole.close()
    Nick.close()
    Cal.close()

def pandemic_use_card():
  if request.method == "POST":
    details=request.form
    nick_temp=[]
    Nick=[]
    nick_file = open("./data/pandemic/Nick.txt", "r")
    for x in nick_file:
      nick_temp.extend(x.split(";"))
      for i in nick_temp:
        Nick.append(i.split(":"))
    nick_file.close()

    cole_temp=[]
    Cole=[]
    cole_file = open("./data/pandemic/Cole.txt", "r")
    for x in cole_file:
      cole_temp.extend(x.split(";"))
      for i in cole_temp:
        Cole.append(i.split(":"))
    cole_file.close()

    cal_temp=[]
    Cal=[]
    cal_file = open("./data/pandemic/Cal.txt", "r")
    for x in cal_file:
      cal_temp.extend(x.split(";"))
      for i in cal_temp:
        Cal.append(i.split(":"))
    cal_file.close()

    james_temp=[]
    James=[]
    james_file = open("./data/pandemic/James.txt", "r")
    for x in james_file:
      james_temp.extend(x.split(";"))
      for i in james_temp:
        James.append(i.split(":"))
    james_file.close()


    if re.search("^James", details['action']):
      string=str(details['action'])
      num=int(string[-1])
      del James[num]

      length=len(James)-1

      james_file = open("./data/pandemic/James.txt", "w")
      for i in range(len(James)-1):
        james_file.write(James[i][0]+":"+James[i][1]+";")
      james_file.write(James[length][0]+":"+James[length][1])
      james_file.close()

    elif re.search("^Cole", details['action']):
      string=str(details['action'])
      num=int(string[-1])
      del Cole[num]

      length=len(Cole)-1

      cole_file = open("./data/pandemic/Cole.txt", "w")
      for i in range(len(Cole)-1):
        cole_file.write(Cole[i][0]+":"+Cole[i][1]+";")
      cole_file.write(Cole[length][0]+":"+Cole[length][1])
      cole_file.close()
     

    elif re.search("^Nick", details['action']):
      string=str(details['action'])
      num=int(string[-1])
      del Nick[num]

      length=len(Nick)-1

      nick_file = open("./data/pandemic/Nick.txt", "w")
      for i in range(len(Nick)-1):
        nick_file.write(Nick[i][0]+":"+Nick[i][1]+";")
      nick_file.write(Nick[length][0]+":"+Nick[length][1])
      nick_file.close()

    elif re.search("^Cal", details['action']):
      string=str(details['action'])
      num=int(string[-1])
      del Cal[num]

      length=len(Cal)-1

      cal_file = open("./data/pandemic/Cal.txt", "w")
      for i in range(len(Cal)-1):
        cal_file.write(Cal[i][0]+":"+Cal[i][1]+";")
      cal_file.write(Cal[length][0]+":"+Cal[length][1])
      cal_file.close()