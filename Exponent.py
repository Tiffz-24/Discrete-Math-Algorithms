def exp(current, exponent):
	result = 1

	while exponent >= 1:
		if exponent % 2 == 1:
			result = result * current
			exponent -=1
		else: 
			current = current * current
			exponent = exponent / 2
	return result

def main():
	base = int(input("enter positive integer for base here: "))
	power = int(input("enter positive integer for power here: "))
	result = exp(base, power)
	print(result)

main()
