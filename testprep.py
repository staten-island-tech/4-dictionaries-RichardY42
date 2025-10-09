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
