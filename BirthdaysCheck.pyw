from win10toast import ToastNotifier
from datetime import date
from datetime import datetime
import datetime
import re
from os.path import exists

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

    rntoday7 = datetime.date.today()
    ntoday7 = rntoday7 + datetime.timedelta(days=7)
    today7 = re.sub(r'.', '', str(ntoday7), count = 5)
    today7 = str(today7)
        
    rntoday6 = datetime.date.today()
    ntoday6 = rntoday6 + datetime.timedelta(days=6)
    today6 = re.sub(r'.', '', str(ntoday6), count = 5)
    today6 = str(today6)
        
    rntoday5 = datetime.date.today()
    ntoday5 = rntoday5 + datetime.timedelta(days=5)
    today5 = re.sub(r'.', '', str(ntoday5), count = 5)
    today5 = str(today5)
        
    rntoday4 = datetime.date.today()
    ntoday4 = rntoday4 + datetime.timedelta(days=4)
    today4 = re.sub(r'.', '', str(ntoday4), count = 5)
    today4 = str(today4)
        
    rntoday3 = datetime.date.today()
    ntoday3 = rntoday3 + datetime.timedelta(days=3)
    today3 = re.sub(r'.', '', str(ntoday3), count = 5)
    today3 = str(today3)
        
    rntoday2 = datetime.date.today()
    ntoday2 = rntoday2 + datetime.timedelta(days=2)
    today2 = re.sub(r'.', '', str(ntoday2), count = 5)
    today2 = str(today2)

    rntoday1 = datetime.date.today()
    ntoday1 = rntoday1 + datetime.timedelta(days=1)
    today1 = re.sub(r'.', '', str(ntoday1), count = 5)
    today1 = str(today1)
    
    fileName = open(birthdayfile, "r")

    for line in fileName:
        if today in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday today!!", " ", icon_path="Birthday.ico", duration=6 )

    fileName.close()
    fileName = open(birthdayfile, "r")

    for line in fileName:
        if today7 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday in a week!!", " 7 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")

    for line in fileName:
        if today6 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday is near!!", " 6 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")

    for line in fileName:
        if today5 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday is near!!", " 5 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")
            
    for line in fileName:
        if today4 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday is near!!", " 4 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")
            
    for line in fileName:
        if today3 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday is near!!", " 3 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")
            
    for line in fileName:
        if today2 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday is near!!", " 2 days left ", icon_path="Birthday.ico", duration=6 )
            
    fileName.close()
    fileName = open(birthdayfile, "r")
            
    for line in fileName:
        if today1 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            toaster.show_toast(person.title() + "'s birthday tomorrow!!", " 1 days left ", icon_path="Birthday.ico", duration=6 )

    fileName.close()