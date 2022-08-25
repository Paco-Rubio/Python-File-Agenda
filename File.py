
from rich.progress import track
import os
from datetime import date
import time
import re
import pyperclip
import math
import webbrowser
from os.path import exists
from win10toast import ToastNotifier

today = date.today()

toaster = ToastNotifier()

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

if not exists("birthday.txt"):
    birthdayfile = open("birthday.txt", "w+")
    birthdayfile.write("# This file is used to store birthdays the user want's to be reminded of")
    birthdayfile.close

def choose():
    
    print ()
    print (" W -> Write names ")
    print (" S -> Search in file ")
    print (" D -> Days left ")
    print (" A -> Age ")
    print (" O -> Open file ")
    print (" E -> Erase ")
    print (" L -> Lines in file ")
    print (" F -> Finish ")
    print (" C -> Copy line ")
    print (" M -> Mail ")
    print (" B -> Birthdays ")
    print ()
    time.sleep(0.2)

    rawoption = input(" What do you want to do? (W / S / D / A / O / E / L / F / C / M / B)  ")
    option = str(rawoption)
    if option in ("w", "W"):
         addtofile()
    elif option in ("s", "S"):
         searchinfile()
    elif option in ("d", "D"):
         daysleft()
    elif option in ("e", "E"):
         clean()
    elif option in ("f", "F"):
         finish()
    elif option in ("a","A"):
         age()
    elif option in ("o","O"):
         openfile()
    elif option in ("l","L"):
         countlines()
    elif option in ("c","C"):
         copyline()
    elif option in ("m","M"):
         mail()
    elif option in ("B","b"):
         birthday()
    else:
        print()
        print(" That's not a possible option")
        print()
        choose()
    
def restart():  
    
    time.sleep(0.5)
    print ()
    print (" W -> Write names ")
    print (" S -> Search in file ")
    print (" D -> Days left ")
    print (" A -> Age ")
    print (" O -> Open file ")
    print (" E -> Erase ")
    print (" L -> Lines in file ")
    print (" F -> Finish ")
    print (" C -> Copy line ")
    print (" M -> Mail ")
    print (" B -> Birthdays ")
    print()
    time.sleep(0.5)
    rawagain = input(" Anything else? (W / S / D / A / O / E / L / F / C / M / B)  ")
    again = str(rawagain)
    if again in ("w", "W"):
         addtofile()
    elif again in ("s", "S"):
         searchinfile()
    elif again in ("d", "D"):
         daysleft()
    elif again in ("f", "F"):
         finish()
    elif again in ("e", "E"):
         clean()
    elif again in ("a","A"):
         age()
    elif again in ("o","O"):
         openfile()
    elif again in ("l","L"):
         countlines()
    elif again in ("C","c"):
         copyline()
    elif again in ("M","m"):
         mail()
    elif again in ("B","b"):
         birthday()
    else:
        print()
        print(" That's not a possible option")
        print()
        restart()
    
def addtofile():
    
    print()
    possible = False
    raworder = 1
    while not possible:
        rawnum = input(" How many people?  ")
        file = open("Agenda.txt", "a+")
        if rawnum == "":
            print()
            print(" You should at least add one person")
            print()
        elif int(rawnum) >= 1:
            possible = True
        else:
            print()
            print(" You should at least add one person")
            print()
            
    
    for _ in range(int(rawnum)):
        order = str(raworder)

        print()
        iscomplete = False
        while not iscomplete:
            name = (input(" Name number " + order + "?  "))
            if name == "":
                print()
                print(" You must insert a name")
                print()
            else:
                iscomplete = True
                file.write(" ")
                file.write(name.title())
                file.write(" ")
                file.close
                file = open("Agenda.txt", "a+")
                print()
 
        
        surname = (input(" " + name.title() +"'s surname?  "))
        file.write(surname.title())
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()

        isdone = False
        while not isdone:
            
            rawbirthday = input (" When is " + name.title() + "'s birthday? (YYYY-MM-DD)  ")
            birthdaypattern = re.compile('\d{4}(?P<sep>[-])\d{2}(?P=sep)\d{2}')
            birthdaymatch = re.match(birthdaypattern, rawbirthday)
            
            if birthdaymatch :
                try:
                    year, month, day = map(int, rawbirthday.split("-")) 
                    birthday = date(year, month, day)
                    birthday_str = str(birthday)
                    file.write(birthday_str)
                    file.write(" | ")
                    file.close
                    file = open("Agenda.txt", "a+")
                    print()
                    isdone = True
                except:
                    print()
                    print(" That's not a valid date")
                    print()
            elif rawbirthday == "":
                isdone = True
                file.write(" ")
                file.write(" | ")
                file.close
                file = open("Agenda.txt", "a+")
                print()
            else:
                print()
                print(" That's not a valid date")
                print()
            

        relation = input(" How is " + name.title() + " related to you? ")
        file.write(relation.title())
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()

        alias = input(" " + name.title() + "'s alias? ")
        file.write(alias)
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()
        
        done = False
        while not done:
            email = input(" What is " + name.title() + "'s email? ")
            pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
            match = re.search(pattern, email)
            if match:
                file.write(email)
                file.write("\n")
                file.close
                done = True
                file = open("Agenda.txt", "a+")
            elif email == "":
                file.write("\n")
                file.close
                done = True
                file = open("Agenda.txt", "a+")
            else:
                print()
                print(" That's not a valid email, try again")
                file = open("Agenda.txt", "a+")

            print()
            raworder = raworder + 1

    file.close
    restart ()

