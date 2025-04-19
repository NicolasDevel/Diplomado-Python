'''Enteros int'''
'''
    Un entero es un tipo de dato que representa un número sin decimales.
    Puede ser positivo, negativo o cero.

    En Python, los enteros tienen precisión arbitraria, lo que significa que
    pueden representar valores muy grandes sin limitaciones de tamaño.
'''

# Ejemplo de valores enteros
numero_positivo = 42
numero_negativo = -15
cero = 0

# Operaciones básicas con enteros
suma = 5 + 3  # Resultado: 8
resta = 10 - 7  # Resultado: 3
producto = 4 * 6  # Resultado: 24
division_entera = 10 // 3  # Resultado: 3


'''Flotatentes float'''
'''
    Un flotante es un tipo de dato que representa un número real, es decir,
    un número que tiene una parte decimal.

    En Python, los flotantes tienen una precisión de aproximadamente 15 dígitos decimales.
'''

# Ejemplo de valores flotantes
pi = 3.14159
numero_negativo = -0.5
notacion_cientifica = 1.23e4  # Equivale a 12300.0

# Operaciones básicas con flotantes
division = 7 / 2  # Resultado: 3.5
potencia = 2 ** 3.5  # Resultado: 11.313708498984761


'''Cadenas de texto str'''

'''
    Una cadena de texto es una secuencia de caracteres que se utiliza para representar texto.
    Las cadenas en Python son inmutables, lo que significa que no se pueden modificar una vez creadas.

    Las cadenas pueden definirse usando comillas simples, dobles o triples.
'''

# Ejemplo de cadenas
texto_simple = 'Hola'
texto_doble = "Mundo"
texto_multilinea = """Esto es
un texto en varias líneas"""

# Operaciones básicas con cadenas
concatenacion = "Hola" + " " + "Mundo"  # Resultado: 'Hola Mundo'
repeticion = "Ja" * 3  # Resultado: 'JaJaJa'

# Acceso a caracteres por índice
primera_letra = texto_simple[0]  # Resultado: 'H'
ultima_letra = texto_simple[-1]  # Resultado: 'a'


'''Flotatentes'''
'''
    Un booleano es un tipo de dato que representa uno de dos valores posibles: True o False.
    Se utiliza principalmente para evaluar expresiones lógicas y condicionales.
'''

# Ejemplo de valores booleanos
verdadero = True
falso = False

# Operaciones con booleanos
es_mayor = 5 > 3  # Resultado: True
es_igual = 10 == 10  # Resultado: True
es_diferente = 7 != 8  # Resultado: True

# Uso en condicionales
if verdadero:
    print("Es verdadero")
else:
    print("Es falso")
