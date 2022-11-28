name_1=input("enter the name: ")
name_2=input("enter the name: ")

#add a in the given name
if(len(name_1)<len(name_2)):
    len=len(name_2)-len(name_1)
    print(len)
    s=name_1 +"a"*len
else:
    len=len(name_1)-len(name_2)
    print(len)
    s=name_2+"a"*len
    
print(s)