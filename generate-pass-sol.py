# GENERATE SECURE PASS

# The function below gives us a secure password with random
# letters and ascii characters (not more than 18 in total)
import random
import string

ascii = string.punctuation
alphabet = "abcdefghijklmnopqrstuvwxyz" 
  
# function to generate a random string 
def generatePass(): 
    res =""
    for i in range(0,9):
        res += alphabet[random.randrange(27)]
        res +=ascii[random.randrange(len(ascii))]
          
    return res

mynewpass = generatePass()
print(mynewpass)