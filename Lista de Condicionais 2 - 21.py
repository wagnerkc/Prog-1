#21
def main(args):
	nome=input("Digite seu nome: ")
	sexo=input("Digite (M) para masculino ou (F) para feminino: ")
	altura=float(input("Digite sua altura: "))
	if (sexo.upper() == "M"):
		pesoideal = (72.7 * altura) - 58
	elif (sexo.upper() == "F"):
		pesoideal = (62.1 * altura) - 44.7
	else:
		print("Digitou sexo invalido")
		pesoideal="NA"
	print("%s seu peso ideal é: " % (nome),pesoideal)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
