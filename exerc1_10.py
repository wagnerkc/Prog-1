#10
# O custo de um carro novo ao consumidor é a soma do custo 
# de fábrica com a porcentagem do distribuidor e dos impostos 
# (aplicados ao custo de fábrica). Supondo que o percentual 
# do distribuidor seja de 28% e os impostos de 45%, escrever um
# algoritmo para ler o custo de fábrica de um carro, calcular e 
# escrever o custo final ao consumidor.
def main(args):
	
	custo = float(input("Digite o valor de custo do veiculo: "))
	#p = float(input("Digite a porcentagem do distribuidor: "))
	#imposto = float(input("Digite a porcentagem de impostos: "))
	p = 28
	imposto = 45
	
	custoFinal = custo + custo*p/100 + custo*imposto/100
	
	print("Custo Final do veículo = %.2f" % custoFinal)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
