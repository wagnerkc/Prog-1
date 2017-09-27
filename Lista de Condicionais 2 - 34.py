#34
def main(args):
	id_h1=int(input("Digite a idade do primeiro homem: "))
	id_h2=int(input("Digite a idade do segundo homem: "))
	id_m1=int(input("Digite a idade da primeira mulher: "))
	id_m2=int(input("Digite a idade da segunda mulher: "))
	if (id_h1 > id_h2):
		if id_m1>id_m2:
			soma=id_h1+id_m2
			produto=id_h2*id_m1
		else:
			soma=id_h1+id_m1
			produto=id_h2*id_m2
	else:
		if (id_m1 > id_m2):
			soma=id_h2+id_m2
			produto=id_h1*id_m1
		else:
			soma=id_h2+id_m1
			produto=id_h1*id_m2
	print(soma,produto)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
