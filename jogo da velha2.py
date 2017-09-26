def tabuleiro():
	print(" 1 | 2 | 3 ")
	print("___________\n")
	print(" 4 | 5 | 6 ")
	print("___________\n")
	print(" 7 | 8 | 9 ")

def preencheTabuleiro(c1,c2,c3,c4,c5,c6,c7,c8,c9):
	print(" %s | %s | %s " % (c1,c2,c3))
	print("___________\n")
	print(" %s | %s | %s " % (c4,c5,c6))
	print("___________\n")
	print(" %s | %s | %s " % (c7,c8,c9))
	
def atribuiSimbolo(x):
	if (x == 1):
		simbolo = "O"
	else:	
		simbolo = "X"
	return simbolo
	
def testaVencedor(c1,c2,c3,c4,c5,c6,c7,c8,c9):
	if (c1 == c2) and (c2 == c3):
		vencedor = c1
	elif (c4 == c5) and (c5 == c6):
		vencedor = c4
	elif (c7 == c8) and (c8 == c9):
		vencedor = c7
	elif (c1 == c4) and (c4 == c7):
		vencedor = c1
	elif (c2 == c5) and (c5 == c8):
		vencedor = c2
	elif (c3 == c6) and (c6 == c9):
		vencedor = c3
	elif (c3 == c5) and (c5 == c7):
		vencedor = c5
	elif (c1 == c5) and (c5 == c9):
		vencedor = c5
	else:
		vencedor = "nulo"
	
	return vencedor

def main(args):
	t1 = 0
	t2 = 0
	t3 = 0
	t4 = 0
	t5 = 0
	t6 = 0
	t7 = 0
	t8 = 0
	t9 = 0
	c1 = " "
	c2 = " "
	c3 = " "
	c4 = " "
	c5 = " "
	c6 = " "
	c7 = " "
	c8 = " "
	c9 = " "
		
	tabuleiro()
	jogada = 0
	jogador = 1
	v = "nulo"
	while(jogada < 9) and (v == "nulo"):
		
		pos = int(input("Escolha a posição livre onde quer jogar (1-9)"))
		while (pos < 1 or pos > 9):
			pos = int(input("Escolha a posição VÁLIDA livre onde quer jogar (1-9)"))

		if (pos == 1) and (c1 == " "):
			c1 = atribuiSimbolo(jogador)
		elif (pos == 2) and (c2 == " "):
			c2 = atribuiSimbolo(jogador)
		elif (pos == 3) and (c3 == " "):
			c3 = atribuiSimbolo(jogador)
		elif (pos == 4) and (c4 == " "):
			c4 = atribuiSimbolo(jogador)			
		elif (pos == 5) and (c5 == " "):
			c5 = atribuiSimbolo(jogador)
		elif (pos == 6) and (c6 == " "):
			c6 = atribuiSimbolo(jogador)
		elif (pos == 7) and (c7 == " "):
			c7 = atribuiSimbolo(jogador)
		elif (pos == 8) and (c8 == " "):
			c8 = atribuiSimbolo(jogador)
		elif (pos == 9) and (c9 == " "):
			c9 = atribuiSimbolo(jogador)
			
		if (jogada > 4) and (jogada < 9):
			v = testaVencedor(c1,c2,c3,c4,c5,c6,c7,c8,c9)
			
		jogador = jogador*(-1)
		jogada += 1
		preencheTabuleiro(c1,c2,c3,c4,c5,c6,c7,c8,c9)
	
	print("Vencedor = ",v)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
