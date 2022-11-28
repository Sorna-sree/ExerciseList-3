name_1=input("enter the name: ")
name_2=input("enter the name: ")


lastchar_name1=name_1[-1]
lastchar_name2=name_2[-1]
#add a in the given name
if(len(name_1)<len(name_2)):
    len=len(name_2)-len(name_1)
    print(len)
    s=name_1 +lastchar_name1*len
else:
    len=len(name_1)-len(name_2)
    print(len)
    s=name_2+lastchar_name2*len
    
print(s)