temp = float(input("Ingrese la temperatura (°C): "))

if temp < 10:
    print("Clasificación: Frío.")
elif temp < 25:
    print("Clasificación: Templado.")
elif temp < 35:
    print("Clasificación: Caluroso.")
else:
    print("Clasificación: Muy caluroso.")