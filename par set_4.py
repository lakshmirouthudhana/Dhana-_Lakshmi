'''
# STUDENT MARKS FILE MANAGER----

# Requirement 1: Open marks.txt in write mode
with open("marks.txt", "w") as file:

    # Requirement 2: Accept marks for 5 students
    for i in range(5):

        try:
            # Requirement 3: Convert input into integer
            mark = int(input("Enter student mark: "))

            # Requirement 5: Check mark between 0 and 100
            if 0 <= mark <= 100:

                # Requirement 6: Write valid mark into file
                file.write(str(mark) + "\n")
                print("Mark saved successfully")

            else:
                print("Invalid mark")

        # Requirement 4: Handle non-number input
        except ValueError:
            print("Invalid mark")


# Requirement 7: Open file in read mode
print("\nSaved Marks:")

with open("marks.txt", "r") as file:

    # Requirement 8: Read and display every mark
    for mark in file:
        print(mark.strip())


# EXPENSE TRACKER-----

# Requirement 1: Create/open expenses.txt in write mode
with open("expenses.txt", "w") as file:

    # Requirement 2: Ask for 5 expenses
    for i in range(1, 6):

        try:
            # Requirement 3: Convert input into float
            expense = float(input(f"Enter expense {i}: "))

            # Requirement 5: Check expense is greater than 0
            if expense > 0:

                # Requirement 6: Write expense into file
                file.write(str(expense) + "\n")

            else:
                print("Invalid expense. Amount must be greater than 0.")

        # Requirement 4: Handle invalid input
        except ValueError:
            print("Invalid expense. Please enter a number.")


# Requirement 7: Open file in read mode
try:
    total = 0

    print("\nExpenses:")

    with open("expenses.txt", "r") as file:

        # Requirement 8: Read each expense
        for line in file:

            # Requirement 9: Convert line into float
            expense = float(line.strip())

            # Requirement 10: Calculate total
            total = total + expense

            print(expense)

    # Requirement 12: Display total
    print("Total expense:", total)


except FileNotFoundError:
    print("Expense file not found.")


STUDENT ATTENDANCE MANAGER----

# Student Attendance Manager

# Requirement 1: Create attendance.txt
with open("attendance.txt", "w") as file:

    # Requirement 2: Accept attendance for 5 students
    for i in range(5):

        try:
            # Requirement 3: Get student name
            name = input("Enter student name: ")

            # Requirement 4: Get attendance status
            status = input("Enter attendance (P/A): ").upper()

            # Requirement 5: Check whether status is P or A
            if status == "P" or status == "A":

                # Requirement 8: Save name and status
                file.write(name + "," + status + "\n")

            else:
                # Requirement 6
                print("Invalid attendance status")

        # Requirement 7: Handle unexpected errors
        except Exception:
            print("Invalid input")


# Requirement 9: Open file in read mode
try:
    print("\nPresent Students:")

    with open("attendance.txt", "r") as file:

        # Requirement 10: Read each record
        for record in file:

            # Requirement 11: Separate name and status
            name, status = record.strip().split(",")

            # Requirement 12: Display only Present students
            if status == "P":
                print(name)

# Requirement 13: Handle missing file
except FileNotFoundError:
    print("Attendance file not found.")


# Product Inventory Manager

# Requirement 1: Open inventory.txt in append mode
with open("inventory.txt", "a") as file:

    # Requirement 2: Enter 3 new products
    for i in range(3):

        try:
            # Requirement 3: Get product name
            product = input("Enter product name: ")

            # Requirement 4 & 5: Get quantity and convert to integer
            quantity = int(input("Enter quantity: "))

            # Requirement 7: Check quantity >= 0
            if quantity >= 0:

                # Requirement 8: Save product
                file.write(product + "," + str(quantity) + "\n")

            else:
                print("Invalid quantity")

        # Requirement 6: Handle invalid quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")


# Requirement 9: Open file in read mode
try:
    print("\nCurrent Inventory:")

    with open("inventory.txt", "r") as file:

        # Requirement 10: Display every product
        for record in file:

            # Separate product and quantity
            product, quantity = record.strip().split(",")

            print(product, "-", quantity)


    # Requirement 11: Ask product to search
    search_product = input("\nEnter product to search: ")

    found = False

    # Open file again for searching
    with open("inventory.txt", "r") as file:

        for record in file:

            # Separate product and quantity
            product, quantity = record.strip().split(",")

            # Requirement 12: Check whether product exists
            if product.lower() == search_product.lower():

                print(search_product + " is available.")
                print("Quantity:", quantity)

                found = True
                break

    # Requirement 14: Product not found
    if not found:
        print(search_product + " is not available.")


# Requirement 13: Handle missing file
except FileNotFoundError:
    print("Inventory file not found.")


#PR,ODUCT INVENTORY MANAGER:

passed = 0
failed = 0
total_marks = 0
valid_students = 0

try:
    with open("students.txt", "r") as file:

        for line in file:
            line = line.strip()

            # Split name and mark
            name, mark = line.split(",")

            try:
                mark = int(mark)

                # Check Pass or Fail
                if mark >= 50:
                    result = "Pass"
                    passed += 1
                else:
                    result = "Fail"
                    failed += 1

                # Add valid marks
                total_marks += mark
                valid_students += 1

                print(f"{name} - {mark} - {result}")

            except ValueError:
                print(f"Invalid mark for {name}")

    # Calculate average
    if valid_students > 0:
        average = total_marks / valid_students
    else:
        average = 0

    print("-------------------------")
    print("Result Summary")
    print("-------------------------")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")
    print(f"Average mark: {average:.2f}")

except FileNotFoundError:
    print("Error: students.txt file not found.")
