#Questão 2
frase = input("Digite uma frase: ")

count = 0
count_A = 0
count_a = 0

for letra in frase:
    if letra.lower() == "a":
        count += 1

    if letra == "a":
        count_a += 1

    if letra == "A":
        count_A += 1


print("A letra 'A' aparece ", count, " vezes na frase")
print("A letra 'A' em caixa alta aparece ",count_A, " vezes na frase")
print("A letra 'a' em caixa baixa aparece ", count_a, " vezes na frase")

