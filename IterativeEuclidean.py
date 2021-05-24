def gcd(m, n):
	dividend = m
	divisor = n
	remainder = dividend%divisor 
	while remainder!=0:
	    dividend = divisor            
	    divisor = remainder            
	    remainder = dividend % divisor  
	return divisor
	
def main():
    dividend = int(input("please enter an integer for the dividend: "))
    divisor = int(input("please enter an integer for the divisor: "))
    print(gcd(dividend, divisor))
	
main()