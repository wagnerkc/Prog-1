def main(args):
	nota1=float(input("Digite a primeira nota:"))
	nota2=float(input("Digite a segunda nota:"))
	nota3=float(input("Digite a terceira nota:"))
	nota4=float(input("Digite a quarta nota:"))
	media=(nota1+nota2+nota3+nota4)/4
	if (media >= 7):
		print("Aluno aprovado com media %.2f" % media)
	else:
		exame=float(input("Digite a nota do exame:"))
		media=(media+exame)/2
		if (media >= 5):
			print("Aluno aprovado no EXAME com media %.2f" % media)
		else:
			print("Aluno reprovado com média %.2f" % media)	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
