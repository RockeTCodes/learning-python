from os import system, name


def printcalc():
    print('''
 _____________________
|  _________________  |
| | HELLO USER      | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')


printcalc()


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def calculate(pnum, newnum, operation):
    if operation == "*":
        return pnum * newnum
    elif operation == "/":
        return pnum / newnum
    elif operation == "+":
        return pnum + newnum
    elif operation == "-":
        return pnum - newnum


calculating = True
pnum = float(input("Input the number: "))

while calculating:
    operation = input(" + \n - \n * \n / \n Enter the operation: ")
    newnum = float(input("Input another number: "))
    result = calculate(pnum, newnum, operation)
    print(f"{pnum} {operation} {newnum} = {result}")
    choice = input(
        f"Do you want to continue with {result} or exit.\n(Type 'yes' to continue Or 'no' to exit. If you want to start new calculation Type 'new'): ")
    if choice == "yes":
        pnum = result
    elif choice == "new":
        clear()
        printcalc()
        pnum = float(input("Input the number: "))
    elif choice == "no":
        break
