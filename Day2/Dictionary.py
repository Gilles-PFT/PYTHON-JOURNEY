my_dict = {
           "name":"Jon",
           "age":"18",
           "gender":"male"
           }

m = my_dict["gender"]
print(m)

my_dict["age"] = 20
print(my_dict["age"])

#printing dictionary values wtih for
for key in my_dict:
    print(my_dict[key])
    
#adding a key to the dictionary
my_dict["occupation"] = "Python dev"

print(my_dict["occupation"])

#deleting elements
my_dict.pop("age")

del my_dict  #to delete the whole dictionary