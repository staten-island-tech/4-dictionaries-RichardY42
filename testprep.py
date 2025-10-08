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

def idk(y,t):
    occuty=0
    times=0
    match1=0
    match2=0
    for i in y:
        times+=1
    for o in range(times):
        if "o" in y=="o" in t:
            occuty+=1
    print(occuty)
    print(times)
idk(".o.oo.","o..oo")
