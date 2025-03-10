### PT-BR (🇧🇷): 
# Tabuada com repetições aninhadas

### EN (🇺🇸):
# Multiplication table with nested loops

while True:
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))

    if numero == 0:
        break
    
    multiplicador = 1 # começa a tabuada no número 1

    while multiplicador <= 10:
        print(f"{multiplicador} * {numero} = {multiplicador * numero}")
        multiplicador += 1

    print("=" * 30)