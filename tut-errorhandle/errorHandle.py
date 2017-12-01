# define Python user-defined exceptions
class Error(Exception):
 "Base class for other exceptions"
 pass
class InputTooSmallError(Error):
 "Raised when the input value is too small"
 pass
class InputTooLargeError(Error):
 "Raised when the input value is too large"
 pass
# user guesses a number until he/she gets it right
# user needs to guess this number
number = 20
while True:
 try:
 i_num = int(input("Enter a number: "))
 if i_num < number:
 raise InputTooSmallError
 elif i_num > number:
 raise InputTooLargeError
 break
 except InputTooSmallError:
 print("This value is too small, try again!")
 except InputTooLargeError:
 print("This value is too large, try again!")
 except:
 print("Invalid value, try again!")
print("Congratulations! You guessed it correctly.")