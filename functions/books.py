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

def books_home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users")
    mysql.connection.commit()
    users_names = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT Books.Books_Name, Users.Users_Name FROM Books INNER JOIN Users ON Books.Users_ID=Users.Users_ID WHERE Books.Books_Finished=0")
    mysql.connection.commit()
    books_names_upcoming = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT Books.Books_Name, Users.Users_Name FROM Books INNER JOIN Users ON Books.Users_ID=Users.Users_ID WHERE Books.Books_Finished=1")
    mysql.connection.commit()
    books_names_chosen = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT Books.Books_Name, Users.Users_Name FROM Books INNER JOIN Users ON Books.Users_ID=Users.Users_ID WHERE Books.Books_Finished=2")
    mysql.connection.commit()
    books_names_finished = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()
    





    users_selection = []
    books_upcoming_selection = []
    books_finished_selection = []
    books_chosen_selection = [] 

    for row in users_names:
        users_selection.append(row) #adding each row from the database into a newly created list, info 

    for row in books_names_upcoming:
        books_upcoming_selection.append(row) #adding each row from the database into a newly created list, info 
    
    for row in books_names_chosen:
        books_chosen_selection.append(row) #adding each row from the database into a newly created list, info 
    
    for row in books_names_finished:
        books_finished_selection.append(row) #adding each row from the database into a newly created list, info 
    
    return (books_upcoming_selection, users_selection, books_finished_selection, books_chosen_selection)







def books_edit():
    if request.method == "POST":
        details=request.form
        books_name=details['books_name']
        users_name=details['users_name']
        users_password=details['users_password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT Users_Password FROM Users WHERE Users_Name=(%s)", [users_name])
        mysql.connection.commit()
        users_password_true = cur.fetchall()

        users_password_selection=[]

        for row in users_password_true:
            users_password_selection.append(row) #adding each row from the database into a newly created list, info 
        
        if books_name != "" and users_password == users_password_selection[0][0]:
            books_name = re.sub("^\s*", "", books_name)
            if details['action'] == 'Create':               
                cur.execute("INSERT IGNORE INTO Books (Books_Name, Users_ID) VALUES ((%s), (SELECT Users_ID from Users WHERE Users_Name= (%s)))", [books_name, users_name])
            elif details['action'] == 'Delete':
                cur.execute("DELETE FROM Books WHERE Books_Name=(%s)", [books_name])
            mysql.connection.commit()
            cur.close()        