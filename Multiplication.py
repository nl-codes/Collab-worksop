def multiply_numbers():
    while True:
        num1 = input("Enter the first number (or 'q' to quit): ")
        if num1.lower() == 'q':
            print("Exiting the calculator. bye!")
            break

        num2 = input("Enter the second number: ")
        if num2.lower() == 'q':
            print("Exiting the calculator. bye!")
            break
        try:
            num1 = float(num1)
            num2 = float(num2)
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
multiply_numbers()