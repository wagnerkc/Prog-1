#!/usr/bin/env python
from random import randrange

def main(args):
	n = int(input("Digite o valor: "))
	for i in range(1,11):
		print("%d x %d = %d" % (n,i,n*i))
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
