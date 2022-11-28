city_name=input("Enter the city name: ")
print("The city name is: ",city_name)
count_a=0
count_e=0



for i in range(len(city_name)):
 if(city_name[i]=="a"):
      count_a+=1
 if(city_name[i]=="e"):
       count_e+=1
       
print(" a and e  in the city name: ",count_a, ",",count_e)