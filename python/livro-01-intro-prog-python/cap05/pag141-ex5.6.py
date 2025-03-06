x = int(input("Informe um valor para a tabuada: "))
inicio = int(input("A tabuada deve começar em: "))
fim = int(input("A tabuada deve terminar em: "))

while inicio <= fim:
    print(f"{inicio} x {x} = {inicio * x}")
    inicio = inicio + 1