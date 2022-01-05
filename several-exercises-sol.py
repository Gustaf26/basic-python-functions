# 1. Define a function that accepts 2 values and returns
# its sum, subtraction and multiplication.

# SOLUTION:

def result(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    print(f"Sum is {sum}, Sub is {sub}, & Multiply is {mul}")

a = int(input("Enter value of a: "))  
b = int(input("Enter value of b: "))  
result(a,b)

# 2. Define a function in python that accepts 3 digits
# and returns the highest of the three digits

def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum among all")
    elif b > a and b > c:
        print(f"{b} is maximum among all")
    else:
        print(f"{c} is maximum among all")

max(30,22,18)

# 3. Define a function that counts vowels
# and consonants in a word that you send in.

def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con + 1

    print("Count of vowels is ",vov)
    print("Count of consonant is ",con)

x = input("Enter a word: ") 
count(x)