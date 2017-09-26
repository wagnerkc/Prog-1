

def main(args):
	#binario = 11111000001111
	binario = int(input("Digite um codigo binario: "))
	decimal = 0
	potencia = 0
	if (binario > 0):
		flag = True
	else:
		flag = False
	print(binario,end = " ")
	while (binario > 0):
		resto = binario % 10
		decimal = decimal + resto*2**potencia
		potencia = potencia + 1
		binario = binario // 10
	if (flag):
		print(decimal)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
