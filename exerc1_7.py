#7
# Faça um algoritmo que leia a idade de uma pessoa expressa 
# em anos, meses e dias e escreva a idade dessa pessoa expressa 
# apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
def main(args):
	print("Informe quantos anos, meses e dias você tem de idade")
	a = int(input("Digite os anos: "))
	m = int(input("Digite os meses: "))
	d = int(input("Digite os dias: "))
	idade = a * 365 + m * 30 + d
	print("Sua idade em dias é  %d" % idade)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
