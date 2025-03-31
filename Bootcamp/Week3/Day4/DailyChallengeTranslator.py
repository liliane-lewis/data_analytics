#!/usr/bin/python3

#Instructions :

#Consider this list
#
#french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
#
#    Look at this result 
#
#{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
#
#You have to recreate the result using a translator module. Take a look at the googletrans module

dictionary_translation_fr = {"Bonjour": "Hello", 
                          "Au revoir": "Goodbye", 
                          "Bienvenue": "Welcome", 
                          "A bientôt": "See you soon"
                          }


dictionary_translation_pt = {"Olá": "Hello", 
                          "Tchau": "Goodbye", 
                          "Bem Vindo": "Welcome", 
                          "Até logo": "See you soon"
                          }

def translator(word, language):
    if language == "PT":
        dictionary = dictionary_translation_pt
    elif language == "FR":
        dictionary = dictionary_translation_fr
    else:
        raise Exception("Language not detected") 
    
    return dictionary.get(word, "Word not found in dictionary")


# see useTranslator.py