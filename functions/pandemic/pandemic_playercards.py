from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def pandemic_playercards_discard():
    playercards_discard_temp=[]
    PlayerCards_Discard=[]
    playercards_discard_file = open("./data/pandemic/PlayerCards_Discard.txt", "r")
    for x in playercards_discard_file:
        playercards_discard_temp.extend(x.split(";"))
    for i in playercards_discard_temp:
        PlayerCards_Discard.append(i.split(":"))
    playercards_discard_file.close()

    if len(PlayerCards_Discard)!=0:
        del PlayerCards_Discard[-1]

    return (PlayerCards_Discard)

def pandemic_playercards_recover():
    if request.method == "POST":
        details=request.form
        players_name=details['players_name']

        playercards_discard_temp=[]
        PlayerCards_Discard=[]
        playercards_discard_file = open("./data/pandemic/PlayerCards_Discard.txt", "r")
        for x in playercards_discard_file:
            playercards_discard_temp.extend(x.split(";"))
        for i in playercards_discard_temp:
            PlayerCards_Discard.append(i.split(":"))
        playercards_discard_file.close()

        if len(PlayerCards_Discard)!=0:
            del PlayerCards_Discard[-1]

        for i in range(len(PlayerCards_Discard)):
            if PlayerCards_Discard[i][0]==details['action']:
                file = open("./data/pandemic/"+players_name+".txt", "a")
                file.write(PlayerCards_Discard[i][0]+":"+PlayerCards_Discard[i][1]+":"+PlayerCards_Discard[i][2]+";")
                file.close()
                del PlayerCards_Discard[i]
                break

        
        playercards_discard_file = open("./data/pandemic/PlayerCards_Discard.txt", "w")
        for i in range(len(PlayerCards_Discard)):
            playercards_discard_file.write(PlayerCards_Discard[i][0]+":"+PlayerCards_Discard[i][1]+":"+PlayerCards_Discard[i][2]+";")

