
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
    configfile.write("english")
    configfile.write("\n")
    configfile.write("# Choose your preferred language: 'english', 'spanish'")
    configfile.close

if not exists("birthday.txt"):
    birthdayfile = open("birthday.txt", "w+")
    birthdayfile.write("# This file is used to store birthdays the user wants to be reminded of")
    birthdayfile.close


def choose():
    
    if not langconfig == "spanish":

        print ()
        print (" W -> Write names ")
        print (" S -> Search in agenda ")
        print (" D -> Days left ")
        print (" A -> Age ")
        print (" O -> Open file ")
        print (" E -> Erase ")
        print (" L -> Lines in agenda ")
        print (" F -> Finish ")
        print (" C -> Copy line ")
        print (" M -> Mail ")
        print (" B -> Birthdays ")
        print (" R -> Run Program ")
        print (" P -> Phone ")
        print ()
        time.sleep(0.2)

        rawoption = input(" What do you want to do? (W / S / D / A / O / E / L / F / C / M / B / R / P)  ")
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
        elif option in ("R","r"):
         run()
        elif option in ("P", "p"):
         phone()
        else:
            print()
            print(" That's not a possible option")
            choose()
    else:

        print ()
        print (" W -> Añadir nombres ")
        print (" S -> Buscar en agenda ")
        print (" D -> Días restantes ")
        print (" A -> Edad ")
        print (" O -> Abrir archivo ")
        print (" E -> Borrar ")
        print (" L -> Líneas en agenda ")
        print (" F -> Finalizar ")
        print (" C -> Copiar linea ")
        print (" M -> Correo ")
        print (" B -> Cumpleaños ")
        print (" R -> Ejecutar programa ")
        print (" P -> Teléfono ")
        print ()
        time.sleep(0.2)

        rawoption = input(" ¿Qué quieres hacer? (W / S / D / A / O / E / L / F / C / M / B / R / P)  ")
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
        elif option in ("R","r"):
         run()
        elif option in ("P", "p"):
         phone()
        else:
            print()
            print(" Esa no es una opción posible")
            choose()
    
def restart():  
    
    if not langconfig == "spanish":

        time.sleep(0.5)
        print ()
        print (" W -> Write names ")
        print (" S -> Search in agenda ")
        print (" D -> Days left ")
        print (" A -> Age ")
        print (" O -> Open file ")
        print (" E -> Erase ")
        print (" L -> Lines in agenda ")
        print (" F -> Finish ")
        print (" C -> Copy line ")
        print (" M -> Mail ")
        print (" B -> Birthdays ")
        print (" R -> Run Program ")
        print (" P -> Phone ")
        print()
        time.sleep(0.5)
        rawagain = input(" Anything else? (W / S / D / A / O / E / L / F / C / M / B / R / P)  ")
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
        elif again in ("R","r"):
         run()
        elif again in ("P","p"):
         phone()
        else:
            print()
            print(" That's not a possible option")
            restart()
    else:
        time.sleep(0.5)
        print ()
        print (" W -> Añadir nombres ")
        print (" S -> Buscar en agenda ")
        print (" D -> Días restantes ")
        print (" A -> Edad ")
        print (" O -> Abrir archivo ")
        print (" E -> Borrar ")
        print (" L -> Lineas en agenda ")
        print (" F -> Finalizar ")
        print (" C -> Copiar linea ")
        print (" M -> Correo ")
        print (" B -> Cumpleaños ")
        print (" R -> Ejecutar programa ")
        print (" P -> Teléfono ")
        print()
        time.sleep(0.5)
        rawagain = input(" ¿Algo más? (W / S / D / A / O / E / L / F / C / M / B / R / P)  ")
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
        elif again in ("R","r"):
         run()
        elif again in ("P","p"):
         phone()
        else:
            print()
            print(" Esa no es una opción posible")
            restart()
    
