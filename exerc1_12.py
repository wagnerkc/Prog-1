#12
# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, 
# calcular e escrever o valor correspondente em graus Celsius. 
# Fórmula: C/5 = (F-32)/9
def main(args):
	
	f = float(input("Digite a temperatura em F: "))
	c = 5*(f-32)/9
	
	print("%.2f Fahrenheit = %.2f Celsius" % (f,c))

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
