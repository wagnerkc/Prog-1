#23
def main(args):
	conta=int(input("Digite o numero da conta: "))
	saldo=float(input("Digite o saldo: "))
	debito=float(input("Digite o dabito: "))
	credito=float(input("Digite o credito: "))
	saldo_atual=saldo-debito+credito
	print("O saldo atual é R$",saldo_atual)
	if (saldo_atual < 0):
		print("Saldo negativo")
	else:
		print("Saldo positivo")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
