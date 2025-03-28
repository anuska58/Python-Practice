import random

# print(random.randint(0,100,))

# list=['apple', 'ball', 'cat', 'dog']
# random.shuffle(list)
# print(list[3])

guessNumber = input("Enter a number from 1 to 10 to guess: ")
randomNumber = random.randint(1,10)
if guessNumber == randomNumber:
    print(f"You guessed the correct number which is {randomNumber}")
else:
    print(f"Try again, the correct number is {randomNumber}")
