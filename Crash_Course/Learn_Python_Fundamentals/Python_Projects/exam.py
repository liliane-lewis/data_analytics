from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------


def brute_force_zip():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter1 in alphabet:
        for letter2 in alphabet:
            find_me = f"{letter1}{letter2}"
            secret_password = find_me + 'bcmpda'
            print(find_me)

            d = unzip_with_7z(zip_file_path, dest_path, secret_password)
            if d:
                return find_me 
    return("NOT FOUND")
# Call function
password_found = brute_force_zip()
print(f"Password found: {password_found}bcmpda")