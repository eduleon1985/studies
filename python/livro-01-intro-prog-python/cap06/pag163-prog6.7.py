### PT-BR (🇧🇷): 
# Tópico: Listas, Remoção de Elementos

### EN (🇺🇸):
# Topic: Lists, Element removal

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f"Existem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("F - Adiciona um cliente ao finm da fila")
    print("A - Atendimento do cliente, que sai da fila")
    print("S - Sair")
    operacao = str(input("F, A ou S: "))
    if operacao == "A" or operacao == "a":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido!")
        else:
            print("Fila vazia, ninguém pra atender!")
    elif operacao == "F" or operacao == "f":
        ultimo += 1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S" or operacao == "s":
        break
    else:
        print("Operação inválida. Digite apenas F, A ou S.")