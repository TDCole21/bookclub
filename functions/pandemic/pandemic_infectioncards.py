from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def pandemic_infectioncards_discard():
    infectioncards_discard_temp=[]
    InfectionCards_Discard=[]
    infectioncards_discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
    for x in infectioncards_discard_file:
        infectioncards_discard_temp.extend(x.split(";"))
    for i in infectioncards_discard_temp:
        InfectionCards_Discard.append(i.split(":"))
    infectioncards_discard_file.close()

    del InfectionCards_Discard[-1]

    return (InfectionCards_Discard)

def pandemic_infectioncards_draw():
    infectioncards_deck_temp=[]
    InfectionCards_Deck=[]
    infectioncards_deck_file = open("./data/pandemic/InfectionCards_Deck.txt", "r")
    for x in infectioncards_deck_file:
        infectioncards_deck_temp.extend(x.split(";"))
    for i in infectioncards_deck_temp:
        InfectionCards_Deck.append(i.split(":"))
    infectioncards_deck_file.close()

    del InfectionCards_Deck[-1]


    infectioncards_discard_temp=[]
    InfectionCards_Discard=[]
    infectioncards_discard_file = open("./data/pandemic/InfectionCards_Discard.txt", "r")
    for x in infectioncards_discard_file:
        infectioncards_discard_temp.extend(x.split(";"))
    for i in infectioncards_discard_temp:
        InfectionCards_Discard.append(i.split(":"))
    infectioncards_discard_file.close()

    del InfectionCards_Discard[-1]

    return (InfectionCards_Deck,InfectionCards_Discard)