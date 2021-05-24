def getCoefficient(n, k):
	if k > n:
		return 0
	
	if k == 0 or k == n:
		return 1
	
	return getCoefficient(n-1, k-1) + getCoefficient(n-1, k)
	
def main():
	n = int(input("enter n here: "))
	k = int(input("enter k here: "))
	print(getCoefficient(n, k))
	
main()
	