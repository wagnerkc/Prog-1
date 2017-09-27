#18
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	if (a < b):
		print ("Em ordem crescente: %d e %d" % (a,b))
	else:
		print ("Em ordem crescente: %d e %d" % (b,a))  
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