def searchinfile():
    
    file = open("Agenda.txt", "r")
    print ()
    rawword = input (" Word to search:  (Enter or '.' for wildcard) ")
    print()
    word = rawword.title()
    
    s = " "
    rawcount = 1
    for i in track(range(10), description= " Processing..."):
        time.sleep(0.05)
    print()
    linets = []
    while(s):
        s = file.readline()
        l = re.split(("[ -]"), s)
        l_str = str(l)
        count = str(rawcount)
        if re.search(word, l_str):
            if s == "":
                linets.append(rawcount - 1)
            else:
                print(" Line " + count + ":" + s)
                linets.append(rawcount - 1)
        rawcount = rawcount + 1

    copyanswer = input(" Do you want to copy this line? (Y / Enter) ")
    if copyanswer in ("y", "Y"):

        file = open("Agenda.txt", "r") 
        line = file.readlines() 
        linetsnmb = 0
        if len(linets) == 1:
            linenmb = int(linets[int(linetsnmb)])
            pyperclip.copy (line[linenmb])
            linetsnmb = linetsnmb + 1
        else:
            linelist = []
            times = int(len(linets)-1)
            ttime = 0
            while ttime != times:
                linenmb = int(linets[int(linetsnmb)])
                linelist.append(line[linenmb])
                linetsnmb = linetsnmb + 1
                ttime = ttime + 1
            linelistcopy = "".join([str(x) for x in linelist])
            pyperclip.copy (linelistcopy)
        file.close
        restart()
    
    file.close
    restart()

def daysleft():
    
    print()
    rawchosendate = input(" What date do you want to operate with? (MM-DD) (Name) ")
    year = today.year
    try:
        month, day = map(int, rawchosendate.split("-"))
        chosendate = date(year, month, day)
        result = (chosendate - today)
        result_days_str = str(result.days)
        result_days_int = int(result_days_str)
        if result_days_int < 0:
            result_days_str = str(result.days)
            result_days_str = result_days_str.replace ('-', '')
            year2 = year + 1
            chosendate2 = date(year2, month, day)
            result2 = (chosendate2 - today)
            result2_days_str = str(result2.days)
            print()
            print(" You must insert a future date, that date happened", result_days_str, "days ago!, and will happen again in " + result2_days_str + " days.")
            print()
        elif result_days_int == 0:
            print()
            print(" That's today!")
            print()
        elif result_days_int > 0:
            print()
            print (" There are " + result_days_str + " days left")
            print()
        restart()
    except:
        w = " "
        nameline = ""
        rawchosennamedays = rawchosendate.title()
        chosennamedays = " " + rawchosennamedays + " "
        file = open("Agenda.txt", "r")
        year = today.year
        searchdayspattern = r"\-\d{2}\-\d{2}"
        while(w):
            w = file.readline()
            if re.search(chosennamedays, w):
                nameline = w
                break
        if re.search(searchdayspattern, nameline):
            rawrawdatematch = re.search(searchdayspattern, nameline)
            rawdatematch = rawrawdatematch.group()
            datematch = rawdatematch.split("-")
            del datematch[0]
            rawmonth, rawday = (datematch)
            month = int(rawmonth)
            day = int(rawday)
            chosendate = date(year, month, day)
            result = (chosendate - today)
            result_days_str = str(result.days)
            result_days_int = int(result_days_str)
            if result_days_int < 0:
                result_days_str = str(result.days)
                result_days_str = result_days_str.replace ('-', '')
                year2 = year + 1
                chosendate2 = date(year2, month, day)
                result2 = (chosendate2 - today)
                result2_days_str = str(result2.days)
                print()
                print(" You must insert a future date, that date happened", result_days_str, "days ago!, and will happen again in " + result2_days_str + " days.")
                print()
                restart()
            elif result_days_int == 0:
                print()
                print(" That's today!")
                print()
                restart()
            elif result_days_int > 0:
                print()
                print (" There are " + result_days_str + " days left")
                print()
                restart()
        
        else:           
            print()
            print(" Couldn't find the name or date (Or it was incorrect)")
            daysleft()

