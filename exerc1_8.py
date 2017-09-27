#8
# Escreva um algoritmo para ler o número total de eleitores de um
# município, o número de votos brancos, nulos e válidos. 
# Calcular e escrever o percentual que cada um representa 
# em relação ao total de eleitores.
def main(args):
	
	total = int(input("Digite o total de eleitores do município: "))
	brancos = int(input("Digite o total de votos em branco: "))
	nulos = int(input("Digite o total de votos nulos: "))
	validos = int(input("Digite o total de votos válidos: "))
	
	print("Percentual de votos em branco = %.2f %%" % (brancos*100/total))
	print("Percentual de votos nulos = %.2f %%" % (nulos*100/total))
	print("Percentual de votos válidos = %.2f %%" % (validos*100/total))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
