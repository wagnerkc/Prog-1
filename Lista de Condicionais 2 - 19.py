#19
def main(args):
	hi = int(input("Digite a hora inicial:" ))
	hf = int(input("Digite a hora final"))
	if (hi > hf):
		total = (24-hi) + hf
	elif (hi == hf):
		total = 24
	else:
		total = hf - hi
	print("Numero de horas jogado = ", total)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