def finish():
    
    print()
    print(" Finishing...")
    time.sleep(0.7)
    print()
    print(" 3")
    time.sleep(0.7)
    print()
    print(" 2")
    time.sleep(0.7)
    print()
    print(" 1")
    time.sleep(0.7)
    
def clean():

    os.system("cls")
    choose()

def age():

    print()
    rawagedate = input(" What date do you want to operate with? (YY-MM-DD) (Name)  ")
    year = today.year
    try:
        year, month, day = map(int, rawagedate.split("-"))
        agedate = date(year, month, day)
        resultage = (today - agedate)
        resultage_days_str = str(resultage.days)
        resultage_days_int_raw = int(resultage_days_str)
        resultage_int = int(resultage_days_int_raw // 365.1)
        resultage_str = str(resultage_int)
        resultage_days_left_int_raw = resultage_days_int_raw - (resultage_int * 365.1)
        resultage_months_left_raw = resultage_days_left_int_raw // 30.4375
        resultage_months_left = str(int(resultage_months_left_raw))
        resultage_days_left_int_raw = resultage_days_left_int_raw - (resultage_months_left_raw * 30.4375)
        resultage_days_left = str(math.trunc(resultage_days_left_int_raw))
        if resultage_int < 0:
            print()
            print(" You must insert a past date, that date hasn't happened yet!")
            print()
        elif resultage_int == 0:
            print()
            print(" That's today!")
            print()
        elif resultage_int > 0:
            print()
            print (" The age is " + (resultage_str) + " years, " + (resultage_months_left) + " months and " + (resultage_days_left) + " days")
            print()
        restart()
    except:
        q = " "
        namelineq = ""
        rawagedateq = rawagedate.title()
        agedateq = " " + rawagedateq + " "
        file = open("Agenda.txt", "r")
        searchagepattern = r"\d{4}\-\d{2}\-\d{2}"
        while(q):
            q = file.readline()
            if re.search(agedateq, q):
                namelineq = q
                break
        if re.search(searchagepattern, namelineq):
            rawrawagedatematch = re.search(searchagepattern, namelineq)
            rawagedatematch = rawrawagedatematch.group()
            agedatematch = rawagedatematch.split("-")
            rawyear, rawmonth, rawday = (agedatematch)
            year = int(rawyear)
            month = int(rawmonth)
            day = int(rawday)
            agedate = date(year, month, day)
            resultage = (today - agedate)
            resultage_days_str = str(resultage.days)
            resultage_days_int_raw = int(resultage_days_str)
            resultage_int = int(resultage_days_int_raw // 365.1)
            resultage_str = str(resultage_int)
            resultage_days_left_int_raw = resultage_days_int_raw - (resultage_int * 365.1)
            resultage_months_left_raw = resultage_days_left_int_raw // 30.4375
            resultage_months_left = str(int(resultage_months_left_raw))
            resultage_days_left_int_raw = resultage_days_left_int_raw - (resultage_months_left_raw * 30.4375)
            resultage_days_left = str(math.trunc(resultage_days_left_int_raw))
            if resultage_int < 0:
                print()
                print(" You must insert a past date, that date hasn't happened yet!")
                print()
            elif resultage_int == 0:
                print()
                print(" That's today!")
                print()
            elif resultage_int > 0:
                print()
                print (" The age is " + (resultage_str) + " years, " + (resultage_months_left) + " months and " + (resultage_days_left) + " days")
                print()
            restart()
        else:
            print()
            print(" Couldn't find the name or date (Or it was incorrect)")
            age()

def openfile():

    print()
    whichfile = input(" Which file do you want to open? (Agenda -> A) (Settings -> S) (Birthdays -> B)  ")
    try:
        if whichfile in ("a","A"):
            print()
            os.startfile("Agenda.txt")
            restart()
        else:
            raise Exception
    except:
        try:
            if whichfile in ("b","B"):
                print()
                os.startfile("birthday.txt")
                restart()
            else:
                raise Exception
        except:
            try:
                if whichfile in ("s","S"):
                    print()
                    os.startfile("config.txt")
                    restart()
                else:
                    raise Exception
            except:
                try:
                    print()
                    print(" That file isn't available")
                    openfile()
                except:
                    openfile()

def countlines():

    file = open("Agenda.txt", "r")
    s = " "
    rawcountlines = 0
    
    
    while(s):
        s = file.readline()
        rawcountlines = rawcountlines + 1
    
    rawcountlines = rawcountlines - 1
    countlines = str(rawcountlines)
    print()
    print(" There are " + str(countlines) + " lines in the file")
    restart()

def copyline():
    
    print()
    rawline = int(input(" Line to copy: "))
    line = int(rawline) 
    file = open("Agenda.txt", "r") 
    line = file.readlines() 
    pyperclip.copy (line[(int(rawline)-1)])
    
    file.close
    restart()

def mail():

    file = open("Agenda.txt", "r")
    mailpattern = r"\w+@\w+\.\w+"
    print()
    w = " "
    rawchosennamemail = input(" What name is the mail linked to? ")
    chosennamemail = " " + rawchosennamemail.title() + " "
    namemailline =  " "
    while(w):
        w = file.readline()
        if re.search(chosennamemail, w):
            namemailline = w
            break
    if re.search(mailpattern, namemailline):
        rawmailmatch = re.search(mailpattern, namemailline)
        mailmatch = str(rawmailmatch.group())
        pyperclip.copy (mailmatch)
        print()
        answergmail = input(" Copied to clipboard, do you want to open gmail? (Y / Enter) ")
        if answergmail in ("y", "Y"):

                raconfig = setting()
                config = str(raconfig[0])

                if config == "gmail":
                    if exists("Gmail.lnk"):
                        os.system ("cd C:\Program Files (x86)\Microsoft\Edge\Application & msedge_proxy.exe --profile-directory=Default --app-id=fmgjjmmmlfnkbppncabfkddbjimcfncm --app-url=https://mail.google.com/mail/?usp=installed_webapp --app-launch-source=4")
                        choose()
                    else: 
                        webbrowser.open('https://mail.google.com/mail/u/0/')
                        choose()
                elif config == "outlook":
                    webbrowser.open('https://outlook.live.com/mail/0/')
                else: 
                    print(" The congig file has an unsupported email provider")
        else:
            choose()
    else:           
        print()
        print(" Couldn't find the name or mail")
        mail()

def setting():

    with open("config.txt") as settingsfile:
        settings = list(settingsfile)[0::2]
    settings = ([s.replace('\n', '') for s in settings])
    return settings

def birthday():
  
    print()
    rawchosendate = input(" What birthday do you want to be reminded of? (Name) ")
    w = " "
    nameline = ""
    rawchosennamedays = rawchosendate.title()
    chosennamedays = " " + rawchosennamedays + " "
    file = open("Agenda.txt", "r")
    searchdayspattern = r"\-\d{2}\-\d{2}"
    while(w):
        w = file.readline()
        if re.search(chosennamedays, w):
            nameline = w
            break
    if re.search(searchdayspattern, nameline):
        rawrawdatematch = re.search(searchdayspattern, nameline)
        rawdatematch = rawrawdatematch.group()
        datematch = rawdatematch.split("-")
        file.close
        del datematch[0]
        rawmonth, rawday = (datematch)
        file = open("birthday.txt", "a+")
        file.write("\n")
        file.write(" " + rawchosennamedays + " | " + rawmonth + "-" + rawday + " ")
        print()
        print (" This birthday has been added to list")
        file.close()
        restart()
        
    else:           
        print()
        print(" Couldn't find the name or date (Or it was incorrect)")
        birthday()
        
choose()

#add calendar support      os.startfile (r"C:\Users\Jorge\Desktop\Calendario (2).lnk")