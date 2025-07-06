print ("student grade average")

student_count = 0



response = input("Do you want to do this program? (type Yes to continue): ")

while response == "Yes":
  last_name = input("Enter students last name: ")
exam1 = float(input("enter exam 1 score:"))
exam2 = float(input("enter exam 2 score:"))

average = (exam1 + exam2) / 2

print("student:", lname, average)
print()

student_count = student_count + 1


response = input("do you want to do this loop again? (type Yes to continue): ")

print("total number of students who entered their scores:", student_count)








