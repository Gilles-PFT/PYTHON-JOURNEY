a=" Hello world "

b=a.strip()   #removing spaces infront and behind
c=a.lower()   #change string to lower case
d=a.upper()   #change string to upper case
e=a.replace("e", "o")  #replacing a letter in a string
f=a.split(' ')    #dividing a string and storing in a list

print(b)
print(c)
print(d)
print(e)
print(f)

if 'y' in a:
    print("it is in a")
else:
    print("it's not in a")