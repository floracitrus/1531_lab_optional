import sys
try:
	num = int(input("enter numerator: "))
	den = int(input("enter denominator: "))
	result = num/den
except ValueError:
	print("numbers only pls")
	sys.exit()
except ZeroDivisionError:
	print("cannot divide by 0, enter the appropariate denominator")
	sys.exit()

print("you entered nos, %f, %f, and the result of division is %f", numerator, denominator, result)
