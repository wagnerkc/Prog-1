#!/usr/bin/env python
from random import randrange

def main(args):
	soma = 0
	for i in range(10):
		n = randrange(100)
		print(n)
		if (n < 40):
			soma = soma + n

	print("Soma dos menores que 40 = %d" % soma)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
