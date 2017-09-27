#36
def main(args):
	codigo_usuario=int(input("Digite o codigo usuário:"))
	if (codigo_usuario == 1234):
		senha_usuario=int(input("Digite a senha:"))
		if (senha_usuario == 9999):
			print("Acesso permitido")
		else:
			print("Senha incorreta!")
	else:
		print("Usuário inválido!")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