def addtofile():
    
    print()
    possible = False
    raworder = 1
    while not possible:
        if not langconfig == "spanish":
            rawnum = input(" How many people?  ")
        else:
            rawnum = input (" ¿Cuántas personas? ")

        if rawnum == " ":
            print()
            print(" -")
            choose()

        file = open("Agenda.txt", "a+")
        if rawnum == "":
            print()
            if not langconfig == "spanish":
                print(" You should at least add one person")
            else: 
                print(" Debe ser mínimo una persona")
            print()
        elif int(rawnum) >= 1:
            possible = True
        else:
            print()
            if not langconfig == "spanish":
                print(" You should at least add one person")
            else: 
                print(" Debe ser mínimo una persona")
            print()
            
    
    for _ in range(int(rawnum)):
        order = str(raworder)

        print()
        iscomplete = False
        while not iscomplete:

            if not langconfig == "spanish":
                name = (input(" Name number " + order + "?  "))
            else:
                name = (input(" ¿Nombre número " + order + "?  "))

            if name == " ":
                print()
                print(" -")
                choose()

            if name == "":
                print()
                if not langconfig == "spanish":
                    print(" You must insert a name")
                else: 
                    print(" Debes insertar un nombre")
                print()
            else:
                iscomplete = True
                file.write(" ")
                file.write(name.title())
                file.write(" ")
                file.close
                file = open("Agenda.txt", "a+")
                print()
 
        if not langconfig == "spanish":
            surname = (input(" " + name.title() +"'s surname?  "))
        else: 
            surname = (input(" ¿Apellidos de " + name.title() +"?  "))
        file.write(surname.title())
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()

        isdone = False
        while not isdone:
            
            if not langconfig == "spanish":
                rawbirthday = input (" When is " + name.title() + "'s birthday? (YYYY-MM-DD)  ")
            else: 
                rawbirthday = input (" ¿Cuándo es el cumpleaños de " + name.title() + "? (YYYY-MM-DD)  ")
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
                    if not langconfig == "spanish":
                        print(" That's not a valid date")
                    else:
                        print(" Esa no es una fecha válida")
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
                if not langconfig == "spanish":
                    print(" That's not a valid date")
                else:
                    print(" Esa no es una fecha válida")
                print()
            
        if not langconfig == "spanish":
            relation = input(" How is " + name.title() + " related to you?  ")
        else:
            relation = input(" ¿Cuál es tu relación con " + name.title() + "?  ")
        file.write(relation.title())
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()

        if not langconfig == "spanish":
            alias = input(" " + name.title() + "'s alias? ")
        else:
            alias = input(" ¿Cuál es el apodo de " + name.title() + "?  ")
        file.write(alias)
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()

        if not langconfig == "spanish":
            phonenumber = (input(" " + name.title() +"'s phone number?  "))
        else:
            phonenumber = (input(" ¿Cuál es el número de teléfono de " + name.title() +"?  "))
        file.write(phonenumber)
        file.write(" | ")
        file.close
        file = open("Agenda.txt", "a+")
        print()
        
        done = False
        while not done:
            if not langconfig == "spanish":
                email = input(" What is " + name.title() + "'s email? ")
            else:
                email = input(" ¿Cuál es el email de " + name.title() + "? ")
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
                if not langconfig == "spanish":
                    print(" That's not a valid email, try again")
                else:
                    print(" Ese no es un email válido, vuelve a intentarlo")
                file = open("Agenda.txt", "a+")

            print()
            raworder = raworder + 1

    file.close
    restart ()

def searchinfile():
     
    file = open("Agenda.txt", "r")
    print ()
    if not langconfig == "spanish":
        rawword = input (" Word to search  (Enter or '.' for wildcard): ")
    else:
        rawword = input(" Palabra a buscar (Enter o '.' para comodín): ")

    if rawword == " ":
        print()
        print(" -")
        choose()

    print()
    word = rawword.title()
    
    s = " "
    rawcount = 1
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
                if not langconfig == "spanish":
                    print(" Line " + count + ":" + s)
                else:
                    print(" Línea" + count + ":" + s)
                linets.append(rawcount - 1)
        rawcount = rawcount + 1

    file.close()

    if len(linets) < 1:
        if not langconfig == "spanish":
            print(" There is nothing to copy")
        else:
            print(" No hay nada que copiar")
    else:
        if not langconfig == "spanish":
            copyanswer = input(" Do you want to copy this line? (Y / Enter) ")
        else:
            copyanswer = input(" ¿Quieres copiar esta línea? (Y / Enter) ")
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
                times = int(len(linets))
                ttime = 0
                while ttime < (times-1):
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
    if not langconfig == "spanish":
        rawchosendate = input(" What date do you want to operate with? (MM-DD) (Name) ")
    else:
        rawchosendate = input(" ¿Con qué fecha quieres operar? (MM-DD) (Nombre) ")

    if rawchosendate == " ":
        print()
        print(" -")
        choose()

    if str(rawchosendate) == "":
        print()
        if not langconfig == "spanish":
            print(" Couldn't find the name or date (Or it was incorrect)")
        else:
            print(" No se encontró el nombre o fecha (O era incorrecto)")
        daysleft()
    else:
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
                if not langconfig == "spanish":
                    print(" You must insert a future date, that date happened", result_days_str, "days ago!, and will happen again in " + result2_days_str + " days.")
                else:
                    print(" Debes insertar una fecha futura, esa fecha ocurrió hace", result_days_str, "días!, y volverá a ocurrir en " + result2_days_str + " días.")
            elif result_days_int == 0:
                print()
                if not langconfig == "spanish":
                    print(" That's today!")
                else:
                    print(" Eso es hoy!")
            elif result_days_int > 0:
                print()
                if not langconfig == "spanish":
                    print (" There are " + result_days_str + " days left")
                else:
                    print (" Quedan " + result_days_str + " días")
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
                    if not langconfig == "spanish":
                        print(" You must insert a future date, that date happened", result_days_str, "days ago!, and will happen again in " + result2_days_str + " days.")
                    else:
                        print(" Debes insertar una fecha futura, esa fecha ocurrió hace", result_days_str, "días!, y volverá a ocurrir en " + result2_days_str + " días.")
                    restart()
                elif result_days_int == 0:
                    print()
                    if not langconfig == "spanish":
                        print(" That's today!")
                    else:
                        print(" Eso es hoy!")
                    restart()
                elif result_days_int > 0:
                    print()
                    if not langconfig == "spanish":
                        print (" There are " + result_days_str + " days left")
                    else: 
                        print (" Quedan " + result_days_str + " días")
                    restart()
        
        else:           
            print()
            if not langconfig == "spanish":
                print(" Couldn't find the name or date (Or it was incorrect)")
            else:
                print(" No se encontró el nombre o la fecha (O era incorrecto)")
            daysleft()

