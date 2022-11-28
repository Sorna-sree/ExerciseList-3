movie_name=input("Enter the movie name: ")
print("Movie name is: ",movie_name)
count=0
movie_name=movie_name.split()

#count the words in the given movie name
for i in range(len(movie_name)):
    count+=1
    
print(f"{count} ,words in the movie name")