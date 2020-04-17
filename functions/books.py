from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def books_home():
    users_temp=[]
    Users=[]
    users_file = open("./data/Users.txt", "r")
    for x in users_file:
        users_temp.extend(x.split(";"))
    for i in users_temp:
        Users.append(i.split(":"))
    users_file.close()

    del Users[-1]

    books_temp=[]
    Books=[]
    books_file = open("./data/watercooler/Books.txt", "r")
    for x in books_file:
        books_temp.extend(x.split(";"))
    for i in books_temp:
        Books.append(i.split(":"))
    books_file.close()

    del Books[-1]

    books_upcoming_selection=[]
    books_finished_selection=[]
    books_chosen_selection=[]
    for i in Books:
        if int(i[2])==0:
            books_upcoming_selection.append(i)
        elif int(i[2])==1:
            books_chosen_selection.append(i)
        else:
            books_finished_selection.append(i)

    return (books_upcoming_selection, Users, books_finished_selection, books_chosen_selection)




def books_edit():
    if request.method == "POST":
        details=request.form
        books_name=details['books_name']
        users_name=details['users_name']
        users_password=details['users_password']

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
                    books_name = re.sub("^\s*", "", books_name)
                    books_name = re.sub(":", "-", books_name)
                    books_name = re.sub(";", "-", books_name)
                    Books=open("./data/watercooler/Books.txt", "a")
                    Books.write(books_name+":"+users_name+":0;")
                
                elif details['action'] == 'Remove':
                    books_temp=[]
                    Books=[]
                    books_file = open("./data/watercooler/Books.txt", "r")
                    for x in books_file:
                        books_temp.extend(x.split(";"))
                    for i in books_temp:
                        Books.append(i.split(":"))
                    books_file.close()

                    del Books[-1]

                    books_file = open("./data/watercooler/Books.txt", "w")
                    for i in range(len(Books)):
                        if Books[i][0]==books_name:
                            pass
                        else:
                            books_file.write(Books[i][0]+":"+Books[i][1]+":"+Books[i][2]+";") 
                
                elif users_name=="Cole" and details['action'] == 'Shuffle':
                    books_temp=[]
                    Books=[]
                    books_file = open("./data/watercooler/Books.txt", "r")
                    for x in books_file:
                        books_temp.extend(x.split(";"))
                    for i in books_temp:
                        Books.append(i.split(":"))
                    books_file.close()

                    del Books[-1]

                    books_choice = []
                    for i in range(len(Books)):
                        if Books[i][2]=="1":
                            Books[i][2]="0"
                        if Books[i][2]=="0":
                            books_choice.append(Books[i])

                    random.shuffle(books_choice)

                    books_choice[0][2]="1"

                    for i in range(len(Books)):
                        if Books[i][2]==2:
                            books_choice.append("Books[i]")

                    books_file = open("./data/watercooler/Books.txt", "w")
                    for i in range(len(books_choice)):
                        books_file.write(books_choice[i][0]+":"+books_choice[i][1]+":"+books_choice[i][2]+";") 


                
                elif users_name=="Cole" and details['action'] == 'Finished':
                    books_temp=[]
                    Books=[]
                    books_file = open("./data/watercooler/Books.txt", "r")
                    for x in books_file:
                        books_temp.extend(x.split(";"))
                    for i in books_temp:
                        Books.append(i.split(":"))
                    books_file.close()

                    del Books[-1]

                    books_choice = []
                    for i in range(len(Books)):
                        if Books[i][2]=="1":
                            Books[i][2]="2"


                    books_file = open("./data/watercooler/Books.txt", "w")
                    for i in range(len(Books)):
                        books_file.write(Books[i][0]+":"+Books[i][1]+":"+Books[i][2]+";") 