#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.


def repeat_word(word,num):
    for i in range(0,num):
        print(word)


repeat_word("hello", 3)  
# Output:
# hello
# hello
# hello

repeat_word("goodbye", 2)  
# Output:
# goodbye
# goodbye