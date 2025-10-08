#eng or fren assign., should be put in a def func, doesnt need input func
def lang(x):
    s=0
    t=0
    for char in x:
        if char == "" or char=="":
            s+=1
        elif char =="" or char== "":
            t+=1
        if s>t:
            print
        if t<s:
            print


lang("asgdkelfghsssfttttdtdtdstststtssfiueawhftti")
#occupy space, should not have to use input func
def spaces(n,y,t):
    occu=0
    for i in range(n):
        #print(y[i],t[i])
        if y[i]=="c"and t[i]=="c":
            occu+=1
    return(occu)
print(spaces(5,"cccc.","c.c.c"))

#TEST ON FIRDAY AHHHHHHHHHHHHHHHHHH
