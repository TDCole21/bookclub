from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def pandemic_rules():
    actions_temp=[]
    Actions=[]
    actions_file = open("./data/pandemic/Actions.txt", "r")
    for x in actions_file:
        actions_temp.extend(x.split(";"))
    for i in actions_temp:
        Actions.append(i.split(":"))
    actions_file.close()

    del Actions[-1]

    roles_temp=[]
    Roles=[]
    roles_file = open("./data/pandemic/Roles.txt", "r")
    for x in roles_file:
        roles_temp.extend(x.split(";"))
    for i in roles_temp:
        Roles.append(i.split(":"))
    roles_file.close()

    del Roles[-1]

    return (Actions,Roles)