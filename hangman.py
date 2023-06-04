import random
from os import system, name
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''')


player_lives = 6
words = ["HOME", "LOVE", "ZOO", "THOR", "ABANDONED", "ABDOMINAL", "LION", "TIGER",
         "PYTHON", "HORSE", "RABBIT", "MOUSE", "PEACOCK", "SCHOOL", "PROGRAMMING"]

random_word = random.choice(words)


random_word_length = len(random_word)
print(f"The word contains {random_word_length} letters.")

emptyguess = []
for i in range(random_word_length):
    emptyguess += "_"


def printemptyguess(emptyguess):
    emptyguessp = ""
    for guess in emptyguess:
        emptyguessp += f" {guess}"
    print(f"{emptyguessp}\n")


printemptyguess(emptyguess)


def checkifguessexist(guess):
    for i in range(0, random_word_length):
        if random_word[i] == guess:
            return True
    return False


def filltheguess(guess):
    for i in range(0, random_word_length):
        if random_word[i] == guess:
            emptyguess[i] = guess
        else:
            continue


def checkifwordguessed(emptyguess):
    emptyguessp = ""
    for guess in emptyguess:
        emptyguessp += guess
    if emptyguessp == random_word:
        return True
    else:
        return False


def printhangman():
    if player_lives == 6:
        print('''
      _________
     |/      |
     |      
     |      
     |      
     |      
     |
 ____|___
        ''')
    elif player_lives == 5:
        print('''
      _________
     |/      |
     |      (_)
     |      
     |      
     |      
     |
 ____|___
        ''')
    elif player_lives == 4:
        print('''
      _________
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|___
        ''')
    elif player_lives == 3:
        print('''
      _________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|___
        ''')

    elif player_lives == 2:
        print('''
      _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
        ''')
    elif player_lives == 1:
        print('''
      _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___
        ''')
    elif player_lives == 0:
        print('''
      _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___
        ''')


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def printafterwinning():
    print('''

-----------------------------------------------------
   _                             .-.
  / )  .-.    ___          __   (   )
 ( (  (   ) .'___)        (__'-._) (
  \ '._) (,'.'               '.     '-.
   '.      /  "\               '    -. '.
     )    /   \ \   .-.   ,'.   )  (  ',_)    _
   .'    (     \ \ (   \ . .' .'    )    .-. ( \\
  (  .''. '.    \ \|  .' .' ,',--, /    (   ) ) )
   \ \   ', :    \    .-'  ( (  ( (     _) (,' /
    \ \   : :    )  / _     ' .  \ \  ,'      /
  ,' ,'   : ;   /  /,' '.   /.'  / / ( (\    (
  '.'      "   (    .-'. \       ''   \_)\    \\
                \  |    \ \__             )    )
              ___\ |     \___;           /  , /
             /  ___)                    (  ( (
             '.'                         ) ;) ;
                                        (_/(_/
----------------------------------------------------
    
    ''')


while player_lives >= 0:
    if player_lives == 0:
        print("GAME OVER")
        break
    if checkifwordguessed(emptyguess):
        clear()
        print("🎉🎉Yay you Won🎉🎉")
        printafterwinning()
        break
    guess = (input("Guess a letter of the word: ")).upper()
    if checkifguessexist(guess):
        clear()
        filltheguess(guess)
        print("Yay you guessed correctly.")
        print(f"Lives Left: {player_lives}\n")
        printemptyguess(emptyguess)
        printhangman()
    else:
        player_lives -= 1
        clear()
        print("This letter does not exist in the word.")
        print(f"Lives Left: {player_lives}")
        printemptyguess(emptyguess)
        printhangman()
