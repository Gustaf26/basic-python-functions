# REGISTER USER - LOG IN

# Work on creating a program yourself that creates a new user with a generated password
# or with your own password, and lets the new user log in
 
# It should have 4 functions:

# First a main function dispatch () that calls for 3 action functions inside it:
# login, register or cancel

# In dispatch you are asked "what do you want to do"?

# If you want to register, call the register () function,
# and there you can choose to get a new password - called on generatePass (), see below-
# or to enter a new password yourself. Then you call the main function again dispatch ()

# generatePass () generates a new password with ascii characters
# and letters (18 characters in total) -you can use the modules random and string for it-,
# prints the username and the new password eg print (f'User {username} with password {newLoss}
# has been created ') and then calls dispatch () again

# The login () function is simple. If you enter the correct username and password, it will be printed ('You
# is logged in '), otherwise printed (' Wrong password, try again ') and login () is called again

# Action Cancel should only end the dispatch () function with a return

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

    def login():
        global anvandarNamn
        

    def register():
        global anvandarNamn
        anvandarNamn = input('Du ska registreras. Var vänlig ange ett användarnamn: ')
        global my_password
        

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