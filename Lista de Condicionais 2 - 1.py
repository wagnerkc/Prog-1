#1
def main(args):
	entrada1=int(input("entre um numero:"))
	entrada2=int(input("entre outro numero:"))
	if entrada1<entrada2:
		resultado=entrada2-entrada1
	else:
		resultado=entrada1-entrada2
	print(resultado)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
