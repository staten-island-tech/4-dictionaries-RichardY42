drinks={
    "name": "Brisk",
    "price": 2.50,
    "type": "Iced Tea"
}
chips={
    "name": "Pop Corners",
    "price": 3.00,
    "type": "chips"
}
gum={
    "name": "Watermelon gum",
    "price": 2.00,
    "type": "gum"
}
done=False
cart=[]
receipt=()
while done==False:
    print("What would you like to buy?")
    result=input("drinks  chips  gum ")
    if result=="drinks":
        cart+=[drinks["name"]]
        cart+=float([drinks["price"]])
        receipt+="Brisk: $2.50"
    elif result=="chips":
        cart+=[chips["name"]]
        cart+=float([chips["price"]])
        
    elif result=="gum":
        cart+=[gum["name"]]
        cart+=float([gum["price"]])
    ans=input("would you like to continue? y/n ")
    if ans == "y":
        done=False
    elif ans=="n":
        done=True
        print(cart)
        if val in cart== float:
            