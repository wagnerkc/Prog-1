from random import *

def geraString():
	palavra = ""
	for i in range(6):
		if (i % 2 == 0):
			palavra = palavra + chr(randrange(65,91))
		else:
			palavra = palavra + choice('AEIOU')
	return palavra

def main(args):
	somaAlunos = 0
	contaAprovados = 0
	contaReprovados = 0
	disciplina = input("Digite o código da disciplina ou deixe vazio para sair: ")
	#for disciplinas in range(5):
	while (disciplina != ""):
		#disciplina = geraString()
		#qteAlunos = randrange(4,10)
		qteAlunos = int(input("Digite a quantidade de alunos: "))
		somaAlunos = somaAlunos + qteAlunos
		print("Disciplina: %s" % disciplina)
		somaMediaDisciplina = 0
		maiorMedia = 0
		menorMedia = 101
		matrMenorMedia = ""
		matrMaiorMedia = ""
		while (qteAlunos > 0):
		'''
		for alunos in range(qteAlunos):
			matricula = geraString()
			n1 = randrange(30,101)
			n2 = randrange(30,101)
			n3 = randrange(30,101) 
			frequencia = randrange(50,101)
			'''
			matricula = input("Digite a matricula do aluno: ")
			n1 = float(input("Digite a 1 nota do aluno: "))
			n2 = float(input("Digite a 2 nota do aluno: "))
			n3 = float(input("Digite a 3 nota do aluno: "))
			frequencia = int(input("Digite a frequencia do aluno: "))
			
			media = (n1*2+n2*3+n3*5)/10
			somaMediaDisciplina = somaMediaDisciplina + media
			if (media > maiorMedia):
				maiorMedia = media
				matrMaiorMedia = matricula
			elif (media < menorMedia):
				menorMedia = media
				matrMenorMedia = matricula
			if (media >=60) and (frequencia >= 72):
				situacao = "Aprovado"
				contaAprovados = contaAprovados + 1
			elif (media < 60) and (frequencia >=72):
				situacao = "Reprovado por Nota"
				contaReprovados = contaReprovados + 1
			elif (media >= 60) and (frequencia < 72):
				situacao = "Reprovado por Falta"
				contaReprovados = contaReprovados + 1
			else:
				situacao = "Reprovado por Nota e Falta"
				contaReprovados = contaReprovados + 1
			print("Matricula: %s, Media: %.2f, Frequ: %d, Sit: %s" %(matricula,media,frequencia,situacao))
			qteAlunos = qteAlunos - 1
		print("Média da disciplina: %.2f" % (somaMediaDisciplina/qteAlunos))
		print("Maior media da disciplina: %s - %.2f" % (matrMaiorMedia, maiorMedia))
		print("Maior media da disciplina: %s - %.2f" % (matrMenorMedia, menorMedia))
		print("\n")
		disciplina = input("Digite o código da disciplina ou deixe vazio para sair: ")
	print("Porcentagem de Aprovados = %.2f %%" % ((contaAprovados*100)/somaAlunos))
	print("Porcentagem de Reprovados = %.2f %%" % ((contaReprovados*100)/somaAlunos))
	return 0













if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
