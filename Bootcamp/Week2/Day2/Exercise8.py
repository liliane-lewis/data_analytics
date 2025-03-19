#!/usr/bin/python3

#Exercise 8 : Star Wars Quiz
#Instructions

#This project allows users to take a quiz to test their Star Wars knowledge.
#The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

#Here is an array of dictionaries, containing those questions and answers
#
#data = [
#    {
#        "question": "What is Baby Yoda's real name?",
#        "answer": "Grogu"
#    },
#    {
#        "question": "Where did Obi-Wan take Luke after his birth?",
#        "answer": "Tatooine"
#    },
#    {
#        "question": "What year did the first Star Wars movie come out?",
#        "answer": "1977"
#    },
#    {
#        "question": "Who built C-3PO?",
#        "answer": "Anakin Skywalker"
#    },
#    {
#        "question": "Anakin Skywalker grew up to be who?",
#        "answer": "Darth Vader"
#    },
#    {
#        "question": "What species is Chewbacca?",
#        "answer": "Wookiee"
#    }
#]


#    Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. 
#   Create a list of wrong_answers
#    Create a function that informs the user of his number of correct/incorrect answers.
#    Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
#    If he had more then 3 wrong answers, ask him to play again.

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_questions():
    count_correct = 0
    count_incorrect = 0
    wrong_answers = []

    for q in data:
        print(q["question"])
        ans = input("Your answer: ").strip()

        if ans.lower() == q["answer"].lower():
            count_correct += 1
        else: 
            count_incorrect += 1
            wrong_answers.append({"question": q["question"], "your_answer": ans, "correct_answer": q["answer"]})

    return count_correct, count_incorrect, wrong_answers

def show_results(count_correct, count_incorrect, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct answers: {count_correct}")
    print(f"Incorrect answers: {count_incorrect}")

    if wrong_answers:
        print("\nHere are the questions you got wrong:")
        for item in wrong_answers:
            print(f"{item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}\n")

    if count_incorrect > 3:
        retry = input("You had more than 3 wrong answers. Do you want to try again? (yes/no): ").strip().lower()
        if retry == "yes":
            main()
    elif count_correct == 6:
        print("You got everything right. You are a Jedi master!")

def main():
    count_correct, count_incorrect, wrong_answers = ask_questions()
    show_results(count_correct, count_incorrect, wrong_answers)

# Rodando o quiz
main()