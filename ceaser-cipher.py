print('''
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|     
''')


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode():
    encode = input("Enter message to encode: ").lower()
    shift = int(input("Enter the shift: "))

    encoded = ""

    for j in range(0, len(encode)):
        for i in range(0, 26):
            if encode[j] == letters[i]:
                encoded += letters[(i+shift) % 26]

    print(f"Your encoded message is: {encoded}")


def decode():
    decode = input("Enter message to decode: ").lower()
    shift = int(input("Enter the shift: "))
    decoded = ""

    for j in range(0, len(decode)):
        for i in range(0, 26):
            if decode[j] == letters[i]:
                decoded += letters[(i-shift) % 26]

    print(f" Your decoded mesaage is: {decoded}")


start = True

while start:
    userinput = input("You want to 'encode' or 'decode' ? :").lower()
    if userinput == "encode":
        encode()
    elif userinput == "decode":
        decode()
    else:
        print("Please enter a valid Input.")
    askagain = input(
        "Type 'yes' to encode/decode again or type 'no' to exit: ").lower()
    if askagain == "no":
        start = False
    elif askagain == "yes":
        continue
    else:
        print("Please enter a valid Input.")
