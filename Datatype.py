# Datatype
number = 78  # int
num = 45.09  # float
greeting = "How are you doing"  # str
Is_Programming_Interesting = True  # bool
devices = ["laptop","computer","phone","tablet"]  # list
browsers = ("Opera","firefox","chrome","safari")  # Tuple
countries = {"Kenya","Uganda","India"} # set
employee = {
    "firstname" : "jane",
    "age": 29,
    "nationality": "India",
    "emailaddress": "jane@gmail.com",
} #dictionary
print(Is_Programming_Interesting)
print(num)
print(countries)
print(employee["firstname"])
print(employee["age"])
print(number)

# Determining datatypes
print(type(countries))
print(type(employee))
# Typecasting is the process of converting one datatype to another
print(int(num))
print(float(number))