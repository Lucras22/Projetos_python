print("Seja bem vindo")

#condição

idade = int(input("Diga sua idade: "))
 
if idade < 16:
        print("Você não pode votar!")
elif idade >= 16 and idade < 18:
        print("Voto opcional!")
elif idade >= 18 and idade < 70:
        print("Voto obrigatorio!")
elif idade >= 70:
        print("Voto opcional!")
else:
    print("Isso não é uma idade!")

#estrutura de repetição:

#for
nomes = ["Pedro", "João", "Leticia", "Lucas"]
for n in nomes:
    print(n)

#while
contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1
