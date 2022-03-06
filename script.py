#python 3.x
#written to resemble the shortcuts version I created. Probably really messy as I don't know Python.
import random
from numpy import char

#variables
ascii_values = []
encrypt = ""
encode = "" 
d = ""
decoded = ""
decrypted=""
key = ""
finalKey = ""
splitText = ""
splitKey = ""

#choose to encrypt or decrypt
chooseFromMenu = int(input("Choose an option: [0]=Encrypt Message, [1]=Decrypt Message\n"))

#if statement
if chooseFromMenu == 0:

    providedInput = input("Input the message you want to encrypt:\n")
    
    for character in providedInput:
        #generates random number to addd to the string converted to ASCII
        key = random.randint(2,750)
        encrypt = int(key) + int((ord(character))) #ord allows for string to ASCII
        encode = str(encode) + str(encrypt) + ":"
        finalKey = str(finalKey) + str(key) + ":"

    key = finalKey[:-1] #removes the final colon
    encode = encode[:-1] #removes the final colon
    print("\n- Your encrypted message is as follows -\n" + encode + "\n- Your key is as follows -\n" + key + "\n")

else:
    try:
        providedInput = input("Input the encrypted message you want to decrypt. It should only contain numbers and colons. (Ex = 111:2:333)\n")
        key = input("Input your key. It should only contain numbers and colons. (Ex = 111:2:333)\n")
        
        splitText = providedInput.split(":")
        splitKey = key.split(":")
        i = 0

        #loops through for each item in split, analogous to 'repeat with each'
        while i < len(splitText):
            d = int(splitText[i]) - int(splitKey[i])
            decoded = chr(int(d)) #chr allows for ASCII to string
            decrypted = str(decrypted) + str(decoded)
            i += 1
        
        print("\n- Your decrypted message is below -\n" + decrypted + "\n")

    except: #give error when there is an error
        print("\nError. Check your key and encrypted message. Make sure they contain only the numbers and colons. (Ex = 11:2:333)\n")