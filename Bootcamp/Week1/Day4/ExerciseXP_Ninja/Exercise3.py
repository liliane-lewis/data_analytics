#!/usr/bin/python3

import string

#Exercise 3: Working on a paragraph

#1.    Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
#2.    Paste it to your code, and store it in a variable.
#3.    Let’s analyze the paragraph. Print out a nicely formatted message saying:
#4.    How many characters it contains (this one is easy…).
#5.    How many sentences it contains.
#6.    How many words it contains.
#7.    How many unique words it contains.
#8.    Bonus: How many non-whitespace characters it contains.
#9.    Bonus: The average amount of words per sentence in the paragraph.
#10.    Bonus: the amount of non-unique words in the paragraph.



#2
paragraph = """In spite of the fact that the number of female students in hi-tech majors has doubled in the last decade, there is still almost no representation of women in senior positions and leading start-ups, the Israel Innovation Authority (IIA) said in a report released Tuesday. 
Just 4.3% of funds raised in the sector between 2021 and 2024 went to start-ups led by women, the report added, noting that just over 10% of private tech companies founded in Israel between 2013 and 2024 are led by women.
Women make up just 17.6% of senior leaders in private hi-tech companies and just 24.3% of board members in public companies, the report highlighted."""

#4
print(f"There are {len(paragraph)} characters in the paragraph")

#5
sentence_count = sum(paragraph.count(end) for end in ".!?")
print(f"There are {sentence_count} chasentencesracters in the paragraph")

#6 
words = paragraph.split()
word_count = len(words)
print(f"There are {word_count} words in the paragraph")

#7

words = paragraph.split()
unique_words = list(set(words))
word_count = len(unique_words)
print(f"There are {word_count} unique words in the paragraph")

#8
non_whitespace_count = len(paragraph.replace(" ", "").replace("\n", ""))
print(f"There are {non_whitespace_count} non-whitespace characters in the paragraph")

#9 

sentence_count = sum(paragraph.count(end) for end in ".!?")
avg_words_per_sentence = word_count / max(sentence_count, 1)
print(f"There are {avg_words_per_sentence} words per paragraph in the avarege")

#10. 
words = paragraph.split()
clean_words = [word.strip(string.punctuation).lower() for word in words]

word_counts = {}
for word in clean_words:
    word_counts[word] = word_counts.get(word, 0) + 1

non_unique_words = {word: count for word, count in word_counts.items() if count > 1}
print("Non-unique words and their counts:", non_unique_words)