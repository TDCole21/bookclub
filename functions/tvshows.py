from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
import re


app = Flask(__name__) #__name__ is for best practice

# app.config["MYSQL_HOST"] = os.environ['MYSQL_HOST']
# app.config["MYSQL_USER"] = os.environ['MYSQL_USER']
# app.config["MYSQL_PASSWORD"] = os.environ['MYSQL_PASSWORD']
# app.config["MYSQL_DB"] = os.environ['MYSQL_DB']



mysql = MySQL(app)

def tvshows_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Streaming_Platforms")
    mysql.connection.commit()
    streaming_platforms_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT TVShows.TVShows_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((TVShows INNER JOIN Users ON TVShows.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON TVShows.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID) WHERE TVShows.TVShows_Finished=0")
    mysql.connection.commit()
    tvshows_names_upcoming = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT TVShows.TVShows_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((TVShows INNER JOIN Users ON TVShows.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON TVShows.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID) WHERE TVShows.TVShows_Finished=1")
    mysql.connection.commit()
    tvshows_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT TVShows.TVShows_Name, Users.Users_Name, Streaming_Platforms.Streaming_Platforms_Name FROM ((TVShows INNER JOIN Users ON TVShows.Users_ID=Users.Users_ID) INNER JOIN Streaming_Platforms ON TVShows.Streaming_Platforms_ID=Streaming_Platforms.Streaming_Platforms_ID) WHERE TVShows.TVShows_Finished=2")
    mysql.connection.commit()
    tvshows_names_finished = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()
    
    users_selection = []
    streaming_platforms_selection=[]
    tvshows_upcoming_selection = []
    tvshows_finished_selection = []
    tvshows_chosen_selection = [] 

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in streaming_platforms_names:
        streaming_platforms_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in tvshows_names_upcoming:
        tvshows_upcoming_selection.append(row) #adding each row from the database into a newly created list, info 
    
    
    for row in tvshows_names_chosen:
        tvshows_chosen_selection.append(row) #adding each row from the database into a newly created list, info 
    
    for row in tvshows_names_finished:
        tvshows_finished_selection.append(row) #adding each row from the database into a newly created list, info 
    
    for i in range(len(tvshows_names_upcoming)):
        tvshow_name=tvshows_names_upcoming[i][0]


    return (tvshows_upcoming_selection, users_selection, streaming_platforms_selection, tvshows_finished_selection, tvshows_chosen_selection)




def tvshows_edit():
    if request.method == "POST":
        details=request.form
        tvshows_name=details['tvshows_name']
        streaming_platforms_name=details.getlist('streaming_platforms_name')
        users_name=details['users_name']
        users_password=details['users_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Name=(%s)", [users_name])
        mysql.connection.commit()
        users_password_true = cur.fetchall()

        users_password_selection=[]

        for row in users_password_true:
            users_password_selection.append(row) #adding each row from the database into a newly created list, info 



        if tvshows_name != "" and users_password == users_password_selection[0][0]:
            cur = mysql.connection.cursor()
            tvshows_name = re.sub("^\s*", "", tvshows_name) 
            if details['action'] == 'Create' and streaming_platforms_name != "- Choose a Streaming Platform -":
                if len(streaming_platforms_name)>1:
                    for i in streaming_platforms_name:          
                        cur.execute("INSERT INTO TVShows (TVShows_Name, Streaming_Platforms_ID, Users_ID) VALUES ((%s), (SELECT Streaming_Platforms_ID from Streaming_Platforms WHERE Streaming_Platforms_Name= (%s)), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [tvshows_name, i, users_name])
                else:
                    cur.execute("INSERT IGNORE INTO TVShows (TVShows_Name, Streaming_Platforms_ID, Users_ID) VALUES ((%s), (SELECT Streaming_Platforms_ID from Streaming_Platforms WHERE Streaming_Platforms_Name= (%s)), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [tvshows_name, streaming_platforms_name, users_name])

            if details['action'] == 'Delete':
                cur.execute("DELETE FROM TVShows WHERE TVShows_Name=(%s)", [tvshows_name])     
            mysql.connection.commit()
            cur.close()