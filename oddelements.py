# to print the odd index elements of a list
A = [1,2,3,4,5,6,7,'a']
B= []
for i in range(len(A)):
    if (i%2!=0):
        print(type(i))
        B.append(A[i])
print("the updated list is",B)

#[print for i in A  if int(A.index)%2 != 0]