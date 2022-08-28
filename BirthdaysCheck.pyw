from win10toast import ToastNotifier
from datetime import date
from datetime import datetime
import re
from os.path import exists
import time

if not exists("birthday.txt"):
    birthdayfile = open("birthday.txt", "w+")
    birthdayfile.write("# This file is used to store birthdays the user want's to be reminded of")
    birthdayfile.close

if not exists("config.txt"):

    configfile = open("config.txt", "w+")
    configfile.write("gmail")
    configfile.write("\n")
    configfile.write("# Choose your email provider: 'gmail', 'outlook' ")
    configfile.write("\n")
    configfile.write("y")
    configfile.write("\n")
    configfile.write("# Reminder of previously selected birthdays?: 'y' / 'n' ")
    configfile.write("\n")
    configfile.close

def setting():

        with open("config.txt") as settingsfile:
            settings = list(settingsfile)[0::2]
        settings = ([s.replace('\n', '') for s in settings])
        return settings

toaster = ToastNotifier()

rawdoit = setting()
doit = str(rawdoit[1])

if doit in ("y", "Y"):
    birthdayfile = "birthday.txt"
    rawtoday = date.today()
    strtoday = str(rawtoday)
    today = re.sub(r'.', '', strtoday, count = 5)

    fileName = open(birthdayfile, "r")
    for line in fileName:
        if today in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast("It is" + person.title() + "'s birthday today!!", " ")
