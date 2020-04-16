from flask import Flask, render_template, request, redirect, url_for
import os
import re

app = Flask(__name__) #__name__ is for best practice



def users_home():
    users_temp=[]
    Users=[]
    users_file = open("./data/Users.txt", "r")
    for x in users_file:
        users_temp.extend(x.split(";"))
    for i in users_temp:
        Users.append(i.split(":"))
    users_file.close()

    del Users[-1]

    return Users


def users_edit():
    if request.method == "POST":
        details=request.form
        users_name=details['users_name']
        users_password=details['users_password']

        if details['action'] == 'Add':
            users_password = re.sub("^\s*", "", users_password)
            users_password = re.sub(":", "-", users_password)
            users_password = re.sub(";", "-", users_password)
            users_name = re.sub("^\s*", "", users_name)
            users_name = re.sub(":", "-", users_name)
            users_name = re.sub(";", "-", users_name)
            Users=open("./data/Users.txt", "a")
            Users.write(users_name+":"+users_password+";")
        
        elif details['action'] == 'Remove':
            users_temp=[]
            Users=[]
            users_file = open("./data/Users.txt", "r")
            for x in users_file:
                users_temp.extend(x.split(";"))
            for i in users_temp:
                Users.append(i.split(":"))
            users_file.close()

            del Users[-1]

            users_file = open("./data/Users.txt", "w")
            for i in range(len(Users)):
                if Users[i][0]==users_name and Users[i][1]==users_password:
                    pass
                else:
                    users_file.write(Users[i][0]+":"+Users[i][1]+";")

