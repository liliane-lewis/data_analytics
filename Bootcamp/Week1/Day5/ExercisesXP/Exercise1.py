#!/usr/bin/python3


#Exercise 1 : Convert lists into dictionaries
#Instructions

#    Convert the two following lists, into dictionaries.
#    Hint: Use the zip method

#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys,values))
print(f"Dictionary: {dictionary}")