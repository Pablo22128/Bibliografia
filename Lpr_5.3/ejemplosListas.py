# ============================================================
#   METODOS DE LISTAS EN PYTHON
#   Ejemplos practicos para repasar cada metodo
# ============================================================
#
#   Ejecutar con:  python metodos_listas.py
#   Cada bloque muestra la lista ANTES y DESPUES de usar el metodo.
# ============================================================


print("=" * 50)
print("1) append(x) - agrega un elemento al final")
print("=" * 50)
frutas = ['manzana', 'pera']
print("Antes: ", frutas)
frutas.append('banana')
print("Despues:", frutas)      # ['manzana', 'pera', 'banana']


print("\n" + "=" * 50)
print("2) extend(iter) - agrega varios elementos al final")
print("=" * 50)
numeros = [1, 2, 3]
print("Antes: ", numeros)
numeros.extend([4, 5, 6])
print("Despues:", numeros)     # [1, 2, 3, 4, 5, 6]
# OJO: append([4,5]) metria la lista entera como UN solo elemento.
#      extend la "abre" y agrega sus elementos uno por uno.


print("\n" + "=" * 50)
print("3) insert(i, x) - inserta en la posicion i")
print("=" * 50)
colores = ['rojo', 'verde', 'azul']
print("Antes: ", colores)
colores.insert(1, 'amarillo')
print("Despues:", colores)     # ['rojo', 'amarillo', 'verde', 'azul']


print("\n" + "=" * 50)
print("4) remove(x) - elimina la primera ocurrencia de x")
print("=" * 50)
numeros = [1, 2, 3, 2, 4]
print("Antes: ", numeros)
numeros.remove(2)
print("Despues:", numeros)     # [1, 3, 2, 4]  (solo el primer 2)


print("\n" + "=" * 50)
print("5) pop([i]) - elimina Y DEVUELVE el elemento en la posicion i")
print("=" * 50)
letras = ['a', 'b', 'c']
print("Antes:   ", letras)
sacada = letras.pop(1)
print("Devuelve: ", sacada)    # 'b'
print("Despues: ", letras)     # ['a', 'c']
# Sin indice, saca y devuelve el ultimo:
ultimo = letras.pop()
print("pop() sin indice devuelve:", ultimo)   # 'c'


print("\n" + "=" * 50)
print("6) clear() - elimina todos los elementos")
print("=" * 50)
datos = [10, 20, 30]
print("Antes: ", datos)
datos.clear()
print("Despues:", datos)       # []


print("\n" + "=" * 50)
print("7) index(x) - indice de la primera aparicion de x")
print("=" * 50)
animales = ['gato', 'perro', 'loro']
print("Lista:", animales)
print("index('perro') =", animales.index('perro'))   # 1


print("\n" + "=" * 50)
print("8) count(x) - cuenta cuantas veces aparece x")
print("=" * 50)
numeros = [2, 5, 2, 8, 2]
print("Lista:", numeros)
print("count(2) =", numeros.count(2))   # 3


print("\n" + "=" * 50)
print("9) sort() - ordena la lista (ascendente)")
print("=" * 50)
numeros = [4, 1, 3, 2]
print("Antes:       ", numeros)
numeros.sort()
print("Ascendente:  ", numeros)         # [1, 2, 3, 4]
numeros.sort(reverse=True)
print("Descendente: ", numeros)         # [4, 3, 2, 1]


print("\n" + "=" * 50)
print("10) reverse() - invierte el orden")
print("=" * 50)
numeros = [1, 2, 3]
print("Antes: ", numeros)
numeros.reverse()
print("Despues:", numeros)     # [3, 2, 1]


print("\n" + "=" * 50)
print("11) copy() - devuelve una copia superficial")
print("=" * 50)
original = [1, 2, 3]
nueva = original.copy()
nueva.append(4)
print("original:", original)   # [1, 2, 3]  (no se modifico)
print("nueva:   ", nueva)      # [1, 2, 3, 4]
# Si hicieras  nueva = original  (sin .copy()), las dos apuntarian
# a la MISMA lista y cambiar una afectaria a la otra.