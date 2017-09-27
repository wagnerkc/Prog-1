#29
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	c=int(input("entre outro numero:"))
	if (a < b) and (a < c):
		if (b < c):
			print("Em ordem %d, %d e %d" % (a,b,c))
		else:
			print("Em ordem %d, %d e %d" % (a,c,b))
	elif (b < c):
		if (a < c):
			print("Em ordem %d, %d e %d" % (b,a,c))
		else:
			print("Em ordem %d, %d e %d" % (b,c,a))			
	else:
		if (a < b):
			print("Em ordem %d, %d e %d" % (c,a,b))
		else:
			print("Em ordem %d, %d e %d" % (c,b,a))	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
