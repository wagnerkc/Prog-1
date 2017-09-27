#7
def main(args):
	a = float(input("entre um numero:"))
	b = float(input("entre outro numero:"))
	c = float(input("entre outro numero:"))
	d = float(input("entre outro numero:"))
	if (a % 2 == 0) and (a % 9 == 0):
		print(a)
	if (b % 2 == 0) and (b % 9 == 0):
		print(b)
	if (c % 2 == 0) and (c % 9 == 0):
		print(c)
	if (d % 2 == 0) and (d % 9 == 0):
		print(d)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
