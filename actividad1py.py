var_numeroInt = int(input('ingrese la cantidad de numeros que desea evaluar'))
contador = 0

for i in range(var_numeroInt):
    num = float(input(f"ingrese el numero {i + 1}: "))
    if num >= 10 and num <=20:
        contador += 1

print(f'la cantidad de numeros en el rango de 10 a 20 es: {contador}')
