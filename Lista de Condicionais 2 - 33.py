#33
def main(args):
	litros=float(input("Entre com o numero de litros: "))
	comb=input("Tipo de combustivel (A-Alcool/G-Gasolina): ")
	if comb.upper() == "G":
		preco=3.3
		if litros<=20 :
			desconto=0.04
		else:
			desconto=0.06
	elif comb.upper() == "A":
		preco=2.9
		if litros<=20 :
			desconto=0.03
		else:
			desconto=0.05
	else:
		print("Combustivel incorreto")
		preco=0.0
		desconto=0.0
	valor_pagar=litros*preco*(1-desconto)
	print (valor_pagar)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