def finish():
    
    print()
    if not langconfig == "spanish":
        print(" Finishing...")
    else:
        print(" Finalizando...")
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
    quit()
    
def clean():

    os.system("cls")
    choose()

def age():

    print()
    if not langconfig == "spanish":
        rawagedate = input(" What date do you want to operate with? (YY-MM-DD) (Name)  ")
    else:
        rawagedate = input(" ¿Con qué fecha quieres operar? (YY-MM-DD) (Nombre)  ")

    if rawagedate == " ":
        print()
        print(" -")
        choose()

    if str(rawagedate) == "":
        print()
        if not langconfig == "spanish":
            print(" Couldn't find the name or date (Or it was incorrect)")
        else:
            print(" No se encontró el nombre o la fecha (O era incorrecto)")
        daysleft()
    else:
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
                if not langconfig == "spanish":
                    print(" You must insert a past date, that date hasn't happened yet!")
                else: 
                    print(" Debes insertar una fecha pasada, esa fecha no ha ocurrido aún!")
            elif resultage_int == 0:
                print()
                if not langconfig == "spanish":
                    print(" That's today!")
                else:
                    print(" Eso es hoy!")
            elif resultage_int > 0:
                print()
                if not langconfig == "spanish":
                    print (" The age is " + (resultage_str) + " years, " + (resultage_months_left) + " months and " + (resultage_days_left) + " days")
                else:
                    print (" La edad es " + (resultage_str) + " años, " + (resultage_months_left) + " meses y " + (resultage_days_left) + " días")
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
                    if not langconfig == "spanish":
                        print(" You must insert a past date, that date hasn't happened yet!")
                    else:
                        print(" Debe sinsertar una fecha pasada, esa fecha no ha ocurrido aún!")
                elif resultage_int == 0:
                    print()
                    if not langconfig == "spanish":
                        print(" That's today!")
                    else:
                        print(" Eso es hoy!")
                elif resultage_int > 0:
                    print()
                    if not langconfig == "spanish":
                        print (" The age is " + (resultage_str) + " years, " + (resultage_months_left) + " months and " + (resultage_days_left) + " days")
                    else:
                        print (" La edad es " + (resultage_str) + " años, " + (resultage_months_left) + " meses y " + (resultage_days_left) + " días")
                restart()
        else:
            print()
            if not langconfig == "spanish":
                print(" Couldn't find the name or date (Or it was incorrect)")
            else:
                print(" No se encontró el nombre o la fecha (O era incorrecto)")
            age()

def openfile():

    print()
    if not langconfig == "spanish":
        whichfile = input(" Which file do you want to open? (Agenda -> A) (Settings -> S) (Birthdays -> B)  ")
    else:
        whichfile = input(" ¿Qué archivo quieres abrir? (A -> Agenda) (S -> Ajustes) (B -> Cumpleaños)  ")

    if whichfile == " ":
        print()
        print(" -")
        choose()

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
                    if not langconfig == "spanish":
                        print(" That file isn't available")
                    else:
                        print(" Ese archivo no está disponible")
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
    if not langconfig == "spanish":
        print(" There are " + str(countlines) + " lines in the file")
    else:
        print(" Hay " + str(countlines) + " líneas en el documento")
    restart()

