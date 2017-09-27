#17
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	if (a > b):
		print ("O maior numero é %d" % a)
	else:
		print ("O maior numero é %d" % b)  
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
