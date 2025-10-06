x=input("type in a sentence i determine if it is english or french: ")
eng=[]
fren=[]
for ltr in x:
    if ltr == "t" or ltr =="T":
        eng.append(ltr)
    if ltr=="s" or ltr == "S":
        fren.append(ltr)
if eng>fren:
    print("english")
elif eng<fren:
    print("french")
#print(eng)
