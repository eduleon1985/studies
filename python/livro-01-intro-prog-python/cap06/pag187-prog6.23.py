### PT-BR (🇧🇷): 
# Exemplo de dicionário sem valor padrão

### EN (🇺🇸):
# Exemple of a dictionary without a default value

# Dicionário
d = {}

for letra in "abracadabra":
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1

print(d)