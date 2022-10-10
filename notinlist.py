#if elements already exists in given dictionary else delete from list
rollno = [44,
          66,
          69,
          37,
          76,
          83,
          95,
          97]

sample_dict = {'sojo':44,
               'thomas':69,
               'tom':76,
               'jack':11}

list = sample_dict.values()
print(list)
a=[]
print(rollno)
#using slice as error will occur on performing 2 fns same time
for i in rollno[:]:
    while i not in list:
        print(i)
        rollno.pop(rollno.index(i))
        break

print(rollno)
