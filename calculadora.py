N1 = int(input("Escreva o valor de N1: "))
N2 = int(input("Escreva o valor de N2: "))
 
op = int(input("Digite 1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão ou 5 para ver o resto da divisão: "))

if op == 1:
    print("Soma dos dois numeros: ", N1 + N2)

elif op == 2:
    print("Subtração dos dois numeros: ", N1 - N2)

elif op == 3:
    print("Multiplicação dos dois numeros: ", N1 * N2)

elif op == 4: 
    print("Divisão dos dois numeros: ", N1 / N2)

elif op == 5:
    print("O resto da divisão dos dois numeros: ", N1 % N2)
