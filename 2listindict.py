#2 map two ist into a dictionary

list1=[]
list2=[]

size = int(input("please insert the size for the list :"))

print("insert values into the list 1")
for i in range(size):
    x = input("value 1 : ")
    list1.append(int(x))
print("insert values into the list 2")
for i in range(size):
    y = input("value 2 : ")
    list2.append(y)
dict = {}

for i in range(size):
    dict[list1[i]] = list2[i]

print("The dictionary is :",dict)