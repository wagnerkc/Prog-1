#13
def main(args):
	a=int(input("entre um numero:"))
	if (a >= 0):
		print("o numero %d é positivo" % a)
	else:
		print("o numero %d é negativo" % a)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
