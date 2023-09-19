number = int(input("please enter a number"))
if number < 0 or number % 1 != 0:
	print("not a natural number")
else is_prime(number)
---
def is_prime(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return ("composite")
	print("prime")
