x=input("type in a sentence i determine if it is english or french: ")
eng=[]
fren=[]
y=x.split("t")
y1=x.split("T")
z=x.split("s")
z1=x.split("S")
eng+=[y]
fren+=[z]
if eng>fren:
    print("english")
elif eng<fren:
    print("french")
