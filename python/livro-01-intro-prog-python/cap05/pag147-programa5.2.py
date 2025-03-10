### PT-BR (🇧🇷): 
# Tabuada com repetições aninhadas

### EN (🇺🇸):
# Multiplication table with nested loops

tabuada = 1

while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f"{tabuada} x {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1