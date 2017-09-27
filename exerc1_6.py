#5
#Escreva um algoritmo para ler um valor (do teclado) 
#e escrever (na tela) o seu antecessor
def main(args):
    n = int(input("Digite um número: "))
    print("O antecessor de %d é %d" % (n,n-1))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
