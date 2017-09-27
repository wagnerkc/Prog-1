#!/usr/bin/env python
from random import randrange

def main(args):
	cont = 0
	for i in range(10):
		n = randrange(-100,100)
		print(n)
		if (n < 0):
			cont = cont + 1

	print("Qte Negativos = %d" % (cont))
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
