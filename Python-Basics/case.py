num1 = int(input("Enter firrst number : "))
num2 = int(input("Enter second number : "))
op = input("Enter an operator : ")
match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 *num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Enter a valid operator!!")