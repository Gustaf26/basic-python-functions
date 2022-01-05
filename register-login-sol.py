# REGISTER USER - LOG IN

import random
import string

ascii = string.punctuation
alphabet = "abcdefghijklmnopqrstuvwxyz" 

my_password='Pelle_svanslos'
anvandarNamn=''

def dispatch(): 
    def generatePass(anvNamn): 
        nyttLosen =""
        global my_password
        for i in range(0,9):
            nyttLosen += alphabet[random.randrange(26)]
            nyttLosen +=ascii[random.randrange(len(ascii))]
            my_password=nyttLosen
        # Skriv här
        print(f'Användare {anvNamn} med password {nyttLosen} har skapats')
        dispatch()

    def login():
        global anvandarNamn
        anvNamn = input('Var vänlig ange ditt användarnamn: ')
        if anvandarNamn == anvNamn:
            loginPass=input('Var vänlig ange ditt lösenord: ')
            if loginPass==my_password:
                print('Du är inloggad')
            else:
                print('Lösenordet är inte korrekt')
                login()
        else:
            register()

    def register():
        global anvandarNamn
        anvandarNamn = input('Du ska registreras. Var vänlig ange ett användarnamn: ')
        global my_password
        if anvandarNamn:
            answer = input(f"Hej {anvandarNamn}, vill du att jag ska ge dig ett nytt lösenord? ")
            if answer =='ja':
                generatePass(anvandarNamn)
            else:
                my_password = input(f"Hej {anvandarNamn}, skriv ditt eget nya lösenord: ")
                print(f'Användare {anvandarNamn} med password {my_password} har skapats')
                dispatch()
        else:
            register()

    action=input('Ange ett av tre val: 1. Logga in, 2. Registrera, 3. Avbryta: ')
    if action=="1":
        login()
    elif action=="2":
        register()
    elif action=='3':
        print('Tack för besöket, välkommen tillbaka')
        return
    else:
        print('Du måste ange en action')
        dispatch()
dispatch()
