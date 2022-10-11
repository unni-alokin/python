import re
txt = input("Enter the email id :")
x = re.split("@", txt)
print(x[0]+"@")