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

def tvshows_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Streaming_Platforms")
    mysql.connection.commit()
    streaming_platforms_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT TVShows.TVShows_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((TVShows INNER JOIN Users ON TVShows.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON TVShows.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID)")
    mysql.connection.commit()
    tvshows_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()
    
    users_selection = []
    tvshows_selection = []
    streaming_platforms_selection=[]

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in tvshows_names:
        tvshows_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in streaming_platforms_names:
        streaming_platforms_selection.append(row) #adding each row from the database into a newly created list, info 
    
    return (tvshows_selection, users_selection, streaming_platforms_selection)




def tvshows_create():
    if request.method == "POST":
        details=request.form
        tvshows_name=details['tvshows_name']
        streaming_platforms_name=details['streaming_platforms_name']
        users_name=details['users_name']
        users_password=details['users_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Name=(%s)", [users_name])
        mysql.connection.commit()
        users_password_true = cur.fetchall()

        users_password_selection=[]

        for row in users_password_true:
            users_password_selection.append(row) #adding each row from the database into a newly created list, info 



        if tvshows_name != "" and streaming_platforms_name != "- Choose a Streaming Platform -" and users_password == users_password_selection[0][0]:
            cur = mysql.connection.cursor()
            tvshows_name = re.sub("^\s*", "", tvshows_name)          
            cur.execute("INSERT IGNORE INTO TVShows (TVShows_Name, Streaming_Platforms_ID, Users_ID) VALUES ((%s), (SELECT Streaming_Platforms_ID from Streaming_Platforms WHERE Streaming_Platforms_Name= (%s)), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [tvshows_name, streaming_platforms_name, users_name])
            mysql.connection.commit()
            cur.close()