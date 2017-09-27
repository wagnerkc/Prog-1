#26
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	c=int(input("entre outro numero:"))
	if (a > b) and (a > c):
		print("O maior número é %d" % a)
	elif (b > c):
		print("O maior número é %d" % b)
	else:
		print("O maior número é %d" % c)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
