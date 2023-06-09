import random
from os import system, name
from data import data, logo, vs
import time


def check_answer(celeb1, celeb2, user_answer):
    if celeb1["follower_count"] > celeb2["follower_count"] and user_answer == "A":
        return True
    elif celeb2["follower_count"] > celeb1["follower_count"] and user_answer == "B":
        return True
    else:
        return False


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


user_choice = input(
    "Do you want to play the game ? . Type 'y' or 'n': ").lower()


def play(user_choice):
    right_answers = 0
    celeb1 = random.choice(data)
    celeb2 = random.choice(data)
    while celeb1 == celeb2:
        celeb1 = random.choice(data)
        celeb2 = random.choice(data)

    while user_choice == "y":

        print(
            f"\n A.){celeb1['name']},a {celeb1['description']} from {celeb1['country']}.\n {vs} \n\n B.){celeb2['name']},a {celeb2['description']} from {celeb2['country']}.\n")
        user_answer = input(
            "Who is more popular ? Type 'A' or 'B' : ").upper()
        if check_answer(celeb1, celeb2, user_answer):
            clear()
            print(logo)
            print("You answer is correct.")
            right_answers += 1
            print(f"Current Score: {right_answers}.")
            time.sleep(1)
            clear()
            print(logo)
            print(f"Current Score: {right_answers}.")
            celeb1 = celeb2
            celeb2 = random.choice(data)

        elif not check_answer(celeb1, celeb2, user_answer):
            clear()
            print(logo)
            print(
                f"Game Over.You scored {right_answers}.\n")
            break

    play_again = input("Want to play again ? Type 'y' or 'n': ")
    if play_again == "y":
        clear()
        print(logo)
        play(play_again)
    else:
        print("Tata")


if user_choice == "y":
    clear()
    print(logo)
    play(user_choice)
else:
    print("Tata")
