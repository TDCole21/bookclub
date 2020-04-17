from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def tvshows_home():
    users_temp=[]
    Users=[]
    users_file = open("./data/Users.txt", "r")
    for x in users_file:
        users_temp.extend(x.split(";"))
    for i in users_temp:
        Users.append(i.split(":"))
    users_file.close()

    del Users[-1]

    tvshows_temp=[]
    TVShows=[]
    tvshows_file = open("./data/watercooler/TVShows.txt", "r")
    for x in tvshows_file:
        tvshows_temp.extend(x.split(";"))
    for i in tvshows_temp:
        TVShows.append(i.split(":"))
    tvshows_file.close()

    del TVShows[-1]

    streaming_platforms_temp=[]
    Streaming_Platforms=[]
    streaming_platforms_file = open("./data/watercooler/Streaming_Platforms.txt", "r")
    for x in streaming_platforms_file:
        Streaming_Platforms.extend(x.split(";"))
    streaming_platforms_file.close()

    del Streaming_Platforms[-1]

    tvshows_upcoming_selection=[]
    tvshows_finished_selection=[]
    tvshows_chosen_selection=[]
    for i in TVShows:
        if int(i[3])==0:
            tvshows_upcoming_selection.append(i)
        elif int(i[3])==1:
            tvshows_chosen_selection.append(i)
        else:
            tvshows_finished_selection.append(i)

    return (tvshows_upcoming_selection, Users, Streaming_Platforms, tvshows_finished_selection, tvshows_chosen_selection)







def tvshows_edit():
    if request.method == "POST":
        details=request.form
        tvshows_name=details['tvshows_name']
        streaming_platforms_name=details.getlist('streaming_platforms_name')
        users_name=details['users_name']
        users_password=details['users_password']

        if len(streaming_platforms_name)>0:
            Streaming_Platforms=""
            for i in range(len(streaming_platforms_name)-1):
                Streaming_Platforms=Streaming_Platforms+str(streaming_platforms_name[i])+", "
            if Streaming_Platforms != "":
                Streaming_Platforms=Streaming_Platforms[0:len(Streaming_Platforms)-2]+" and "+str(streaming_platforms_name[-1])
            else:
                Streaming_Platforms=Streaming_Platforms+str(streaming_platforms_name[-1])

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
                    tvshows_name = re.sub("^\s*", "", tvshows_name)
                    tvshows_name = re.sub(":", "-", tvshows_name)
                    tvshows_name = re.sub(";", "-", tvshows_name)
                    TVShows=open("./data/watercooler/TVShows.txt", "a")
                    TVShows.write(tvshows_name+":"+Streaming_Platforms+":"+users_name+":0;")
                
                elif details['action'] == 'Remove':
                    tvshows_temp=[]
                    TVShows=[]
                    tvshows_file = open("./data/watercooler/TVShows.txt", "r")
                    for x in tvshows_file:
                        tvshows_temp.extend(x.split(";"))
                    for i in tvshows_temp:
                        TVShows.append(i.split(":"))
                    tvshows_file.close()

                    del TVShows[-1]

                    tvshows_file = open("./data/watercooler/TVShows.txt", "w")
                    for i in range(len(TVShows)):
                        if TVShows[i][0]==tvshows_name:
                            pass
                        else:
                            tvshows_file.write(TVShows[i][0]+":"+TVShows[i][1]+":"+TVShows[i][2]+":"+TVShows[i][3]+";") 



                elif users_name=="Cole" and details['action'] == 'Shuffle':
                    tvshows_temp=[]
                    TVShows=[]
                    tvshows_file = open("./data/watercooler/TVShows.txt", "r")
                    for x in tvshows_file:
                        tvshows_temp.extend(x.split(";"))
                    for i in tvshows_temp:
                        TVShows.append(i.split(":"))
                    tvshows_file.close()

                    del TVShows[-1]

                    tvshows_choice = []
                    for i in range(len(TVShows)):
                        if TVShows[i][3]=="1":
                            TVShows[i][3]="0"
                        if TVShows[i][3]=="0":
                            tvshows_choice.append(TVShows[i])

                    random.shuffle(tvshows_choice)

                    tvshows_choice[0][3]="1"

                    for i in range(len(TVShows)):
                        if TVShows[i][3]=="2":
                            tvshows_choice.append(TVShows[i])

                    tvshows_file = open("./data/watercooler/TVShows.txt", "w")
                    for i in range(len(tvshows_choice)):
                        tvshows_file.write(tvshows_choice[i][0]+":"+tvshows_choice[i][1]+":"+tvshows_choice[i][2]+":"+tvshows_choice[i][3]+";") 


                
                elif users_name=="Cole" and details['action'] == 'Finished':
                    tvshows_temp=[]
                    TVShows=[]
                    tvshows_file = open("./data/watercooler/TVShows.txt", "r")
                    for x in tvshows_file:
                        tvshows_temp.extend(x.split(";"))
                    for i in tvshows_temp:
                        TVShows.append(i.split(":"))
                    tvshows_file.close()

                    del TVShows[-1]

                    tvshows_choice = []
                    for i in range(len(TVShows)):
                        if TVShows[i][3]=="1":
                            TVShows[i][3]="2"


                    tvshows_file = open("./data/watercooler/TVShows.txt", "w")
                    for i in range(len(TVShows)):
                        tvshows_file.write(TVShows[i][0]+":"+TVShows[i][1]+":"+TVShows[i][2]+":"+TVShows[i][3]+";") 