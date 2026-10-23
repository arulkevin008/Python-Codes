while True:
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    operand=input("Enter the operation:")
    match (operand):
        case "+":
            print("Addition:",a+b)
        case "-":
            print("Subtraction:",a-b)
        case "*":
            print("Multiplication:",a*b)
        case "/":
            print("Division:",a/b)
        case "%":
            print("Modulus:",a%b)
        case "^":
            print("Power:",a**b)
        case "**":
            print("Power:",a**b)
        case _:
            print("Invalid Operand")
