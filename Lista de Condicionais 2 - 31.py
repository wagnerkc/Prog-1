#31
def main(args):
	a=int(input("Digite um valor: "))
	b=int(input("Digite outro valor: "))
	if (a > b):
		print("O primeiro número é o maior")
	elif (b > a):
		print("O segundo número é o maior")
	else:
		print("Os números são iguais")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
