#20
def main(args):
	vh = float(input("Valor da hora:" ))
	ht = int(input("Horas trabalhadas no mes: "))
	if (ht > 160):
		he = ht - 160
		sal = (160*vh) + (he*vh*1.5)
	else:
		sal = ht*vh
	print("O salário total = ", sal)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
