from win10toast import ToastNotifier
from datetime import date
from datetime import datetime
import datetime
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
    configfile.write("yes")
    configfile.write("\n")
    configfile.write("# Reminder of previously selected birthdays?: 'yes' / 'no' ")
    configfile.write("\n")
    configfile.write("windows")
    configfile.write("\n")
    configfile.write("# Chooose your calendar provider: 'windows', 'google'")  
    configfile.write("\n")
    configfile.write("mystudylife")
    configfile.write("\n")
    configfile.write("# Choose your management app:'mystudylife', 'todoist'")
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

if doit in ("yes"):
    birthdayfile = "birthday.txt"
    rawtoday = date.today()
    strtoday = str(rawtoday)
    today = re.sub(r'.', '', strtoday, count = 5)
    rawnextweektoday = datetime.date.today()
    nextweektoday = rawnextweektoday + datetime.timedelta(days=7)
    nexttoday = re.sub(r'.', '', str(nextweektoday), count = 5)
    nexttoday = str(nexttoday)

    fileName = open(birthdayfile, "r")

    for line in fileName:
        if today in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast("It is" + person.title() + "'s birthday today!!", " ")

    fileName.close()

    nextfileName = open(birthdayfile, "r")

    for nextline in nextfileName:
        if nexttoday in nextline:
            nexteachline = nextline.split(" | ")
            nextperson = nexteachline[0]
            toaster.show_toast("It is" + nextperson.title() + "'s birthday in a week!!", " ")

    nextfileName.close()