name=input("Enter the student name:")
Marks1=int(input("Enter the 1st sub marks:"))
Marks2=int(input("Enter the 2nd sub marks:"))
Marks3=int(input("Enter the 3rd sub marks:"))
Marks4=int(input("Enter the 4th sub marks:"))
Marks5=int(input("Enter the 5th sub marks:"))
Total=Marks1+Marks2+Marks3+Marks4+Marks5
per=Total/5
if per>=80:
    print("Grade: A+")
elif per>=70 and per<80:
    print("Grade: A")
elif per>=60 and per<70:
    print("Grade: B")
elif per>=50 and per<60:
    print("Grade: C")
else:
    print("Fail")        
    
print("Total Marks:",Total)
print("Percentage:",per)