
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
done=False
cart=[]

while done==False:
    print("What would you like to buy?")
    result=input("drinks  chips  gum ")
    if result=="drinks":
        cart+=[storeinv[0]["name"],storeinv[0]["price"],storeinv[0]["type"]]
        # cart+=[drinks["price"]]
    elif result=="chips":
        cart+=[storeinv[1]["name"],storeinv[1]["price"],storeinv[1]["type"]]
        # cart+=[chips["price"]]
    elif result=="gum":
        cart+=[storeinv[2]["name"],storeinv[2]["price"],storeinv[2]["type"]]
        # cart+=[gum["price"]]
    ans=input("would you like to continue? y/n ")
    if ans == "y":
        done=False
    elif ans=="n":
        done=True
        print(cart)
        for 
        print(f"Total: ${sum(cart[storeinv["price"]])}")
        
        
            