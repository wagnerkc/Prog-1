#10
def main(args):
	a=int(input("entre um numero:"))
	if (a >= 1) and (a <= 9):
		print("o numero está na faixa")
	else:
		print("o numero está fora da faixa")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
