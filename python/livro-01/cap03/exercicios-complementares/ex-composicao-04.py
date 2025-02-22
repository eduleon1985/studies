# 4 -  Conversão de temperatura | Temperature Conversion
# 📌 Português:
# Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit usando a fórmula:
# F = (C × 9/5) + 32
# "[C]°C equivale a [F]°F."

# 📌 English:
# Ask the user for a temperature in Celsius and convert it to Fahrenheit using the formula:
# "[C]°C is equivalent to [F]°F."

temperatura = 33
temp_f = temperatura * 9 / 5 + 32
msg = f"{temperatura}ºC equivale a {temp_f}ºF"
msg2 = f"{temperatura}ºC is equivalent to {temp_f}ºF"
print(msg)
print(msg2)