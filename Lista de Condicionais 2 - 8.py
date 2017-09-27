#8
def main(args):
	a=int(input("entre um numero:"))
	b=int(input("entre outro numero:"))
	c=int(input("entre outro numero:"))
	d=int(input("entre outro numero:"))
	e=int(input("entre outro numero:"))
	maior=a
	menor=a
	if menor>b:
		menor=b
	if menor>c:
		menor=c
	if menor>d:
		menor=d
	if menor>e:
		menor=e
	print ("O menor numero é o %d" % menor)
	if maior<b:
		maior=b
	if maior<c:
		maior=c
	if maior<d:
		maior=d
	if maior<e:
		maior=e
	print ("O maior numero é o %d" % maior)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
