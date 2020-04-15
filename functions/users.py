from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os
import re


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = os.environ['MYSQL_HOST']
app.config["MYSQL_USER"] = os.environ['MYSQL_USER']
app.config["MYSQL_PASSWORD"] = os.environ['MYSQL_PASSWORD']
app.config["MYSQL_DB"] = os.environ['MYSQL_DB']



mysql = MySQL(app)


def users_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    users_selection = []

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info  

    return users_selection


def users_edit():
    if request.method == "POST":
        details=request.form
        users_name=details['users_name']
        users_email=details['users_email']
        users_password=details['users_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Name=(%s)", [users_name])
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Email=(%s)", [users_email])
        mysql.connection.commit()
        users_password_true = cur.fetchall()

        users_password_selection=[]

        for row in users_password_true:
            users_password_selection.append(row) #adding each row from the database into a newly created list, info 


        if users_name != "" and users_email != "" and users_password != "":
            cur = mysql.connection.cursor()
            users_name = re.sub("^\s*", "", users_name)
            users_password = re.sub("^\s*", "", users_password)
            if details['action'] == 'Create':
                cur.execute("INSERT IGNORE INTO Users (Users_Name, Users_Password, Users_Email) VALUES ((%s),(%s),(%s))", [users_name, users_password, users_email])
            elif len(users_password_selection)>0:
                if details['action'] == 'Delete' and users_password == users_password_selection[0][0]:
                    cur.execute("DELETE FROM Users WHERE Users_Name=(%s)", [users_name])
            mysql.connection.commit()
            cur.close()
