#three most words in a text
print("Enter your text")
text_area = input()
#using split function to split the sentance into words
list = text_area.split()
#print(list)
count = 0
dict={}
for i in range(len(list)):
    for j in range(len(list)):
        if list[i] == list[j]:
            count = count + 1
    #print(list[i],count)
    if count >= 3:
        dict[list[i]] = count
    count = 0
#dict = sorted(dict)
[print(key, value) for (key, value) in sorted(dict.items(), key=lambda x: x[1])]

for (key,value) in dict.items():
    key = lambda x:x[1]
    print(dict)
#print(sorted(dict.items()))

#dict = sorted(dict.items())


#print(dict)  
        