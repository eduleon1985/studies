# PT-BR: Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total de segundos.
# EN: Write a program that reads the number of days, hours, minutes, and seconds from the user. Calculate the total number of seconds.

# 1 day = 86400 (24 hours x 60 minutes x 60 seconds)
# 1 hour = 3600 (60 minutes x 60 seconds)
# 1 minute = 60 (60 seconds)

days = int(input("Enter the number of DAYS you want to convert to seconds: "))
hours = int(input("Enter the number of HOURS you want to convert to seconds: "))
minutes = int(input("Enter the number of MINUTES you want to convert to seconds: "))
seconds = int(input("Enter the number of SECONDS you want to add to the total: "))

total = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
print(f"The entered days ({days}), hours ({hours}), minutes ({minutes}) and seconds ({seconds}) correspond to {total} seconds")