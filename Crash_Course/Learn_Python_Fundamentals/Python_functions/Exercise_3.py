#Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.


def check_even_odd(num):
    result = num % 2
    if result == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(4))  # Output: "Even"
print(check_even_odd(7))  # Output: "Odd"
