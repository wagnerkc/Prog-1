#5
def main(args):
	A = float(input("Digite a primeira coeficiente:"))
	B = float(input("Digite o segundo coeficiente:"))
	C = float(input("Digite o terceiro coeficiente:"))
	delta =  B**2 - 4*A*C
	if (A == 0):
		print("Não foi possivel resolver, digite um coeficiente A diferente de zero")
	else:
		if (delta < 0):
			print("A equação não possui raizes reais")
		elif (delta == 0):
			raiz = -B/(2*A)
			print("A raiz possui apenas uma raiz real = %.2f" % raiz)
		else:
			raiz1 = (-B+(delta**0.5))/(2*A)
			raiz2 = (-B-(delta**0.5))/(2*A)
			print("A raiz possui duas raizes reais sendo %.2f e %.2f" % (raiz1,raiz2))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
