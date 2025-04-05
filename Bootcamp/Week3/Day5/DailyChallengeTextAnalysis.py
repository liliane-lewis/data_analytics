#!/usr/bin/python3

#Instructions :

#The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like 
# "Today, is a happy day" or it can be an external text file.#
#
#Part I
#
#First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
#    Create a class called Text that takes a string as an argument and store the text in a attribute.
#    Hint: You need to manually copy-paste the text, straight into the code
#
#    Implement the following methods:
#        a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#        a method that returns the most common word in the text.
#        a method that returns a list of all the unique words in the text.
#
#
#Part II
#
#Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
#    Implement a classmethod that returns a Text instance but with a text file:
#
#        >>> Text.from_file('the_stranger.txt')
#
#    Hint: You need to open and read the text from the text file.
#
#    Now, use the provided the_stranger.txt file and try using the class you created above.
#
#
#Bonus:
#
#    Create a class called TextModification that inherits from Text.
#
#    Implement the following methods:
#        a method that returns the text without any punctuation.
#        a method that returns the text without any english stop-words (check out what this is !!).
#        a method that returns the text without any special characters.
#
#Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.
#
#Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

from collections import Counter
import string
import re 
from nltk.corpus import stopwords

class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return None
        
    def word_count(self):
        return len(self.text.split())

    def unique_words(self):
        return set(self.text.lower().split())

    def most_common_word(self):

        words = self.text.lower().split()
        counter = Counter(words)
        print(counter)
        return counter.most_common(1)[0]

    def contains_word(self, word):
        return word.lower() in self.text.lower().split()
    
class TextModification(Text):
    def remove_punctuation(self):
        return self.text.translate(str.maketrans('', '', string.punctuation))

    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        words = self.text.split()
        filtered = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered)

    def remove_special_characters(self):
        return re.sub(r'[^A-Za-z0-9\s]', '', self.text)

my_text = """Wisdom is one of those qualities that is difficult to define—because it encompasses so much—but which people generally recognize when 
they encounter it. And it is encountered most obviously in the realm of decision-making. Psychologists tend to agree that wisdom involves an integration 
of knowledge, experience, and deep understanding, as well as a tolerance for the uncertainties of life. There's an awareness of how things play out over 
time, and it confers a sense of balance.
"""

text_obj = Text(my_text)

print("Word count:", text_obj.word_count())
print("Unique words:", text_obj.unique_words())
print("Most common word:", text_obj.most_common_word())
print("Contains 'wisdom'? ->", text_obj.contains_word("wisdom"))


text_obj = TextModification.from_file("the_stranger.txt")

if text_obj:
    print("Text without punctuation:")
    print(text_obj.remove_punctuation()[:])
    print("\nText without stopwords:")
    print(text_obj.remove_stopwords()[:])

    print("\nText without special characters:")
    print(text_obj.remove_special_characters()[:])