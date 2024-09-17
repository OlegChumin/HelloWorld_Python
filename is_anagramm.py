#def function_name(parameters):
    # functions body
    # return result
import sys

# lisTen Silent - are anagrams
string_1 = input("Pls. print 1st string: ")
string_2 = input("Pls. print 2nd string: ")

if len(string_1) != len(string_2):
    sys.exit()


def are_anagrams(string_1, string_2):
    string_1 = string_1.replace(" ", "").lower()
    string_2 = string_2.replace(" ", "").lower()

    # sorting string Alphabetically a, b, c, d....
    string_1 = sorted(string_1)
    print(f"'{string_1}'")

    string_2 = sorted(string_2)
    print(f"'{string_2}'")

    if string_1 == string_2:
        return True
    else:
        return False


print(f"Pls. print 2nd '{are_anagrams(string_1, string_2)}'")





