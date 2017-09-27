#2
def main(args):
	entrada1=float(input("entre um numero:"))
	if entrada1<0:
		resultado=entrada1*-1
	else:
		resultado=entrada1
	print(resultado)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
