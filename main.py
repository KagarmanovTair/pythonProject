#task1.1
print("4 ,8 ,15 ,46 ,23 ,42 ")

#task1.2

print("4\n,8\n,15\n,46\n,23\n,42")

#task1.3

a = int(input())
for i in range(1,3):
     print(a+i)

#task1.4
try:

    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))

    total = num1 + num2 + num3

    print(total)
except ValueError:
    print("Error: integer.")

#task1.5
try:
    edge_length = float(input("Cube edge length: "))

    volume = edge_length
    surface_area = 6 * edge_length

    print(f"Volume = {int(volume)}")
    print(f"Total surface area = {int(surface_area)}")
except ValueError:
    print("Error:")

#task2.1
try:

    mandarins = int(input("Tangerines: "))
    students = int(input("SchoolChildren: "))

    per_student = mandarins // students

    remaining = mandarins % students


    print(f"Each student receives {per_student} whole tangerines.")
    print(f"There will be {remaining} whole tangerines left in the basket.")
except ValueError:
    print("Error: Enter integers (number of tangerines and schoolchildren).")

#task2.2
try:

    number = input("Four-digit number: ")

    if len(number) != 4:
        print("Error: enter four-digit number.")
    else:

        thousands = int(number[0])
        hundreds = int(number[1])
        tens = int(number[2])
        units = int(number[3])


        print(f"The digit in the thousands position is {thousands}")
        print(f"The digit in the hundreds position is {hundreds}")
        print(f"The digit in the tens position is {tens}")
        print(f"The digit in the position of units is {units}")
except ValueError:
    print("Error: enter four-digit number.")

#task2.3
    try:
        population = int(input("Enter the population of the universe: "))
        if population % 2 == 1:
            survivors = (population + 1) // 2
        else:
            survivors = population // 2


        print(f"Enter survivors {survivors}")
    except ValueError:
        print("Error: Enter an integer (universe population).")

#task2.4
try:
    num = int(input("Enter integer: "))

    result = num << 1

    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of the << operation is{result}")
except ValueError:
    print("Error: Enter an integer.")

#task2.5
try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))


    operation = input("Choose the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operation.")

    if operation in ('+', '-', '*', '/'):
        print(f"{num1} {operation} {num2} = {result}")
except ValueError:
    print("Error: Please enter numbers in the correct format.")