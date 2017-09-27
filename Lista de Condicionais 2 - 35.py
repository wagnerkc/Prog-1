#35
def main(args):
	morango = float(input("Digite a quantidade de morango: " ))
	maca = float(input("Digite a quantidade de maçã: "))
	desconto = 0
	if (morango <= 5):
		vmorango = morango * 2.5
	else:	
		vmorango = morango * 2.2	
	if (maca <= 5):
		vmaca = maca * 1.8
	else:	
		vmaca = maca * 1.5		
	total_peso = morango + maca	
	total_valor = vmorango + vmaca	
	if (total_peso > 8) or (total_valor > 25):
		desconto = total_valor * 0.1
	print("Valor da compra = ",total_valor-desconto)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
