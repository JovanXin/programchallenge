#Challenge 64 - Easy
#http://rumkin.com/tools/cipher/ - we will be doing a Caesarian Shift

import random
import time

#declaring max shift size
maxshift = 26

#lets user decide if they wish to encrypt or decrypt
def getmode():
    while True:
        print("Do you wish to encrypt or decrypt?")
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

#gets "coded" message from user
def getmessage():
    print("enter your message ")
    return input()

#gets the shift from user
def getshift():
    shift = 0
    while True:
        print("enter a key number between 1 and 26")
        key = int(input())
        if shift >=1 and shift <= maxshift:
            return shift 


#shifts text by (shift) amount of leters
'''def caesar(plaintxt, shift, result):
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
'''
getmode()
#caesar(plaintxt, shift, result)