atm_user_id = 1
atm_pin_number = 1231

input_id = int(input("Enter your id: "))
input_pin = int(input("Enter your pin: "))

if atm_user_id == input_id and atm_pin_number == input_pin:
    print("User verified successfully")

elif atm_user_id == input_id and atm_pin_number != input_pin:
    print("Incorrect pin")

elif not (atm_user_id == input_id):
    print("User not found")

