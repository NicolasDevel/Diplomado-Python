# entrada_salida.py
# Este script demuestra cómo manejar la entrada y salida de datos en Python.

# Entrada de datos
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
es_estudiante = input("¿Eres estudiante? (sí/no): ").lower() == "sí"

# Salida de datos
print("\nInformación ingresada:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"¿Es estudiante?: {'Sí' if es_estudiante else 'No'}")

# Ejemplo de procesamiento de entrada
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 25 and es_estudiante:
    print("Estás en la edad típica de ser universitario.")
else:
    print("Eres mayor de edad y tienes experiencias distintas.")
