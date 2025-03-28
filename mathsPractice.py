import math

number=12.66
print(math.sqrt(25))
print(math.floor(2))
print(math.ceil(10.01))
print(math.pow(10,4))
print(math.factorial(4))

def find_cube(num1):
    cube=math.pow(num1,3)
    print(cube)
num=int(input("Enter any number to find the cube of: "))

find_cube(num)

def age_finder(birth_year):
    age=2025-birth_year
    print(f"Your current age is: {age}")
birth=int(input("Enter your birth year in AD: "))
age_finder(birth)