#!/usr/bin/python3

#Exercise 2 : From English to Morse
#Instructions
#
#Write a function that converts English text to morse code and another one that does the opposite.
#Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/' 
}

MORSE_TO_ENGLISH = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    text = text.upper() 
    return ' '.join(MORSE_CODE_DICT.get(char, char) for char in text)

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        decoded_chars = [MORSE_TO_ENGLISH.get(char, '') for char in word.split()]
        decoded_words.append(''.join(decoded_chars))
    return ' '.join(decoded_words)


english_text = "Hello, World!**"
morse_code = text_to_morse(english_text)
print(f"Text to Morse: {morse_code}")

decoded_text = morse_to_text(morse_code)
print(f"Morse to Text: {decoded_text}")

