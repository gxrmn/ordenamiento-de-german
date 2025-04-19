Método de Ordenamiento de Germán
Implementación del algoritmo de ordenamiento desarrollado por Carlos Germán González Pérez

Este repositorio contiene un algoritmo de ordenamiento diseñado por mí (Germán), que utiliza una lógica basada en comparaciones sucesivas para ir formando una nueva lista ordenada. No se basa en métodos clásicos como *QuickSort* o *Bubble Sort*, sino que implementa una estrategia propia.

---

## 📌 ¿Cómo funciona?

El algoritmo toma una lista de números aleatorios y la recorre comparando cada elemento con los siguientes. Según la relación de orden que encuentra, va agregando valores a una nueva lista (`resultado`) y eliminando los que ya están considerados.

Este proceso se repite **hasta que la lista resultante esté completamente ordenada**.

---

## 🧮 Código

```python
import time
import random

# Generar una lista de 10000 números aleatorios entre 1 y 100000
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

Autor:
Creado con curiosidad y pasión por Carlos Germán González Pérez
¡Gracias por visitar este experimento de lógica! 😊




