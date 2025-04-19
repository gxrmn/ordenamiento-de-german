import time
import random

# Generar una lista de 500 números aleatorios entre 1 y 1000
lista = [random.randint(1, 100000) for _ in range(10000)]
resultado = []

# ⏱ Iniciar tiempo
inicio = time.time()

# Repite hasta que la lista esté completamente ordenada
while True:
    resultado = []
    i = 0
    while i < len(lista):
        actual = lista[i]
        se_añadió = False

        for j in range(i + 1, len(lista)):
            if actual < lista[j]:
                resultado.append(actual)
                lista.pop(i)
                se_añadió = True
                break
            elif actual > lista[j]:
                resultado.append(lista[j])
                lista.pop(j)
                se_añadió = True
                break

        if not se_añadió:
            resultado.append(actual)
            lista.pop(i)

    if resultado == sorted(resultado):
        break
    else:
        lista = resultado.copy()

# ⏱ Fin del tiempo
fin = time.time()

# Resultado final
print("Lista ordenada con el método de Germán:")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
