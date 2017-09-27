#!/usr/bin/env python
from random import randrange

def main(args):
	soma = 0
	for i in range(10):
		n = randrange(10)
		print(n)
		soma = soma + n

	print("Soma = %d" % soma)	
		

		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