def copyline():
    
    print()
    if not langconfig == "spanish":
        rawrawline = (input(" Line to copy: "))
    else:
        rawrawline = (input(" Línea a copiar: "))

    if rawrawline == " ":
        print()
        print(" -")
        choose()

    if rawrawline == "":
        print()
        if not langconfig == "spanish":
            print(" Couldn't find that line")
        else:
            print(" No se encontró esa línea")
        copyline()
    else:
        try:
            rawline = int(rawrawline)
            line = int(rawline) 
            file = open("Agenda.txt", "r") 
            line = file.readlines() 
            pyperclip.copy (line[(int(rawline)-1)])
            print()
            if not langconfig == "spanish":
                print(" Line copied")
            else:
                print(" Línea copiada")
        except:
            print()
            if not langconfig == "spanish":
                print(" Couldn't find that line")
            else:
                print(" No se encontró esa línea")
            copyline()
    
    file.close
    restart()

def mail():

    file = open("Agenda.txt", "r")
    mailpattern = r"\w+@\w+\.\w+"
    print()
    w = " "
    if not langconfig == "spanish":
        rawchosennamemail = input(" What name is the mail linked to? ")
    else:
        rawchosennamemail = input(" ¿A qué nombre está asociado el correo? ")

    if rawchosennamemail == " ":
        print()
        print(" -")
        choose()

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
        if not langconfig == "spanish":
            answergmail = input(" Copied to clipboard, do you want to open mail? (Y / Enter) ")
        else:
            answergmail = input(" Copiado al portapapeles, ¿quieres abrir el mail? (Y / Enter) ")
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
                    print()
                    if not langconfig == "spanish":
                        print(" The config file has an unsupported email provider")
                    else:
                        print(" El archivo de configuración tiene un proveedor de email no soportado") 
                    restart()
        else:
            choose()
    else:           
        print()
        if not langconfig == "spanish":
            print(" Couldn't find the name or mail")
        else:
            print(" No se encontró el nombre o mail")
        mail()

def setting():

    with open("config.txt") as settingsfile:
        settings = list(settingsfile)[0::2]
    settings = ([s.replace('\n', '') for s in settings])
    return settings

def birthday():
  
    print()
    if not langconfig == "spanish":
        rawchosendate = input(" What birthday do you want to be reminded of? (Name) ")
    else:
        rawchosendate = input(" ¿De qué cumpleaños quieres ser notificado? (Nombre) ")

    if rawchosendate == " ":
        print()
        print(" -")
        choose()

    w = " "
    nameline = ""
    rawchosennamedays = rawchosendate.title()
    chosennamedays = " " + rawchosennamedays + " "
    file = open("Agenda.txt", "r")
    searchdayspattern = r"\-\d{2}\-\d{2}"
    rawmonth = ""
    rawday = ""
    while(w):
        w = file.readline()
        if re.search(chosennamedays, w):
            nameline = w
            break
    if re.search(searchdayspattern, nameline):
        if rawchosendate == "":
            print()
            if not langconfig == "spanish":
                print(" No person has been found with that name")
            else:
                print(" Ninguna persona fue encontrada con ese nombre")
            birthday()
        else:
            rawrawdatematch = re.search(searchdayspattern, nameline)
            rawdatematch = rawrawdatematch.group()
            datematch = rawdatematch.split("-")
            file.close
            del datematch[0]
            rawmonth, rawday = (datematch)
            print()
            if not langconfig == "spanish":
                nametoadd = input(" What name do you want this date to be associated with? ")
            else:
                nametoadd = input(" ¿Con qué nombre quieres que esté asociado? ")
            if nametoadd == "":
                file = open("birthday.txt", "a+")
                file.write("\n")
                file.write(" " + rawchosennamedays + " | " + rawmonth + "-" + rawday + " ") 
            else:
                file = open("birthday.txt", "a+")
                file.write("\n")
                file.write(" " + nametoadd + " | " + rawmonth + "-" + rawday + " ")
            print()
            if not langconfig == "spanish":
                print (" This birthday has been added to list")
            else:
                print (" Este cumpleaños ha sido añadido a la lista")
            file.close()
            restart()
        
    else:           
        print()
        if not langconfig == "spanish":
            print(" Couldn't find the name or date (Or it was incorrect)")
        else:
            print (" No se encontró el nombre o la fecha (O era incorrecto)")
        birthday()

