# PT-BR (🇧🇷): 
# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.


# EN (🇺🇸): 
# Write a program that asks for the user's car speed.
# If it exceeds 80 km/h, display a message informing that the user has been fined.
# In this case, show the fine amount, charging R$ 5 for each km above 80 km/h.

# Minha linha de raciocínio
# Perguntar a velocidade do carro do usuário
# Verificar se a velocidade for maior que 80
# Se sim, calcular quanto (velocidade - 80)
# Este número * R$ 5,00

print("===")

velocidade = int(input("Qual é a velocidade que você está dirigindo? "))

if velocidade > 80:
    excedente = velocidade - 80
    multa = excedente * 5
    print(f"Você estava dirigindo a {velocidade}km/h, e terá que pagar uma multa de R${multa}.")
else:
    print("Muito bem, não ultrapasse os 80km/h para não ser multado.")

print("===")