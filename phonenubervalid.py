import re

phone = input("Enter the phone number : ")

x = re.match("\d")
if x :
    print("Correct")
else:
    print("no")