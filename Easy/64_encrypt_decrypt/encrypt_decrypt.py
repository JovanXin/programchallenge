#Challenge 64 - Easy
#http://rumkin.com/tools/cipher/ - we will be doing a Caesarian Shift

import random
import time

#asks user for text and shift
plaintxt = input("what is your plaintext?")
shift = int(input("what is your shift?"))
result = ("your final text is: ")

#shifts text by (shift) amount of leters
def caesar(plaintxt, shift, result):
    if plaintxt.isalpha(): #checking if plaintext contains letters only
        for character in plaintxt:
            asciiValue = ord(character) + shift
            print(asciiValue)
            if asciiValue > 122:
                print('going back to original')
                result += chr(asciiValue - 26)
            else:
                result += chr(asciiValue)
        print(result)
    else:
        print("program failed") #if there's not only letters
        time.sleep(1)
        exit()

caesar(plaintxt, shift, result)