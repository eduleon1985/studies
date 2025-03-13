### PT-BR (🇧🇷): 
# Modifique o programa anterior (pag149-ex5.23.py) de forma a ler um número n.
# Imprima os n primeiros números primos.

### EN (🇺🇸):
# Modify the previous program (pag149-ex5.23.py) to read a number n.
# Print the first n prime numbers.

# git commit -m "Modified prime number checker to print the first n prime numbers."

contador_primos = 0  # Contador de números primos encontrados
numero_atual = 2  # Começamos testando pelo primeiro número primo

while True:  # Loop infinito para manter o programa rodando até o usuário decidir parar
    numero = input("Pressione ENTER para ver o próximo número primo ou digite 0 para sair: ")
    
    if numero == "0":  # Se o usuário digitar 0, o programa encerra
        print("Programa encerrado.")
        break
    
    # Verifica se numero_atual é primo
    primo = True  # Assume que o número atual é primo até provar o contrário
    
    if numero_atual < 2:  # Números menores que 2 não são primos
        primo = False
    elif numero_atual == 2:  # O número 2 é primo
        primo = True
    elif numero_atual % 2 == 0:  # Números pares maiores que 2 não são primos
        primo = False
    else:
        divisor = 3  # Começa testando pelo 3
        while divisor < numero_atual:  # Loop para verificar se é primo
            if numero_atual % divisor == 0:
                primo = False  # Encontrou um divisor, não é primo
                break  # Sai do loop pois já sabemos que não é primo
            divisor += 2  # Testa apenas números ímpares

    if primo:  # Se for primo, exibe o número e incrementa o contador de primos
        print(f"Primo encontrado: {numero_atual}")
        contador_primos += 1

    numero_atual += 1  # Passa para o próximo número e continua o loop
