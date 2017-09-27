#14
def main(args):
	macas=int(input("entre um numero de maças compradas:"))
	if (macas >= 12):
		print("Valor da compra = %.2f" % (macas*1))
	else:
		print("Valor da compra = %.2f" % (macas*1.3))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
