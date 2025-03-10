#!/usr/bin/python3


#exercises Strings

descripton = "strings are..."
new_description=(descripton.upper()).replace("ARE","IS")
print(new_description.split()[0])





bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))
bank_balance=int(bank_balance)
phone_number=str(phone_number)
print(type(bank_balance))
print(type(phone_number))

first_name="Liliane"
last_name="Zukerman"
print(f"{first_name} {last_name}")
