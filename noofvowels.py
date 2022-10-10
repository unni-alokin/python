#to find the no f vowels in a string

vowels = ['a','e','i','o','u']
text_input = input("Enter the text to find the no of vowels :")
c = 0
j = 0
for i in range(len(text_input)):
    for j in range(5):
        if text_input[i] == vowels[j]:
            c = c+1
print("the no of vowels in given text_input is: ",c)