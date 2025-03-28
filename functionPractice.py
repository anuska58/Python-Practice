#no parameter, no return
def name():
    print("My name is Anuska Acharya. I am starting my data science journey")
name()

#parameter but no return
def calculate(num1,num2):
    total=num1+num2
    print(total)
calculate(10,35)

#parameter and return

def full_name(first_name, last_name):
    fullname=f"My name is {first_name} {last_name}"
    return fullname

fn=full_name("Anuska","Acharya")
print(fn)

#no parameter but return
def voter_age():
    return 18
    