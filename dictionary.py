
storeinv=[{
    "name": "Brisk",
    "price": 2.50,
    "type": "Iced Tea"
},
{
    "name": "Pop Corners",
    "price": 3.00,
    "type": "chips"
},
{
    "name": "Watermelon gum",
    "price": 2.00,
    "type": "gum"
}]
buying=True
cart=[]
receipt=0
while buying:
    print("What would you like to buy? 1. drinks 2. chips 3. gum ")
    result=int(input("1 2 or 3: "))
    result-=1
    formed=storeinv[result]
    cart.append(formed)
    receipt+=(formed["price"])

    ans=input("would you like to continue? y/n ")
    if ans == "y":
        buying=True
    elif ans=="n":
        buying=False
        print(cart)
        print(f"price:{receipt}")
        
        
"""
    if result=="drinks":
        receipt+=2.5
        cart+=[storeinv[0]["type"],storeinv[0]["name"],storeinv[0]["price"]]
        print(receipt)
    elif result=="chips":
        receipt+=3
        cart+=[storeinv[1]["type"],storeinv[1]["name"],storeinv[1]["price"]]
        print(receipt)
    elif result=="gum":
        receipt+=2
        cart+=[storeinv[2]["type"],storeinv[2]["name"],storeinv[2]["price"]]
        print(receipt) """