while True:
    gradebook = input("Would you like to view grades or the students? Grades/Students: ").capitalize()
    if gradebook == "Grades":
        print("Here are the grades.")
        print()
        break
    elif gradebook == "Students":
        print("Here are the students.")
        print()
        break
    else:
        print("Please try again, I did not understand that.")
        print()

if gradebook == "Grades":
    print("Test")

if gradebook == "Students":
    print("Test")