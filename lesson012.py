classroomA = []
classroomB = []

print("\nClassroom A: ")
while True:
    choice = input("Do you want to add a student to this classroom (yes/no)? ")
    while choice.lower() != "yes" and choice.lower() != "no":
        print("Enter yes or no")
        choice = input("Do you want to add a student to this classroom (yes/no)? ")

    if choice .lower() == "yes":
        student = input("Name of the student: ")
        classroomA.append(student)
    elif choice.lower() == "no":
        break

print("\nClassroom B: ")
while True:
    choice = input("Do you want to add a student to this classroom (yes/no)? ")
    while choice.lower() != "yes" and choice.lower() != "no":
        print("Enter yes or no")
        choice = input("Do you want to add a student to this classroom (yes/no)? ")

    if choice .lower() == "yes":
        student = input("Name of the student: ")
        classroomB.append(student)
    elif choice.lower() == "no":
        break

combinedClass = classroomA + classroomB
combinedClass.sort()
print(combinedClass)
