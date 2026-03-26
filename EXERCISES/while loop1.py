#Program printing the first 20 terms of the multiplication table
#by 7 and adding an asterix(*) on terms which are multiples of 3

i = 1

while i<21:
    a = i * 7
    if a % 3 == 0:
        print("*", end="")
    i += 1
    print(a, end=" ")