# In-built function/ Standard library functions
y = min(23, 56, 10, 5647)
print(y)

x = max(34, 32, 56, 100)
print("The maximum number is",x)

z = pow(2 , 3)
print(z)

# User-defined functions
def school():
    print("eMobilis")
school() # Calling a function

def multiply():
    num1 = 5
    num2 = 8
    print(num1*num2)
multiply()

# Parameters and arguments
def add(a, b):
    print(a+b)
add(5, 6)
add(13, 6)
add(5, 45)
add(25, 6)
add(5, 66)

def Employee( fullname, age, salary, phone, position ):
    print(fullname, age, salary, phone, position)

Employee("Job Kamau",57,50000,768945013,"MD")
Employee("Jane Wangari",34,30000,768455013,"Admin")
Employee("Corby Wafula",57,50000,763445013,"IT")
Employee("Brad Munene",25,20000,763268013,"Finance")
