
password = input("Enter password: ")
passAttempt = 0
while password != 'anuska':
    print("Unauthorised!")
    passAttempt += 1

    if passAttempt == 3:
        print("Too many attempts!")
        break
    password = input("Enter password: ")
else:
    print("Login Successful")

