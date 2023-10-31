grades=[]
while True:
    grade = input("Enter a grade (or 'EXIT' to finish): ")
    if grade.lower() == "exit":
        break
    else:
        grades.append(float(grade))

average_grade= sum(grades)/len(grades)
print("The Average of the grades is: ", average_grade )