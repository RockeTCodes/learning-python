from os import system, name

newdict = dict()

more = True


def pickwinner(winnername, winningbid):
    print(f"{winnername} won the bid. He bid ${winningbid}")


def addtonewdict(name, bid):
    newdict[name] = bid


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


winnername = ""
winningbid = 0

while more:
    username = input("Enter your name: ")
    bid = int(input("Enter you bid amount: $"))
    addtonewdict(username, bid)
    if bid > winningbid:
        winnername = username
        winningbid = bid
    anymoreleft = input(
        "Are there any more people left to bid(Type 'yes' or 'no'): ")
    if anymoreleft == "no":
        clear()
        pickwinner(winnername, winningbid)
        more = False

    else:
        clear()
        continue


userlist = list()


for key in newdict:
    userlist += str(newdict[key])

print(userlist)
