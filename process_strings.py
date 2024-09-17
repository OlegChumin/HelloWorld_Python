import sys

string_from_input = input("Введите строку текста: ")
if string_from_input == "":
    print(f"'{string_from_input}' is empty")
    sys.exit()

if len(string_from_input) > 10:
    print(f"The string '{string_from_input}' is long with length = {len(string_from_input)}")
else:
    print(f"The string '{string_from_input}' is short with length = {len(string_from_input)}")

if string_from_input[0] == 'a':
    print(f"The string '{string_from_input}' starts with 'a'")
else:
    print(f"The string '{string_from_input}' does not starts with 'a'")


if 'm' in string_from_input:
    print(f"'m' is in the string '{string_from_input}'")
else:
    print(f"'m' is not in the string '{string_from_input}'")

some_substring = "Python"

if some_substring in string_from_input:
    print(f"The string '{string_from_input}' contains '{some_substring}'")

char = '7'

if char.isdigit():
    print(f"'{char}' is digit")
elif char.isalpha():
    print(f"'{char}' is letter")
else:
    print(f"'{char}' is neither a digit nor a letter")
