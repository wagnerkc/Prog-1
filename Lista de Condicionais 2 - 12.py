#12
def main(args):
	a=int(input("entre um numero:"))
	if (a > 10):
		print("o numero %d é maior que 10" % a)
	else:
		print("o numero %d não é maior que 10" % a)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
