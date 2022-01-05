# E-COMMERCE CMR
# 
# Beginning of a e-commerce CMR where we apply different discounts to each 
# product category (pants-10%, sweaters-5%, t-shirts-20%) and pick them up and VAT
# and campaign info from a list (dynamically)
#
# You first ask what type of product it is and then it
# prints out the price - discount + VAT for each product / price
#
# At the end you print out the total sum for all the prizes as well
# as kampanjinfon

category = input("Enter the product category: ")
products = int(input("Enter the number of products: "))
i = 0
sum = 0
trouss_info = [10, 20, "No campaign offers"]
tshirts_info = [20, 20, "Three for two"]
sweaters_info = [5, 20, "Buy now, pay on one month"]

def countTroussers(pris, info):
    for b in range(len(info)):
            if b==0:
               discount = pris*info[b]/100
               pris -=discount
            elif b==1:
               moms = pris*info[b]/100
               pris +=moms
    print(f"Product price with discount and moms is: {pris}")
    return pris

def countTshirts(pris,info):
    for b in range(len(info)):
            if b==0:
               discount = pris*info[b]/100
               pris -=discount
            elif b==1:
               moms = x*info[b]/100
               pris +=moms
    print(f"Product price with discount and moms is: {pris}")
    return pris

def countSweaters(pris,info):
    for b in range(len(info)):
            if b==0:
               discount = pris*info[b]/100
               pris -=discount
            elif b==1:
               moms = pris*info[b]/100
               pris +=moms
    print(f"Product price with discount and moms is: {pris}")
    return pris

for i in range(products):
    
    x = float(input("Enter a product price: "))
    if category == "byxor":
       x =  countTroussers(x, trouss_info)
    elif category=='t-shirts':
       x =   countTshirts(x,tshirts_info)
    elif category=="tröjor":
       x =  countSweaters(x,sweaters_info)
    sum +=x

print(f" The total price for {category} is: {round(sum)} sek" )

def give_info(category):
    if category=='byxor':
       print(f"Campaign info: {trouss_info[2]}")
    elif category=='tröjor':
       print(f"Campaign info: {sweaters_info[2]}")
    else:
       print(f"Campaign info: {tshirts_info[2]}")

give_info(category)
