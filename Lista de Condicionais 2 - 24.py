#24
def main(args):
	qest=int(input("Digite a quantidade em estoque"))
	qmin=int(input("Digite o estoque minimo"))
	qmax=int(input("Digite o estoque maximo"))
	estmedio=(qmax+qmin)/2
	if qest<estmedio:
		print("Efetuar compra!")
	else:
		print("Não é necessário efetuar compra!")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
