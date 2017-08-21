index = int(input())

def fib_sequence(num):
	if num < 2:
		return num

	return (fib_sequence(num-2) + fib_sequence(num-1))
		
print(fib_sequence(index))
