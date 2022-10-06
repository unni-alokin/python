#password verification
username = input ("Enter your username : ")
password = input ("Enter your password : ")

verify_username = input("Enter your username again :")
verify_password = input("Enter your password again : ")

if password == verify_password and username == verify_username:
    print("Hey",username,"the credentials do match !")
else :
    print("Hey",username,"the credentials do not match !")