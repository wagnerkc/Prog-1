#6
def main(args):
	a=float(input("entre um numero:"))
	b=float(input("entre outro numero:"))
	c=float(input("entre outro numero:"))
	if (a < b) and (a < c):
		if (b < c):
			print("Ordem crescente %d, %d e %d" % (a,b,c))
		else:
			print("Ordem crescente %d, %d e %d" % (a,c,b))
	elif (b < c):
		if (a < c):
			print("Ordem crescente %d, %d e %d" % (b,a,c))
		else:
			print("Ordem crescente %d, %d e %d" % (b,c,a))
	elif (a < b):
		print("Ordem crescente %d, %d e %d" % (c,a,b))
	else:
		print("Ordem crescente %d, %d e %d" % (c,b,a))
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
