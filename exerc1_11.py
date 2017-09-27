#10
# Uma revendedora de carros usados paga a seus funcionários 
# vendedores um salário fixo por mês, mais uma comissão também 
# fixa para cada carro vendido e mais 5% do valor das vendas 
# por ele efetuadas. Escrever um algoritmo que leia o número 
# de carros por ele vendidos, o valor total de suas vendas, 
# o salário fixo e o valor que ele recebe por carro vendido. 
#Calcule e escreva o salário final do vendedor.
def main(args):
	
	salFixo = float(input("Digite o salario fixo: "))
	comFix = float(input("Digite a comissao por carro vendido: "))
	nCarros = int(input("Quantidade de carros vendidos: "))
	valorTotal = float(input("Digite o valor total dos carros vendidos: "))
		
	salarioFinal = salFixo + comFix*nCarros + 5/100*valorTotal
	
	print("Salário Final = %.2f" % salarioFinal)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
