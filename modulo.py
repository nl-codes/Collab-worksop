def division():
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    if num2==0:
        result = "Undefined"
    else:
        divide = num1%num2
        result = divide
    print(f"The result of {num1} % {num2} is: {result}")

division()