import unittest

from password_checker import password_checker, NoCapitalLetterError, NoLowerCaseError, NoDigitsError, \
    NoSpecialCharsError, LessThanTwelveError, HasABlankSpaceError


class MyTestCase(unittest.TestCase):
    def test_password_needs_capital_letter(self):

        # Arrange
        password_input = "password"

        # Assert
        with self.assertRaises(NoCapitalLetterError):
            password_checker(password_input)

    def test_password_needs_lower_case(self):

        # Arrange
        password_input = "PASSWORD"

        # Assert
        with self.assertRaises(NoLowerCaseError):
            password_checker(password_input)

    def test_password_needs_one_digit(self):

        # Arrange
        password_input = "Password"

        # Assert
        with self.assertRaises(NoDigitsError):
            password_checker(password_input)

    def test_password_needs_special_character(self):

        # Arrange
        password_input = "Password123"

        # Assert
        with self.assertRaises(NoSpecialCharsError):
            password_checker(password_input)

    def test_password_more_than_eleven(self):

        # Arrange
        password_input = "Password12?"

        # Assert
        with self.assertRaises(LessThanTwelveError):
            password_checker(password_input)

    def test_password_has_white_space(self):

        #  Arrange
        password_input = "Pass word123?"

        # Assert
        with self.assertRaises(HasABlankSpaceError):
            password_checker(password_input)
