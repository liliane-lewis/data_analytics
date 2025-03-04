#Write Python code to complete the following tasks.

#1. Given a list [1, 2, 3, 4], print out all the values in the list one by one.

list = [1, 2, 3, 4]
for l in list:
    print(l)

#2. Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.

list = [1, 2, 3, 4]
for l in list:
    print(20 * l)

#3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
names = ["Elie", "Tim", "Matt"]
first = []
for m in names:
    first += m[0] 
    #print(m[0])
print(first)

#4 Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
list =  [1, 2, 3, 4, 5, 6]
even_list = []
for n in list:
    if n % 2 == 0:
        print(n)
        even_list.append(n)

print(even_list)

#5 Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].
list1 = [1, 2, 3, 4]
list2 =  [3, 4, 5, 6]
new_list = []
for l1 in list1:
    if l1 in list2:
        new_list.append(int(l1))  
print(new_list)

#6. Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"]
names = ["Elie", "Tim", "Matt"]

reversed_words = [name[::-1].lower() for name in names]
print(reversed_words)

#7. Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].
string1 = "first"
string2 = "third"
new_list = []
for s1 in string1:
    if s1 in string2:
        new_list.append(str(s1)) 
print(new_list)

# 8.  For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].
new_list = []
for num in range(1,100):
    if (num % 12 == 0):
        new_list.append(num)

print(new_list)

#9. Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].

string="amazing"
new_list=[]
for s in string:
    if s not in ["a","e","i","o","u"]:
        new_list.append(s)
print(new_list)

#10.  Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

list = []
 
for _ in range(3):
    row = []
    for i in range(3): 
        row.append(i)
    list.append(row)
print(list)

# 11.   Generate a list with the following structure:
#[
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#]


list = []
 
for _ in range(10):
    row = []
    for i in range(10): 
        row.append(i)
    list.append(row)

print("[")
for row in list:
    print(" "+str(row)+",")
print("]")