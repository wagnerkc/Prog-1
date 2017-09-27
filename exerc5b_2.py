#!/usr/bin/env python


def main(args):
	for i in range(21):
		if(i % 2 == 0):
			print(i)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
