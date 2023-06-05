import random
print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/    
''')
wanttoplay = input("Do you want to play blackjack ? (Type 'yes' or 'no'): ")


def choosewinner(usercards, computercards):
    usertotal = 0
    for card in usercards:
        usertotal += card
    computertotal = 0
    for card in computercards:
        computertotal += card

    if usertotal == 21:
        return "You Won"
    elif computertotal == 21:
        return "Computer Won"

    userdiff = 21 - usertotal
    computerdiff = 21 - computertotal

    if userdiff < 0 and computerdiff > 0:
        return "Computer Won"
    elif computerdiff < 0 and userdiff > 0:
        return "You Won"
    elif userdiff < 0 and computerdiff < 0:
        if userdiff > computerdiff:
            return "You Won"
        else:
            return "Computer Won"
    elif userdiff < computerdiff:
        return "You Won"
    elif computerdiff < userdiff:
        return "Computer Won"


def checkifexceed(usercards, computercards):
    usertotal = 0
    for card in usercards:
        usertotal += card
    computertotal = 0
    for card in computercards:
        computertotal += card
    if usertotal > 21 or computertotal > 21 or usertotal == 21 or computertotal == 21:
        return True
    else:
        return False


def usertotalscore(usercards):
    usertotal = 0
    for card in usercards:
        usertotal += card
    return usertotal


if wanttoplay == "yes":
    usercards = [random.randint(1, 10), random.randint(1, 10)]
    computercards = [random.randint(1, 10), random.randint(1, 10)]

    print(
        f"Your Cards: {usercards}\nComputer's first card: {computercards[0]}")
    print(f"Your total score: {usertotalscore(usercards)} ")

    more = True
    while more:
        userchoice = input("Want to continue or pass (Type 'yes' or 'no'): ")

        if userchoice == "no":
            # computercards.append(random.randint(1, 10))
            winner = choosewinner(usercards, computercards)
            print(
                f"Your Cards: {usercards}\nComputer's final card: {computercards}")
            print(f"Your total score: {usertotalscore(usercards)} ")
            print(winner)
            more = False
        if userchoice == "yes":
            usercards.append(random.randint(1, 10))
            computercards.append(random.randint(1, 10))

            if checkifexceed(usercards, computercards):
                winner = choosewinner(usercards, computercards)
                print(
                    f"Your Cards: {usercards}\nComputer's final card: {computercards}")
                print(f"Your total score: {usertotalscore(usercards)} ")
                print(winner)
                more = False
            else:
                print(
                    f"Your Cards: {usercards}\nComputer's first card: {computercards[0]}")
                print(f"Your total score: {usertotalscore(usercards)} ")
                continue


else:
    print("Tata")
