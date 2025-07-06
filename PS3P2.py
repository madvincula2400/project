#Input
last_name = input("Enter the student's last name: ")
midterm_score = float(input("Enter the student's midterm score: "))
final_score = float(input("Enter the student's final score: "))

#Processing  
total_points = midterm_score + final_score

#Output
print(f"Student {last_name}")
print(f"Total Exam Points: {total_points}")