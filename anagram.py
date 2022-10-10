#anagram of a string
import random
import string
string1 = input("enter the string to find the anagram : ")
lists = list(string1)
a = []
print(a)
while True:
    random.shuffle(lists)
    # print(str(lists))

    x = ''.join(lists)
    if x not in a:
        a.append(x)
    else:
        break
print("The anagram of string is :",a)
