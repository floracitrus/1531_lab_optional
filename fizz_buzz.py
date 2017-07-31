n = input("Enter a number: ")
print ['Fizz'*(n%3<1)+'Buzz'*(n%5<1)]
print ['Fizz'*(i%3<1)+'Buzz'*(i%5<1) or i for i in range(1,101)]