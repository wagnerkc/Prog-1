#27
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	c=int(input("entre outro numero:"))
	if (a > b) and (a > c):
		maior = a 
		if (b > c):
			segundo = b
		else:
			segundo = c
	elif (b > c):
		maior = b
		if (a > c):
			segundo = a
		else:
			segundo = c			
	else:
		maior = c
		if (a > b):
			segundo = a
		else:
			segundo = b	
	print("O maior número é %d e o segundo maior %d" % (maior,segundo))
	print("A soma dos dois = %d" % (maior+segundo))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
