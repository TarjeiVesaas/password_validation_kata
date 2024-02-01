class NoCapitalLetterError(Exception):
    pass


class NoLowerCaseError(Exception):
    pass


class NoDigitsError(Exception):
    pass


class LessThanTwelveError(Exception):
    pass


class NoSpecialCharsError(Exception):
    pass


class HasABlankSpaceError(Exception):
    pass


def has_digits(password_input):
    return any(characters.isdigit() for characters in password_input)


def password_checker(password_attempt):
    if password_attempt.islower():
        print("This password has no capital letters. It's not good enough!")
        raise NoCapitalLetterError
    elif password_attempt.isupper():
        print("This password has no lower case letters. It's not good enough!")
        raise NoLowerCaseError
    elif not has_digits(password_attempt):
        print("This password has no digits. It's not good enough!")
        raise NoDigitsError
    elif password_attempt.isalnum():
        print("This password has no special characters. It's not good enough!")
        raise NoSpecialCharsError
    elif len(password_attempt) < 12:
        print("This password is too short. Size matters!")
        raise LessThanTwelveError
    elif password_attempt.count(" ") > 0:
        print("This password has a blank space. It shouldn't do. Not good enough!")
        raise HasABlankSpaceError
    return "This password works!"