def run():
    
    print()
    if not langconfig == "spanish":
        whichprogram = input(" Which program do you want to run? (Birthday -> B) (Calendar -> C) (Task Manager -> T) (Mail -> M) ")
    else:
        whichprogram = input(" ¿Qué programa quieres ejecutar? (Cumpleaños -> B) (Calendario -> C) (Gestor de tareas -> T) (Mail -> M) ")

    if whichprogram in ("B","b"):
        os.startfile("BirthdaysCheck.pyw")
        restart()

    elif whichprogram in ("c","C"):

        runconfig = setting()
        rconfig = str(runconfig[2])

        if rconfig == "windows":
            os.startfile (r"C:\Users\Jorge\Desktop\WindowsCalendar.lnk")
            restart()
        elif rconfig == "google":
            webbrowser.open ("https://calendar.google.com/calendar/")
            restart()
        else:
            print()
            if not langconfig == "spanish":
                print(" The config file has an unsupported calendar provider")
            else:
                print( " La configuración tiene un proveedor de calendario no soportado")
            restart()

    elif whichprogram in ("m","M"):

        raconfig = setting()
        config = str(raconfig[0])

        if config == "gmail":
            if exists("Gmail.lnk"):
                os.system ("cd C:\Program Files (x86)\Microsoft\Edge\Application & msedge_proxy.exe --profile-directory=Default --app-id=fmgjjmmmlfnkbppncabfkddbjimcfncm --app-url=https://mail.google.com/mail/?usp=installed_webapp --app-launch-source=4")
                restart()
            else: 
                webbrowser.open('https://mail.google.com/mail/u/0/')
                restart()
        elif config == "outlook":
                webbrowser.open('https://outlook.live.com/mail/0/')
        else: 
            print()
            if not langconfig == "spanish":
                print(" The config file has an unsupported email provider")
            else:
                print( " La configuración tiene un proveedor de correo no soportado")
            restart()

    elif whichprogram in ("T","t"):

        runconfig = setting()
        rconfig = str(runconfig[3])

        if rconfig == "mystudylife":
            os.system ("cd C:\Program Files (x86)\Microsoft\Edge\Application & msedge_proxy.exe  --profile-directory=Default --app-id=jadpjgflkokghajgdbeojainkclgmiap --app-url=https://app.mystudylife.com/dashboard --app-launch-source=4")
            restart()
        elif rconfig == "todoist":
            os.startfile (r"C:\Users\Jorge\AppData\Local\Programs\todoist\Todoist.exe")
            restart()
        else:
            print()
            if not langconfig == "spanish":
                print(" The config file has an unsupported manager provider")
            else:
                print( " La configuración tiene un gestor de tareas no soportado")
            restart()

    if whichprogram == " ":
        print()
        print(" -")
        choose()

    else:
        print()
        if not langconfig == "spanish":
            print(" That program isn't available ")
        else:
            print(" Ese programa no está disponible ")
        run()

def phone():
    file = open("Agenda.txt", "r")
    phonepattern = r"\d\d\d\d\d\d\d\d\d"
    print()
    w = " "
    if not langconfig == "spanish":
        rawchosennamephone = input(" What name is the phone number linked to? ")
    else:
        rawchosennamephone = input(" ¿Con qué nombre está asociado? ")

    if rawchosennamephone == "":
        if not langconfig == "spanish":
            print()
            print (" You need to enter a name")
            phone()
        else:
            print()
            print (" Es necesario insertar un nombre")
            phone()

    if rawchosennamephone == " ":
        print()
        print(" -")
        choose()

    chosennamephone = " " + rawchosennamephone.title() + " "
    namephoneline =  " "
    while(w):
        w = file.readline()
        if re.search(chosennamephone, w):
            namephoneline = w
            break
    if re.search(phonepattern, namephoneline):
        rawphonematch = re.search(phonepattern, namephoneline)
        phonematch = str(rawphonematch.group())
        pyperclip.copy (phonematch)
        print()
        if not langconfig == "spanish":
            answerphone = input(" Copied to clipboard, do you want to open whatsapp? (Y / Enter) ")
        else:
            answerphone = input(" Copiado al portapapeles, ¿quieres abrir whatsapp? (Y / Enter) ")
        if answerphone in ("y", "Y"):

            if exists("Whatsapp.lnk"):
                os.startfile (r"C:\Jorge\Python\WhatsApp.lnk")
                choose()
            else: 
                webbrowser.open('https://web.whatsapp.com/')
                choose()

        else:
            choose()
    else:           
        print()
        if not langconfig == "spanish":
            print(" Couldn't find the name or phone number")
        else:
            print(" No se encontró el nombre o número de teléfono")
        mail()

languageconfig = setting()
langconfig = str(languageconfig[4])

choose() 

#windows calendar api to add birthdays to calendar when added to reminder