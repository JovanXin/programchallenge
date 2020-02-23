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
        if shift<=26: #ensuring shift stays within 26
            for character in plaintxt:
                plaintext = ord(character)
                result += chr(plaintext + shift)
            print(result)

        else:
            print("program failed") #if shift > 26
        

    else:
        print("program failed") #if there's not only letters
        time.sleep(1)
        exit()

caesar(plaintxt, shift, result)