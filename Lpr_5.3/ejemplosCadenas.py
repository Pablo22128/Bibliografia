# Crear strings
saludo = "Hola"
nombre = 'Mundo'

# Concatenación simple
frase_completa = saludo + " " + nombre
print(frase_completa)  # Resultado: Hola Mundo

# Repetir cadenas con el operador *
risa = "Ja" * 3
print(risa)  # Resultado: JaJaJa

palabra = "Esternocleidomastoideo"

# Obtener el largo de la cadena
largo = len(palabra)
print(largo)  # Resultado: 22

# Verificar si un texto existe dentro de otro (operador 'in')
tiene_cleido = "cleido" in palabra
print(tiene_cleido)  # Resultado: True

tiene_python = "python" in palabra
print(tiene_python)  # Resultado: False



frase = "  Aprendiendo Python en 2026!  "

# Cambiar mayúsculas y minúsculas
print(frase.upper())       # "  APRENDIENDO PYTHON EN 2026!  "
print(frase.lower())       # "  aprendiendo python en 2026!  "
print(frase.capitalize())  # "  aprendiendo python en 2026!  " (Primera letra en mayúscula)

# Limpiar espacios en blanco a los lados
print(frase.strip())       # "Aprendiendo Python en 2026!"

# Reemplazar texto
print(frase.replace("2026", "hoy")) # "  Aprendiendo Python en hoy!  "

# Comprobar si empieza o termina con algo
print(frase.strip().startswith("A")) # True

# Convertir un string en una lista (Split)
datos = "manzana,banana,pera,uva"
lista_frutas = datos.split(",")
print(lista_frutas)  # Resultado: ['manzana', 'banana', 'pera', 'uva']

# Convertir una lista en un string (Join)
palabras = ["Python", "es", "genial"]
frase_unida = " ".join(palabras)
print(frase_unida)  # Resultado: Python es genial
