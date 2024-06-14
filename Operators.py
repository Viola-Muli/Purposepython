# Arithmetic operators- used for simple calculations
num1 = 56
num2 = 8
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)  # modulus-returns the remainder after dividing 2 numbers

# Comparison operators-compare values
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) # equal to
print(num1 != num2) # not equal to

# Assignment operators- assign values to variables
a = 200
print(a)

a -= 20
print(a)

# Logic operators - and , or , not
x = 100
print( x < 250 and x > 1000)
print( x < 250 or x > 1000)
print(not ( x < 250 or x > 1000))

# Operator precedence - order in which operations get executed
output = (100-4 * 3 / 1)
print(int (output))

# Write a simple python program that returns the area of a trapezium
base1 = 6
base2 = 7
height = 6
area = 0.5 * (base1 + base2) * height

print( "The are of the trapezium is" , int (area))
