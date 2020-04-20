from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def pandemic_infectioncards_discard():
    InfectionCards_Discard_temp=[]
    InfectionCards_Discard=[]
    InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
    for x in InfectionCards_Discard_file:
        InfectionCards_Discard_temp.extend(x.split(";"))
    for i in InfectionCards_Discard_temp:
        InfectionCards_Discard.append(i.split(":"))
    InfectionCards_Discard_file.close()

    if len(InfectionCards_Discard)!=0:
        del InfectionCards_Discard[-1]


    InfectionCards_Removed_temp=[]
    InfectionCards_Removed=[]
    InfectionCards_Removed_file = open("./data/pandemic/InfectionCards_Removed.txt", "r")
    for x in InfectionCards_Removed_file:
        InfectionCards_Removed_temp.extend(x.split(";"))
    for i in InfectionCards_Removed_temp:
        InfectionCards_Removed.append(i.split(":"))
    InfectionCards_Removed_file.close()

    if len(InfectionCards_Removed)!=0:
        del InfectionCards_Removed[-1]

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

    return (InfectionCards_Discard,InfectionCards_Removed, Epidemics)

def pandemic_infectioncards_remove():
    if request.method == "POST":

        details=request.form

        InfectionCards_Discard_temp=[]
        InfectionCards_Discard=[]
        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
        for x in InfectionCards_Discard_file:
            InfectionCards_Discard_temp.extend(x.split(";"))
        for i in InfectionCards_Discard_temp:
            InfectionCards_Discard.append(i.split(":"))
        InfectionCards_Discard_file.close()

        if len(InfectionCards_Discard)!=0:
            del InfectionCards_Discard[-1]


        card=str(details['action'])
        for i in range(len(InfectionCards_Discard)):
            if InfectionCards_Discard[i][0]==card:
                InfectionCards_Removed_file = open("./data/pandemic/InfectionCards_Removed.txt", "a")
                InfectionCards_Removed_file.write(InfectionCards_Discard[i][0]+":"+InfectionCards_Discard[i][1]+";")
                InfectionCards_Removed_file.close()
                del InfectionCards_Discard[i]
                break
        
        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "w")
        for i in range(len(InfectionCards_Discard)):
            InfectionCards_Discard_file.write(InfectionCards_Discard[i][0]+":"+InfectionCards_Discard[i][1]+";")
        InfectionCards_Discard_file.close()


def pandemic_infectioncards_recover():
    if request.method == "POST":

        details=request.form

        InfectionCards_Discard_temp=[]
        InfectionCards_Discard=[]
        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
        for x in InfectionCards_Discard_file:
            InfectionCards_Discard_temp.extend(x.split(";"))
        for i in InfectionCards_Discard_temp:
            InfectionCards_Discard.append(i.split(":"))
        InfectionCards_Discard_file.close()

        if len(InfectionCards_Discard)!=0:
            del InfectionCards_Discard[-1]

        InfectionCards_Deck_temp=[]
        InfectionCards_Deck=[]
        InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "r")
        for x in InfectionCards_Deck_file:
            InfectionCards_Deck_temp.extend(x.split(";"))
        for i in InfectionCards_Deck_temp:
            InfectionCards_Deck.append(i.split(":"))
        InfectionCards_Deck_file.close()

        if len(InfectionCards_Deck)!=0:
            del InfectionCards_Deck[-1]


        card=str(details['action'])
        for i in range(len(InfectionCards_Discard)):
            if InfectionCards_Discard[i][0]==card:
                InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "w")
                InfectionCards_Deck_file.write(InfectionCards_Discard[i][0]+":"+InfectionCards_Discard[i][1]+";")
                for x in range(len(InfectionCards_Deck)):
                    InfectionCards_Deck_file.write(InfectionCards_Deck[x][0]+":"+InfectionCards_Deck[x][1]+";")
                InfectionCards_Deck_file.close()
                del InfectionCards_Discard[i]
                break
        
        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "w")
        for i in range(len(InfectionCards_Discard)):
            InfectionCards_Discard_file.write(InfectionCards_Discard[i][0]+":"+InfectionCards_Discard[i][1]+";")
        InfectionCards_Discard_file.close()

def pandemic_infectioncards_infect():
    if request.method == "POST":
        details=request.form

        InfectionCards_Deck_temp=[]
        InfectionCards_Deck=[]
        InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "r")
        for x in InfectionCards_Deck_file:
            InfectionCards_Deck_temp.extend(x.split(";"))
        for i in InfectionCards_Deck_temp:
            InfectionCards_Deck.append(i.split(":"))
        InfectionCards_Deck_file.close()

        if len(InfectionCards_Deck)!=0:
            del InfectionCards_Deck[-1]

        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "a")
        InfectionCards_Discard_file.write(InfectionCards_Deck[0][0]+":"+InfectionCards_Deck[0][1]+";")
        InfectionCards_Discard_file.close()
        del InfectionCards_Deck[0]
        
        InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "w")
        for i in range(len(InfectionCards_Deck)):
            InfectionCards_Deck_file.write(InfectionCards_Deck[i][0]+":"+InfectionCards_Deck[i][1]+";")
        InfectionCards_Deck_file.close()

def pandemic_infectioncards_epidemic():
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

        InfectionCards_Deck_temp=[]
        InfectionCards_Deck=[]
        InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "r")
        for x in InfectionCards_Deck_file:
            InfectionCards_Deck_temp.extend(x.split(";"))
        for i in InfectionCards_Deck_temp:
            InfectionCards_Deck.append(i.split(":"))
        InfectionCards_Deck_file.close()

        if len(InfectionCards_Deck)!=0:
            del InfectionCards_Deck[-1]

        InfectionCards_Discard_temp=[]
        InfectionCards_Discard=[]
        InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
        for x in InfectionCards_Discard_file:
            InfectionCards_Discard_temp.extend(x.split(";"))
        for i in InfectionCards_Discard_temp:
            InfectionCards_Discard.append(i.split(":"))
        InfectionCards_Discard_file.close()

        if len(InfectionCards_Discard)!=0:
            del InfectionCards_Discard[-1] 

        # 1 -Increase
        if details['action']=="1 - Increase":
            Epidemics[0][0]=str(int(Epidemics[0][0])+1)

            Epidemics_file = open("./data/pandemic/Epidemics.txt", "w")
            for i in range(len(Epidemics)):
                Epidemics_file.write(Epidemics[i][0]+":"+Epidemics[i][1]+":"+Epidemics[i][2]+";")
            Epidemics_file.close()

        # 2- Infect
        elif details['action']=="2 - Infect":
            InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "a")
            InfectionCards_Discard_file.write(InfectionCards_Deck[-1][0]+":"+InfectionCards_Deck[-1][1]+";")
            InfectionCards_Discard_file.close()
            del InfectionCards_Deck[-1]
            
            InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "w")
            for i in range(len(InfectionCards_Deck)):
                InfectionCards_Deck_file.write(InfectionCards_Deck[i][0]+":"+InfectionCards_Deck[i][1]+";")
            InfectionCards_Deck_file.close()

        # 3 - Intensify
        elif details['action']=="3 - Intensify":
            random.shuffle(InfectionCards_Discard)
            InfectionCards_Discard.extend(InfectionCards_Deck)    
            InfectionCards_Deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "w")
            for i in range(len(InfectionCards_Discard)):
                InfectionCards_Deck_file.write(InfectionCards_Discard[i][0]+":"+InfectionCards_Discard[i][1]+";")  
            InfectionCards_Discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "w") 
            InfectionCards_Deck_file.close()   