### PT-BR (🇧🇷): 
# Exemplo de dicionário com valor padrão

### EN (🇺🇸):
# Exemple of a dictionary with a default value

# O método "get" tenta obter a chave procurada.
# Caso não a encontre, retorna o segundo parâmetro, no caso, 0 (zero).
# Se o segundo parâmetro não for especificado, o "get" retornará None.
# Quando a chave é encontrada no dicionário, get retorna o valor atualmente associado.

d = {}

for letra in "abracadabra":
    d[letra] = d.get(letra, 0) + 1

print(d)