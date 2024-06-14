
num1 = int(input("Enter first number:"))
sign = input("Enter sign:")
num2 = int(input("Enter second number:"))
if sign =="+" :
        print("Result:", num1 + num2)
elif sign == "-" :
        print("Result:", num1 - num2)
elif sign == "*" :
        print("Result:", num1 * num2)
elif sign == "/" :
    if num2 == 0:
            print("0")
    else:
            print("Result:", num1 / num2)

