# Parameter But No Return Type
def greet(name):
    print(f"Hello {name}")


greet("Anuska")


def findsum(num1, num2):
    total = num1 + num2
    print(f"Total is {total}")


num1 = 3
num2 = 6
findsum(num1, num2)
findsum(4, 10)


# No Parameter No Return Type
def programmer():
    print("Anuska is in her datascience journey.")
programmer()

#Parameter and Return Type
def fullname(first_name,last_name):
    fullname=f"{first_name} {last_name}"
    return fullname

fn= fullname("Anuska","Acharya")
print(fn)

def voter_age():
    return 18

anuska_age=24
if anuska_age>=voter_age():
    print("Anuska is eligible to vote")
else:
    print("Anuska is not eligible to vote")