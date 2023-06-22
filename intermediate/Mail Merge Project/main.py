with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt","r") as invtext:
            invitation_text = invtext.read()

for name in names:
    with open(f"./Output/ReadyToSend/{name.rstrip()}_invitation.txt","w") as letter:
        letter.write(invitation_text.replace("[name]",f"{name.strip()}"))