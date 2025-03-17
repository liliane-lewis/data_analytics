#!/usr/bin/python3
#Instructions

#In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

#For example, with a left shift of 3 –> D would be replaced by A,
#–> E would become B, and so on.

#The method is named after Julius Caesar, who used it in his private correspondence.

#Create a python program that encrypts and decrypts messages with ceasar cypher.
#The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a 
# given message and a given shift.


def enc(plaintext,shift):
    cypher_text = ""
    for letter in plaintext:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            cypher_text += chr((ord(letter) - base + shift) % 26 + base)
        else:
            cypher_text += letter
    return cypher_text


def dec(cypher_text,shift):
    plaintext = ""
    for letter in cypher_text:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            plaintext += chr((ord(letter) - base - shift) % 26 + base)
        else:
            plaintext += letter 
    return plaintext

print("Caesar cipher")
ans = input("Do you want encript (e) or decript (d)?\n").strip().lower()
shift = int(input("What is the shift? (1-25)\n"))
message = input("Write a message:\n")

if ans == "e":
    cypher_text = enc(message, shift)
    print(f"The encrypted text is: {cypher_text}")
elif ans == "d":
    plaintext = dec(message, shift)
    print(f"The decrypted text is: {plaintext}")
else:
    print("Wrong option")