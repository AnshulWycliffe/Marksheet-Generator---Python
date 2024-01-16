
print("*"*10,"WELCOME TO MARKSHEET REPORT GENERATOR","*"*10,'\n')
print("Enter Student's Details")
name = input("Name : ")
roll = int(input("Rollno : "))
dob = input("DOB : ")
stdClass = input("Class : ")
fname = input("FName : ")

print("\n")
print("Enter Academic Details")
eng = float(input("English : "))
hindi = float(input("Hindi : "))
maths = float(input("Maths : "))
sci = float(input("Science : "))
soc = float(input("Social Sci. : "))
cs = float(input("Computer Sci. : "))

total = eng + hindi + maths + sci + soc + cs
perc = total/600*100

grades = ''

if perc < 100 and perc >= 91:
    grades = "A+ Outstanding!"

elif perc < 90 and perc >= 81:
    grades = "A Impressive!"

elif perc < 80 and perc >= 71:
    grades = "B+ Good !"

elif perc < 70 and perc >= 61:
    grades = "B Well Done!"

elif perc < 60 and perc >= 51:
    grades = "C Not Bad"

elif perc < 50 and perc >= 41:
    grades = "D You Can Do Better!"

else:
    grades = "E No bro you are failed!"



print("-------------------------------------------------")
print("|                   Marksheet                   |")
print("-------------------------------------------------\n")

print("Name     :",name)
print("Roll No. : ",roll)
print("DOB      : ",dob)
print("Class    : ",stdClass)
print("FName    : ",fname,"\n")

print("-------------------------------------------------")
print("|              Academic Report                  |")
print("-------------------------------------------------")

print("English      - ",eng)
print("Hindi        - ",hindi)
print("Maths        - ",maths)
print("Science      - ",sci)
print("Social Sci   - ",soc)
print("Computer Sci - ",cs)

print("\n")

print("Total Marks Obtained - ",total)
print("Percentage - ", perc)
print("Grades - ",grades)
print("-------------------------------------------------")

