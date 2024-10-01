#Questão 1:
number = int(input("Digite um número: "))

first_number = 0
second_number = 1

while second_number <= number:
    
    if second_number == number:
        print("O número" ,number, "está na sequência Fibonacci.")
        break

    first_number, second_number = second_number, first_number + second_number

    if second_number > number:
        print("O número", number, "não está na sequência Fibonacci.")
        break
   
