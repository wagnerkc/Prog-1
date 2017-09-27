#!/usr/bin/env python
from random import randrange

def main(args):
	n = int(input("Digite o valor limite: "))
	for i in range(1,n+1):
		print(i)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
