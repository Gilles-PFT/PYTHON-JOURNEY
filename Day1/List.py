my_list=["wood", "chair", "orange", "apple"]
print(my_list[1:3])

#looping through a list
for x in my_list:
    print(x)
    
#adding an element to a list
a = my_list.append("cup")
print(my_list)

#adding at a specific index
b = my_list.insert(0,"ink")
print(my_list)

#deleting an element
c = my_list.remove('apple')
print(my_list)