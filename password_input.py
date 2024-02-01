from password_checker import password_checker
import unittest


def passwordinput():
    password = input("Now, please enter a valid password to continue. ")
    try:
        password_checker(password)
    except Exception as y:
        passwordinput()
    else:
        print("Good job! That password finally worked!")
        print("Saving your password...")
        print("Saved!")


from password_checker import password_checker, NoCapitalLetterError, NoLowerCaseError, NoDigitsError, \
    NoSpecialCharsError, LessThanTwelveError, HasABlankSpaceError


print("Welcome to your program.\n")
x = input("Please enter your name. ")
print(" \n\nHello, " + str(x) + ".\n\nIt's a pleasure to meet you.\n")
print("\nTo begin, " + str(x) + ", you need a password.\n\nWe are very fussy about passwords in this program.\n")
print("\nYour password must:\n\nBe at least 12 characters long"
      "\nContain at least one uppercase and one lowercase letter."
      "\nContain one special character, such as – !”#$%&'()*+,-.\\:;<=>?@[/]^_`{|}~"
      "\nContain one digit, and no blank spaces."
      "\nGood Luck.\n")

passwordinput()