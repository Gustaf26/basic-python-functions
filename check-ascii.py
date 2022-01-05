# CHECK ASCII SIGNS IN PASSWORD:

# Defines a function that receives a list of 3 passwords
# and check if there are any ASCII characters ['#', '$', '%'] in any of them ¨
#  and print 'There are ascci symbols in your passwords' if any
# or 'There are no ascci symbols in your passwords' otherwise. It ends then
# the function with return

def checkAscii(lista):
    ascii = ['#', '$', '%']
    if len(lista)==3:
        for symb in ascii:
            i=0
            while i<len(lista):
                if symb in lista[i]:
                    print('There are ascci symbols in your passwords')
                    return
                i +=1
        else:
            print('There are no ascci symbols in your passwords')
            return
    else:
        print('give me 3 valid passwords separated by space, please')
        checkAscii(list(input("Enter a list of passwords: ").strip().split()))

x = list(input("Enter a list of passwords separated by space: ").strip().split()) 
checkAscii(x)