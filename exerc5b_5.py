#!/usr/bin/env python
from random import randrange

def main(args):
	soma = 0
	cont = 0
	for i in range(10):
		n = randrange(10)
		print(n)
		soma = soma + n
		cont = cont + 1
	print("ùltimo valor de i = ",i)
	print("Soma = %.2f" % (soma/cont))
	print("Soma = %.2f" % (soma/(i+1)))		
		

		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
