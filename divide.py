def divide():
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    divide = num1/num2
    if num2==0:
        result = "Undefined"
    else:
        result = divide
    return result

def main():
    divide()
        

