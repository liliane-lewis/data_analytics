#Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.

def check_sign(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
check_sign(10)  # Output: "Positive"
check_sign(-5)  # Output: "Negative"
check_sign(0)   # Output: "Zero"