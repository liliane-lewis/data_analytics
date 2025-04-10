#!/usr/bin/python3


#Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of 
#your program, and will rely on AnagramChecker for the anagram-related logic.

#It should do the following:
#
#   Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.


from anagram_checker import AnagramChecker 


def main():
    while True:
        print("\nAnagram program")
        print("1 - Write a word")
        print("2 - Exit\n")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                user_word = input("Enter a single word: ").strip()
                words = user_word.split()
                if len(words) != 1:
                    print("Error: Please enter only a single word.")
                    return
                
                word = words[0]
                if not word.isalpha():
                    print("Error: Only alphabetic characters are allowed.")
                    return

                print(f"Valid word entered: {word}")
                
                a = AnagramChecker()
                anagrams = a.get_anagrams(word)

                print(f"YOUR WORD: {word.upper()}")
                print("this is a valid English word.")
                print("Anagrams for your word:", ", ".join(anagrams))
                
    
            elif choice == "2":
                return 

            else:
                print("Invalid option.")
        except ValueError as e:
            print("Error:", e)




if __name__ == "__main__":
    main()