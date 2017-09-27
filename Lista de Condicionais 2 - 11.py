#11
def main(args):
	a=int(input("entre um numero:"))
	if (a <= 3):
		print("o numero %d está na faixa" % a)
	else:
		print("o numero %d está fora da faixa" % a)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
