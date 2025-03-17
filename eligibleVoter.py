age = int(input("Enter your age: "))
isCitizen = input("Are you from Nepal? (Y/N)")

if age >= 18 and isCitizen == "y".lower():
    print("You are eligible to vote")

if age < 18 or isCitizen == "n".lower():
    print("You are not an eligible voter")

