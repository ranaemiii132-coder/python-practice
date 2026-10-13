           
age=int(input("Enter your age:"))
has_license=True
if age>=18:
    if has_license==True:
        print("You can drive")
    else:
        print("need license")
else:
    print("You are underage")

marks=75
attendance=80
if marks>40:
    if attendance>75:
        print("You are pass")
    else:
        print("Attendance too low")
else:
    print("Student fail due to low marks")         
username="admin"
password="12345"
if username=="admin":
    if password=="12345":
       print("login Successfull")
    else:
        print("wrong password")
else:
    print("wrong username")

amount=5000
is_member=True
if amount>3000:
    if is_member==True:
        print("You get 20% discount")
    else:
        print("You got 10% discount")
else:
    print("No discount")

balance=10000
withdraw_amount=5000
if balance==10000:
    if withdraw_amount==5000:
        print("please collect your cash")
    else:
        print("Invalid amount")
else:
    print("Insufficiant amount")
