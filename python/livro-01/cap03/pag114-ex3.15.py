# PT-BR (🇧🇷): 
# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro.
# Calcule quantos dias de vida um fumante perderá. Exiba o total em dias.


# EN (🇺🇸): 
# Write a program to calculate the reduction in a smoker's life expectancy.
# Ask for the number of cigarettes smoked per day and the number of years they have smoked.
# Consider that a smoker loses 10 minutes of life for each cigarette.
# Calculate how many days of life a smoker will lose. Display the total in days.

print(".............................................................")
cigarros = int(input("Quantos cigarros em média você fumou por dia? "))
periodo = float(input("Por quantos anos? "))

# Cigarros fumados: 365 dias * periodo (anos)
cigarros_consumidos = (cigarros * 365 * periodo)

# Minutos perdidos
minutos_perdidos = cigarros_consumidos * 10

# Convertendo para dias
# 1 dia tem 1440 minutos (24 * 60)
dias_perdidos = minutos_perdidos / 1440

print(f"Ao longo da vida, você fumou {cigarros_consumidos}")
print(f"Você perdeu {minutos_perdidos} minutos de vida, que corresponde a {dias_perdidos} dias perdidos")
