#to return the count of upper and lower in a string
def islowerupper(strings):
    ucout = lcout = 0
    for i in strings:
        if strings.isupper() == True:
            ucout = ucout + 1
            #print(ucout)
        else:
            lcout = lcout + 1
            #print(lcout)
    print(ucout)
    print(lcout)
text = input("Enter your string")
a = islowerupper(text)
