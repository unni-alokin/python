#to find the grade mark of a student using 6 marks '
name = input("Please enter your name : ")
marks = []
subject_name = [
    "physics",
    "chemistry",
    "socialscience",
    "maths",
    "computerscience",
    "english"]
totalmark = 0
for i in range(6):
    print("Enter the mark for the subject ",subject_name[i]," : ")
    mark = int(input())
    marks.append(mark)
    totalmark = totalmark + mark

#finding average marks 
avg_mark = round((totalmark/6),2)

print("your total mark is ",totalmark)
print("your average mark is ",avg_mark)

#finding grades for the student 
if avg_mark >= 90 and avg_mark <= 100:
    print("Congrats",name,"your grade is A+ !")
elif avg_mark >=80 and avg_mark <90:
    print("Congrats",name,"your grade is A !")
elif avg_mark >=70 and avg_mark <80:
    print("Congrats",name,"your grade is B+ !")
elif avg_mark >=60 and avg_mark <70:
    print("Congrats",name,"your grade is B !")
elif avg_mark >=50 and avg_mark <60:
    print("Congrats",name,"your grade is C !")
elif avg_mark >=40 and avg_mark <50:
    print("Congrats",name,"your grade is D .Keep trying , you can do it !")
elif avg_mark >=30 and avg_mark <40:
    print("Congrats",name,"your grade is E .Keep trying , you can do it !")