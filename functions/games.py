from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def games_home():
    users_temp=[]
    Users=[]
    users_file = open("./data/Users.txt", "r")
    for x in users_file:
        users_temp.extend(x.split(";"))
    for i in users_temp:
        Users.append(i.split(":"))
    users_file.close()

    del Users[-1]

    games_temp=[]
    Games=[]
    games_file = open("./data/watercooler/Games.txt", "r")
    for x in games_file:
        games_temp.extend(x.split(";"))
    for i in games_temp:
        Games.append(i.split(":"))
    games_file.close()

    del Games[-1]

    consoles_temp=[]
    Consoles=[]
    consoles_file = open("./data/watercooler/Consoles.txt", "r")
    for x in consoles_file:
        Consoles.extend(x.split(";"))
    consoles_file.close()

    del Consoles[-1]

    games_upcoming_selection=[]
    games_finished_selection=[]
    games_chosen_selection=[]
    for i in Games:
        if int(i[3])==0:
            games_upcoming_selection.append(i)
        elif int(i[3])==1:
            games_chosen_selection.append(i)
        else:
            games_finished_selection.append(i)

    return (games_upcoming_selection, Users, Consoles, games_finished_selection, games_chosen_selection)







def games_edit():
    if request.method == "POST":
        details=request.form
        games_name=details['games_name']
        consoles_name=details.getlist('consoles_name')
        users_name=details['users_name']
        users_password=details['users_password']

        if len(consoles_name)>0:
            Consoles=""
            for i in range(len(consoles_name)-1):
                Consoles=Consoles+str(consoles_name[i])+", "
            if Consoles != "":
                Consoles=Consoles[0:len(Consoles)-2]+" and "+str(consoles_name[-1])
            else:
                Consoles=Consoles+str(consoles_name[-1])


        users_temp=[]
        Users=[]
        users_file = open("./data/Users.txt", "r")
        for x in users_file:
            users_temp.extend(x.split(";"))
        for i in users_temp:
            Users.append(i.split(":"))
        users_file.close()

        del Users[-1]

        for i in range(len(Users)):
            if Users[i][0]==users_name and Users[i][1]==users_password:

                if details['action'] == 'Add':
                    games_name = re.sub("^\s*", "", games_name)
                    games_name = re.sub(":", "-", games_name)
                    games_name = re.sub(";", "-", games_name)
                    Games=open("./data/watercooler/Games.txt", "a")
                    Games.write(games_name+":"+Consoles+":"+users_name+":0;")
                
                elif details['action'] == 'Remove':
                    games_temp=[]
                    Games=[]
                    games_file = open("./data/watercooler/Games.txt", "r")
                    for x in games_file:
                        games_temp.extend(x.split(";"))
                    for i in games_temp:
                        Games.append(i.split(":"))
                    games_file.close()

                    del Games[-1]

                    games_file = open("./data/watercooler/Games.txt", "w")
                    for i in range(len(Games)):
                        if Games[i][0]==games_name:
                            pass
                        else:
                            games_file.write(Games[i][0]+":"+Games[i][1]+":"+Games[i][2]+":"+Games[i][3]+";") 


                elif users_name=="Cole" and details['action'] == 'Shuffle':
                    games_temp=[]
                    Games=[]
                    games_file = open("./data/watercooler/Games.txt", "r")
                    for x in games_file:
                        games_temp.extend(x.split(";"))
                    for i in games_temp:
                        Games.append(i.split(":"))
                    games_file.close()

                    del Games[-1]

                    games_choice = []
                    for i in range(len(Games)):
                        if Games[i][3]=="1":
                            Games[i][3]="0"
                        if Games[i][3]=="0":
                            games_choice.append(Games[i])

                    random.shuffle(games_choice)

                    games_choice[0][3]="1"

                    for i in range(len(Games)):
                        if Games[i][3]=="2":
                            games_choice.append(Games[i])

                    games_file = open("./data/watercooler/Games.txt", "w")
                    for i in range(len(games_choice)):
                        games_file.write(games_choice[i][0]+":"+games_choice[i][1]+":"+games_choice[i][2]+":"+games_choice[i][3]+";") 


                
                elif users_name=="Cole" and details['action'] == 'Finished':
                    games_temp=[]
                    Games=[]
                    games_file = open("./data/watercooler/Games.txt", "r")
                    for x in games_file:
                        games_temp.extend(x.split(";"))
                    for i in games_temp:
                        Games.append(i.split(":"))
                    games_file.close()

                    del Games[-1]

                    games_choice = []
                    for i in range(len(Games)):
                        if Games[i][3]=="1":
                            Games[i][3]="2"


                    games_file = open("./data/watercooler/Games.txt", "w")
                    for i in range(len(Games)):
                        games_file.write(Games[i][0]+":"+Games[i][1]+":"+Games[i][2]+":"+Games[i][3]+";")  