

students = {}

while True:
    print("\n-----STUDENT MANAGEMENT SYSTEM-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. view results")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice ==  "1":
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        students[name] = marks
        print(f"{name} added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("Student List:")
            for name, marks in students.items():
                print(f"Name: {name}, Marks: {marks}")

    elif choice == "3":
        if not students:
            print("No students found.")
        else:
            print("Student Results:")
            for name, marks in students.items():
                if marks >= 50:
                    result = "Pass"
                else:
                    result = "Fail"
                print(f"Name: {name}, Marks: {marks}, Result: {result}")

    elif choice == "4":
        name = input("Enter student name to delete: ")
        if name in students:
            del students[name]
            print(f"{name} deleted successfully!")
        else:
            print(f"{name} not found.")

    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
