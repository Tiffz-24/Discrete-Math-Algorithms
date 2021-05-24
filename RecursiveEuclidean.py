def gcd(m, n):
	remainder = m % n
	if remainder == 0:
		return n
	else:
		return gcd(n, remainder)
	
def main():
    dividend = int(input("please enter an integer for the dividend: "))
    divisor = int(input("please enter an integer for the divisor: "))
    print(gcd(dividend, divisor))
	
main()