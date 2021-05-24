def converter(decimal):
    binary = ""
    while decimal >= 1:
	    digit = str(int(decimal%2))
	    decimal = int(decimal/2)
	    binary = digit + binary
    return binary
	

def main():
    number = int(input("enter a decimal number here: "))
    result = converter(number)
    print(result)
	
main()