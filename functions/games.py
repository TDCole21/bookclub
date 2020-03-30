from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from data import info
import os
import re


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = info.MySQLhost
app.config["MYSQL_USER"] = info.MySQLuser
app.config["MYSQL_PASSWORD"] = info.MySQLpassword
app.config["MYSQL_DB"] = info.MySQLdb



mysql = MySQL(app)

def games_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Consoles")
    mysql.connection.commit()
    consoles_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT Games.Games_Name, Users.Users_Name, Consoles.Consoles_Name FROM ((Games INNER JOIN Users ON Games.Users_ID=Users.Users_ID) INNER JOIN Consoles ON Games.Consoles_ID=Consoles.Consoles_ID)")
    mysql.connection.commit()
    games_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()
    
    users_selection = []
    games_selection = []
    consoles_selection=[]

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in games_names:
        games_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in consoles_names:
        consoles_selection.append(row) #adding each row from the database into a newly created list, info 
    
    return (games_selection, users_selection, consoles_selection)




def games_create():
    if request.method == "POST":
        details=request.form
        games_name=details['games_name']
        consoles_name=details['consoles_name']
        users_name=details['users_name']
        users_password=details['users_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Name=(%s)", [users_name])
        mysql.connection.commit()
        users_password_true = cur.fetchall()

        users_password_selection=[]

        for row in users_password_true:
            users_password_selection.append(row) #adding each row from the database into a newly created list, info 


        if games_name != "" and consoles_name != "- Choose a Console -" and users_password == users_password_selection[0][0]:
            cur = mysql.connection.cursor()
            games_name = re.sub("^\s*", "", games_name)          
            cur.execute("INSERT IGNORE INTO Games (Games_Name, Consoles_ID, Users_ID) VALUES ((%s), (SELECT Consoles_ID from Consoles WHERE Consoles_Name= (%s)), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [games_name, consoles_name, users_name])
            mysql.connection.commit()
            cur.close()