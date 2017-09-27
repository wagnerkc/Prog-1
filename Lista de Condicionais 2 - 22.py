#22
def main(args):
	sf=float(input("Digite o salario fixo: "))
	vendas=float(input("Digite o valor das vendas: "))
	if (vendas < 1500):
		comissao=vendas*0.03
	else:
		comissao=vendas*0.05
	salario = sf + comissao
	print("Salario fixo = R$ %.2f, Comissão = R$ %.2f" % (sf,comissao))
	print("Salário Total = R$ %.2f" % salario)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
