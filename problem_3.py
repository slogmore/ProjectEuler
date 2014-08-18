

from math import sqrt

def is_prime(number):
	root = int(sqrt(number)) +  1
	for i in range(2, root):
		if number % i == 0:
			return False
	return True

def main():
	to_factorize = 600851475143
	found = False
	divide_with = 1
	while not found:
		if (float(to_factorize) / divide_with).is_integer():
			if is_prime(to_factorize / divide_with):
				print to_factorize / divide_with
				found = True
		divide_with += 2

if __name__=="__main__":
	main()



