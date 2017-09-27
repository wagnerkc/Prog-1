#!/usr/bin/env python
from random import randrange

def main(args):
	somap = 0
	soman = 0
	cont = 0
	for i in range(20):
		n = randrange(-100,100)
		print(n)
		if (n >= 0):
			somap = somap+n
		else:
			soman = soman + n
			cont = cont + 1
	
	print("ùltimo valor de i = ",i)
	print("Média dos Negativos = %.2f" % (soman/cont))
	print("Soma Positivos = %d" % somap)		
		

		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
