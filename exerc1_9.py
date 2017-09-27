#8
# Escreva um algoritmo para ler o salário mensal atual de um 
# funcionário e o percentual de reajuste. 
# Calcular e escrever o valor do novo salário.
def main(args):
	
	salario = float(input("Digite o salário: "))
	p = float(input("Digite o percentual de reajuste: "))
	salario = salario+salario*p/100
	print("Novo salário = %.2f" % salario)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
