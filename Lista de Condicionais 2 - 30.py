#30
def main(args):
	t1=input("Digite o nome do time1: ")
	t2=input("Digite o nome do time2: ")
	p1=int(input("Digite o numero de gols do time 1: "))
	p2=int(input("Digite o numero de gols do time 2: "))
	if (p1 > p2):
		print("%s é o vencedor" % t1)
	elif (p2 > p1):
		print("%s é o vencedor" % t2)
	else:
		print("empate")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
