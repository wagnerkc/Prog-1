#16
def main(args):
	ano=int(input("o ano de nascimento"))
	idade=2017-ano
	if idade<16 :
		print("Não pode votar")
	else:
		print("Pode votar")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
