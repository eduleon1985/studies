### PT-BR (🇧🇷): 
# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

### EN (🇺🇸):
# Write a program that reads a number and checks whether it is a prime number or not.
# To perform this check, calculate the remainder of the division of the number by 2 
# and then by all odd numbers up to the given number.
# If the remainder of any of these divisions is zero, the number is not prime.

### Etapas:
# 1) Ler o número do usuário
# 2) Verificar os primeiros casos triviais (números menores que 2).
# 3) Testar divisibilidade por 2 e por todos os números ímpares até ele mesmo.
# 4) Exibir o resultado, informando se o número é primo ou não.

numero = int(input("Informe um número inteiro positivo qualquer: "))

if numero < 2:
    print("O número informado não é primo.")
elif numero == 2:
    print("O número é primo!")

# Se o número for par e maior que 2, ele não é primo
if numero % 2 == 0 and numero > 2:
    print("O número não é primo")
else:
    primo = True # Assume que o número é primo até que se prove o contrário
    divisor = 3 # começa testando a partir do número 3, pois vamos ignorar os pares

    while divisor < numero: # Testa até um número antes do próprio número
        if numero % divisor == 0: # Se o número for divisível por "divisor", não é primo
            primo = False
            break # Sai do loop, pois já sabemos que não é primo
        divisor += 2 # Incrementa de 2 em 2 para testar apenas números ímpares

    # Se "primo" continuar True, então o número é primo
    if primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")