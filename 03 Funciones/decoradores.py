# decoradores.py

# Un decorador es una función que toma otra función como argumento, la modifica y la devuelve.
# Es una forma de "envolver" la funcionalidad de una función sin modificar su código directamente.

# Ejemplo 1: Un decorador simple
def saludo(func):
    """
    Este decorador agrega un saludo antes de ejecutar la función.
    """
    def wrapper():
        print("¡Hola! Vamos a ejecutar la función.")
        func()
    return wrapper

# Aplicamos el decorador a la función original
@saludo
def decir_hola():
    """
    Función que imprime 'Hola Mundo'.
    """
    print("Hola Mundo!")

# Cuando llamamos a 'decir_hola()', primero se ejecutará el código del decorador,
# luego el código de la función original.
decir_hola()
# Salida:
# ¡Hola! Vamos a ejecutar la función.
# Hola Mundo!

# Ejemplo 2: Decorador con argumentos
def decorador_con_argumentos(func):
    """
    Este decorador toma una función con argumentos y modifica su comportamiento.
    """
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función con argumentos:", args, kwargs)
        result = func(*args, **kwargs)
        print("Después de llamar a la función")
        return result
    return wrapper

# Aplicamos el decorador a una función que recibe parámetros
@decorador_con_argumentos
def sumar(a, b):
    """
    Función que suma dos números.
    """
    return a + b

# Llamamos a la función decorada
resultado = sumar(3, 5)
print("Resultado:", resultado)
# Salida:
# Antes de llamar a la función con argumentos: (3, 5) {}
# Después de llamar a la función
# Resultado: 8

# Ejemplo 3: Decorador con valores de retorno
def decorador_de_retorno(func):
    """
    Este decorador modifica el valor de retorno de la función.
    """
    def wrapper(*args, **kwargs):
        print("Modificando el valor de retorno...")
        return "Valor modificado"
    return wrapper

# Aplicamos el decorador
@decorador_de_retorno
def obtener_dato():
    """
    Función que debería retornar un dato.
    """
    return "Dato original"

# Llamamos a la función decorada
resultado = obtener_dato()
print("Resultado:", resultado)
# Salida:
# Modificando el valor de retorno...
# Resultado: Valor modificado

# Ejemplo 4: Decorador con una función de paso (functools.wraps)
# Si quieres que el decorador conserve la metadata de la función original (como nombre y docstring),
# puedes usar 'functools.wraps' para hacerlo.

from functools import wraps

def decorador_con_wraps(func):
    """
    Este decorador usa wraps para conservar la metadata de la función original.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@decorador_con_wraps
def mi_funcion():
    """
    Esta función hace algo importante.
    """
    print("Función ejecutada.")

# Llamamos a la función decorada
mi_funcion()
print("Nombre de la función decorada:", mi_funcion.__name__)
# Salida:
# Llamando a la función: mi_funcion
# Función ejecutada.
# Nombre de la función decorada: mi_funcion
