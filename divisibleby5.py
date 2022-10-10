#to find the no divisible by 5
l= [43,65,52,50,70,85,25]
list =[]
print("numbers divisible by 5 in the list is ")
for x in l:
    if x%5 ==0:
        list.append(x)
list = sorted(list)
print(list)