import random
total_length = int(input("Total password length: "))
num_length = int(input("Numbers in password: "))
sym_length = int(input("Symbols in password: "))
left_length = total_length - (num_length+sym_length)
ualphabets_length = left_length//2
lalphabets_length = total_length-(num_length+sym_length+ualphabets_length)

symbols = ["!", "@", "#", "$", "%", "&", "*"]

ualphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lalphabets = [l.lower() for l in ualphabets]


password = ""


for i in range(1, sym_length+1):
    password += symbols[random.randint(0, len(symbols)-1)]

for i in range(1, num_length+1):
    password += str(random.randint(0, 9))

for i in range(1, ualphabets_length+1):
    password += ualphabets[random.randint(0, 25)]
for i in range(1, lalphabets_length+1):
    password += lalphabets[random.randint(0, 25)]

newpassword = list(password)
random.shuffle(newpassword)
newpassword = ''.join(newpassword)

print(newpassword)


# We can also use random.choice(list) instead of list[random.randlint()]
