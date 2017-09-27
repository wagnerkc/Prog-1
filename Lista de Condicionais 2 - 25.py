#26
def main(args):
	a = int(input("entre um numero:"))
	if (a > 0):
		print("O valor é positivo")
	elif (a == 0):
		print("O valor é zero")
	else:
		print("O valor é negativo")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
