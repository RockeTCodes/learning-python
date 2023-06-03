import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

computer = game[random.randint(0, len(game)-1)]

player = game[int(
    input("Input 0 for Rock , 1 for Paper and 2 for Scissors: "))]

print(f"You: {player}\nComputer: {computer}")

if player == rock and computer == scissors:
    print("You Win")
elif player == scissors and computer == rock:
    print("You Loose")

elif player == scissors and computer == paper:
    print("You Win")
elif player == paper and computer == scissors:
    print("You Loose")

elif player == paper and computer == rock:
    print("You Win")
elif player == rock and computer == paper:
    print("You Loose")
else:
    print('Draw')
