#employee salary details 
employee_id = input("Please enter your Employee id : ")
employee_name = input("Please enter your Name : ")
emp_basicpay = int(input("Please enter your Basic Pay :"))

print("calculating your DA, HRA and Netpay")

if emp_basicpay > 10000 :
    emp_hra = round((15/100)*emp_basicpay,2)
    emp_da  = round((8/100)*emp_basicpay,2)

elif emp_basicpay >=5000 and emp_basicpay <= 10000:
    emp_hra = round((10/100)*emp_basicpay,2)
    emp_da = round((5/100)*emp_basicpay,2)

else:
    emp_hra = round((5/100)*emp_basicpay,2)
    emp_da = round((3/100)*emp_basicpay,2)


netpay = emp_basicpay+emp_hra+emp_da

print("Hello",employee_name,"Your HRA, DA and Netpay for the given Basic pay : ",emp_basicpay,"is :")
print("HRA :",emp_hra)
print("DA :",emp_da)
print("Net pay : ",netpay)
