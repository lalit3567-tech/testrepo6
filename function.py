# function definition
def greeting():
    print("welcome to python")
# call function (use function)
greeting()

# create a function to add 2 numbers

def add2numbers(a,b): # parameter a,b
    result = a +b
    print("the sume is:", result)

add2numbers(9,6) # arguments (9,6)

def return_fun():
    a = "welcome to AVD"
    return a

print(return_fun())


def add2numbers(a,b): # parameter a,b
    result = a +b
    return result

sum = add2numbers(10,2)
print("the sum is:",sum)

# function to convert celsius to fahrenheit with and without return statement

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit",fahrenheit)

celsius_to_fahrenheit(50)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# calling this function to return a value
temp_f = celsius_to_fahrenheit(10)
print("Temperature in Fahrenheit",temp_f)
#####################

# The pass statement is placeholder in a function or loop
# It does nothing and is used when you need to write
# code that will be added later or to define an
# empty function

def kuchbhi():
    pass
print("Code could be updataed later")

