import re
txt = input("Enter a text ncluding white space and _ :")
x=''
for i in txt:
    if i == "/\s/g":
        print(i)
        x = re.sub(i ,"@",txt,count=1)
    elif i == "@":
        x = re.sub(i,"/\s/g",txt,count=1)
print(x)