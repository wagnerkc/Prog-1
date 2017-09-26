

def main(args):
	num = 4
	den = 1
	mult = 1
	pi = 0
	while (num/den >= 0.0000001):
		pi = pi + mult*(num/den)
		den = den + 2
		mult = mult * (-1)
	print("Pi ", pi)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
