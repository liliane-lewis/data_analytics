#!/usr/bin/python3

#Exercise 1 – Random Sentence Generator
#Instructions
#
#Description: In this exercise we will create a random sentence generator. 
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.
#
#Hint : The generated sentences do not have to make sense.
#
#    Download this word list
#
#    Save it in your development directory.
#
#    Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. 
# What is the correct data type to store the words?
#
#    Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to 
# determine how many words the sentence should have. The function should:
#        use the words list to get your random words.
#        the amount of words should be the value of the length parameter.
#
#    Take the random words and create a sentence (using a python method), the sentence should be lower case.
#
#    Create a function called main which will:
#        Print a message explaining what the program does.
#
#        Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test
#            your validation!
#            If the user inputs incorrect data, print an error message and end the program.
#            If the user inputs correct data, run your code.


import random

def get_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]
    return words

def get_random_sentence(length):
    sentence = ""
    words = get_words_from_file("sowpods.txt")
    for _ in range(length):
        sentence = " ".join(random.choice(words) for _ in range(length))
        #sentence += random.choice(words) + " "
    
    return sentence.lower()




def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence of the length you choose (between 2 and 20 words).")
    
    try:
        length = int(input("How many words should the sentence have? (2 - 20): "))
        if length < 2 or length > 20:
            print("Error: Please enter a number between 2 and 20.")
            return 1
    except ValueError:
        print("Error: That's not a valid number. Please enter an integer.")
        return 1

    sentence = get_random_sentence(length)
    print("Your random sentence:")
    print(sentence)

if __name__ == "__main__":
    main()

#Exercise 2: Working with JSON
#Instructions

#import json
#sampleJson = """{ 
#   "company":{ 
#      "employee":{ 
#         "name":"emma",
#         "payable":{ 
#            "salary":7000,
#            "bonus":800
#         }
#      }
#   }
#}"""
#
#
#    Access the nested “salary” key from the JSON-string above.
#    Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
#    Save the dictionary as JSON to a file.

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(sampleJson[4])

salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

data["company"]["employee"]["birth_date"] = "01/01/1970"

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(data, file_obj, indent=4)
    
pretty_json = json.dumps(data, indent=4)
print(pretty_json)

print("Updated JSON saved to 'my_file.json'")
