#Eng or Fren determiner
"""def langd(x):
    eng=0
    fren=0
    for ltr in x:
        if ltr == "t" or ltr =="T":
            eng+=1
        if ltr=="s" or ltr == "S":
            fren+=1
    if eng>fren:
        print("english")
    elif eng<fren:
        print("french")
#print(eng)
#print(fren)
langd("Lorsque j'avais six ans j'ai vu, une fois,")"""
#Occupy Spaces 

def idk(x,y,t):
    occuty=0
    for o in range(x):
        if y[o]== "o" and t[o]=="o":
            occuty+=1
    print(occuty)
    #print(times)
idk(6,".o.oo.","o..oo")


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
receipt=[]
while done==False:
    print("What would you like to buy?")
    result=input("drinks  chips  gum ")
    if result=="drinks":
        #cart+=[drinks["name"]]
        cart+=[drinks["price"]]
        receipt+=["Brisk: $2.50"]
    elif result=="chips":
        #cart+=[chips["name"]]
        cart+=[chips["price"]]
        receipt+=["Pop Corners: $3.00"]
    elif result=="gum":
        #cart+=[gum["name"]]
        cart+=[gum["price"]]
        receipt+=["Watermelon gum: $2.00"]
    ans=input("would you like to continue? y/n ")
    if ans == "y":
        done=False
    elif ans=="n":
        done=True
        print(receipt)
        print(f"Total: ${sum(cart)}")
        
        
            
