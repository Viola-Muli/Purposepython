try:

    print(x)

except:
    print("Something went wrong")

finally:
    print("Success")

num1 = 67
num2 = 0

try:
    print(num1/num2)
except:
    print("Zerodivision occurred")
finally:
    print("Success")