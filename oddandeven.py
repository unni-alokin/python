#sum of odd and even numbers between 15 nd 35
end = 35
oddsum = evensum = 0
for i in range(15,end+1):
    if i%2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i

print("The odd sum between 15 and 35 :",oddsum)
print("The even sum between 15 and 35 :",evensum)