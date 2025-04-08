#!/usr/bin/python3

#Part 1
#
#    You will have to create two classes:
#        Human
#        Queue
#
#
#Human
#
#Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str).
#  Its blood type can be “A”, “B”, “AB” or “O”.
#
#This class has no methods.
#
#
#Queue
#
#Represents a queue of humans waiting for their vaccine.
#It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
#
#This class is useful to manage who will get vaccinated in priority. It has the following methods: 
#
#
#    add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the
#    list (at index 0) before every other.
#
#    find_in_queue(self, person) : Returns the index of a human in the queue.
#
#    swap(self, person1, person2): Swaps person1 with person2.
#
#    get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
#
#    get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
#
#    sort_by_age(self) : Sorts the queue
#        first the priority people
#        then, the older people
#        then the younger people
#
#Every human returned by get_next and get_next_blood_type is removed from the list.
#Those functions return None if the list is empty (ie. no one in the list).
#
#Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted. 

#Part 2
#Human
#
#Create an attribute family for the Human class.
#
#Initialized as empty, family is a list of all the humans that are living in the same house with this human.
#Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.
#
#
#Queue
#
#Add the rearrange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

class Human:

    family = []

    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def add_family_member(self, person):
        self.family.append(person) 

class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        ''' Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the
    list (at index 0) before every other.'''
        if person.priority or person.age > 60:
            self.humans = [person] + self.humans
        else:
            self.humans += [person]

    def find_in_queue(self, person):
        ''': Returns the index of a human in the queue.'''
        for idx in range(len(self.humans)):
            if self.humans[idx] == person:
                return idx
        return -1

    def swap(self, person1, person2):
        '''Swaps person1 with person2.'''
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        if idx1 != -1 and idx2 != -1:
            temp = self.humans[idx1]
            self.humans[idx1] = self.humans[idx2]
            self.humans[idx2] = temp

    def get_next(self):
        ''' Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.'''
        if len(self.humans) == 0:
            return None
        next_person = self.humans[0]
        self.humans = self.humans[1:]  #Remove the first one
        return next_person

    def get_next_blood_type(self, blood_type):
        '''Returns the first human with this specific blood type.'''
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return person
        return None

    def sort_by_age(self): 
        
        '''Sorts the queue
        first the priority people
        then, the older people
        then the younger people'''
        priority = []
        older = []
        younger = []


        for human in self.humans:
            if human.priority:
                priority += [human]
            elif human.age > 60:
                older += [human]
            else:
                younger += [human]

        self.humans = priority + older + younger

    def rearrange_queue(self):
        i = 0
        while i < len(self.humans) - 1:
            current = self.humans[i]
            next_person = self.humans[i + 1]

            if next_person in current.family:
                found = False
                for j in range(i + 2, len(self.humans)):
                    if self.humans[j] not in current.family:
                        temp = self.humans[i + 1]
                        self.humans[i + 1] = self.humans[j]
                        self.humans[j] = temp
                        found = True
                        break
                if not found:
                    i += 1
            else:
                i += 1 

person1 = Human("1", "Carol", 30, False, "A")
person2 = Human("2", "Roberto", 40, False, "O")
person3 = Human("3", "Carlos", 25, False, "B")
person4 = Human("4", "Marcos", 35, False, "AB")

person1.add_family_member(person2)

q = Queue()
q.add_person(person1)
q.add_person(person2)
q.add_person(person3)
q.add_person(person4)

print([p.name for p in q.humans])  
q.rearrange_queue()
print([p.name for p in q.humans]) 

