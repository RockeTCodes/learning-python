import random

levelchoice = input("Enter the level 'easy' or 'hard': ")

guesses = int()
user_guess = int()

if levelchoice == "easy":
    guesses = 10
elif levelchoice == "hard":
    guesses = 5

print("I have guessed a number btw 1 to 100.")

random_number = random.randint(1, 100)

print(random_number)

while guesses >= 0:

    if user_guess == random_number:
        print("You guessed correctly.")
        break
    if guesses == 0:
        print("You lost. No More guesses left.")
        break
    print(f"You have {guesses} guesses left.")
    user_guess = int(input(" Guess Again: "))
    if user_guess > random_number:
        print("Too High")
    elif user_guess < random_number:
        print("Too Low")
    guesses -= 1
