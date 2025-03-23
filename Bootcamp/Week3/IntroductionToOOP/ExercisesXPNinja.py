#!/usr/bin/python3

#Exercise 1 : Call History
#Instructions
#
#    Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object 
# create an attribute called call_history which value is an empty list.#
#
#    Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, and add this string to the phone’s call_history.
#
#    Add a method called show_call_history. This method should print the call_history.
#
#    Add another attribute called messages to your __init__() method which value is an empty list.
#
#    Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary 
#    with the following keys:
#        to : the number of another Phone object
#        from : your phone number (also a Phone object)
#        content
#
#    Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
#
#    Test your code !!!

class Phone:
    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []
        print(f"{self.number} created")

    def call(self,other_phone):
        call_entry = f"\n{self.number} called {other_phone.number}"
        print(call_entry)
        self.call_history.append(call_entry)

    def show_call_history(self):
            print("\nCall History:")
            for call in self.call_history:
                print(call)

    def send_message(self, other_phone, content):
        message_entry = {
            'to': other_phone.number,
            'from': self.number,
            'content': content
        }
        self.messages.append(message_entry)
        other_phone.messages.append(message_entry)

    def show_outgoing_messages(self):
        print("\nOutgoing Messages:")
        for message in self.messages:
            if message['from'] == self.number:
                print(f"To {message['to']}: {message['content']}")
        
    def show_incoming_messages(self):
        print("\nIncoming Messages:")
        for message in self.messages:
            if message['to'] == self.number:
                print(f"From {message['from']}: {message['content']}")
         
    def show_messages_from(self, sender_phone):
        print(f"\nMessages from {sender_phone.number}:")
        for message in self.messages:
            if message['from'] == sender_phone.number:
                print(f"To {message['to']}: {message['content']}")


phone1 = Phone("053-863-7890")
phone2 = Phone("052-654-3210")
phone1.call(phone2)
phone2.call(phone1)
phone1.show_call_history()
phone2.show_call_history()
phone1.send_message(phone2, "Hello, how are you?")
phone2.send_message(phone1, "I'm good! How about you?")
phone1.send_message(phone2, "I am very good, thanks.")
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone2.show_outgoing_messages()
phone2.show_incoming_messages()
phone1.show_messages_from(phone2)
phone2.show_messages_from(phone1)
