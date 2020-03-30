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

def films_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Streaming_Platforms")
    mysql.connection.commit()
    streaming_platforms_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT Films.Films_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((Films INNER JOIN Users ON Films.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON Films.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID)")
    mysql.connection.commit()
    films_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()
    
    users_selection = []
    films_selection = []
    streaming_platforms_selection=[]

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in films_names:
        films_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in streaming_platforms_names:
        streaming_platforms_selection.append(row) #adding each row from the database into a newly created list, info 
    
    return (films_selection, users_selection, streaming_platforms_selection)




def films_create():
    if request.method == "POST":
        details=request.form
        films_name=details['films_name']
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



        if films_name != "" and streaming_platforms_name != "- Choose a Streaming Platform -" and users_password == users_password_selection[0][0]:
            cur = mysql.connection.cursor()
            films_name = re.sub("^\s*", "", films_name)          
            cur.execute("INSERT IGNORE INTO Films (Films_Name, Streaming_Platforms_ID, Users_ID) VALUES ((%s), (SELECT Streaming_Platforms_ID from Streaming_Platforms WHERE Streaming_Platforms_Name= (%s)), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [films_name, streaming_platforms_name, users_name])
            mysql.connection.commit()
            cur.close()