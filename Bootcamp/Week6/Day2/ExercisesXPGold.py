#Exercise 1 : Authentication database
#Instructions
#PART 1: Authentication CLI - login:
#
#    Create a dictionary that contains users: each key will represent a username, and each value will 
# represent that user’s password. Initialize this dictionary with 3 users & passwords.

users = {
    "Amelia": "12345678",
    "Beto": "password",
    "Cristina": "toto"
}

#Create a loop that does the following:
#
#    If the user inputs “exit”, break out of the loop.
#    If the user inputs “login”, ask them for their username and password.
#        If the user’s details exist print “you are now logged in”.
#        If the user is successfully logged in, store the username in a variable called logged_in 
# so we can track it later.


while True:
    command = input("Enter command (login / exit): ")
    if command == "exit":
        break
    elif command == "login":
        username = input("Username: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print("You are logged in!!!")
            logged_in = username
        else:
            print("Invalid credentials!!!")

#PART 2 : Authentication CLI - signup:
#
#Continuation of the Exercise Above - Authentication CLI - login
#
#    If the user does not exist ask if they would like to sign up:
#        Ask the user for a username and make sure it doesn’t exist as a key in our dictionary, if the username is not valid continue asking the user to input a username.
#        Ask the user for a password. The password is the value.

            signup = input("Would you like to sign up? (yes/no): ")
            if signup == "yes":
                while True:
                    new_user = input("Choose a username: ")
                    if new_user in users:
                        print("Username already exists. Try another.")
                    else:
                        break
                new_pass = input("Choose a password: ")
                users[new_user] = new_pass
                print(f"User '{new_user}' successfully signed up!")
