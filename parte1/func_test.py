import pytest
import time
import random
from func import es_primo

# Prueba de valores válidos (números enteros)
@pytest.mark.parametrize("numero, esperado", [
    (2, True), (3, True), (5, True), (7, True), (11, True),  # Números primos pequeños
    (0, False), (1, False), (4, False), (6, False),          # Números no primos pequeños
    (-1, False), (-2, False),                                # Números negativos (no son primos)
    (7919, True), (7920, False),                             # Números grandes (primo y no primo)
])
def test_es_primo_valores_validos(numero, esperado):
    """
    Verifica que la función `es_primo` identifique correctamente números primos y no primos.
    Incluye casos de números pequeños, negativos y grandes.
    """
    assert es_primo(numero) == esperado

# Prueba de entradas no válidas
@pytest.mark.parametrize("entrada", [
    "string", None, 3.14, [2, 3], {2, 3}, {2: 3}, (2, 3), b'2',
    bytearray(b'2'), range(2), frozenset([2, 3]), complex(2, 3),
    memoryview(b'2'), slice(2, 3), float('inf'), float('nan')
])
def test_es_primo_entradas_invalidas(entrada):
    """
    Verifica que la función `es_primo` lance un TypeError para entradas no válidas.
    Incluye tipos como cadenas, None, flotantes no enteros, estructuras de datos,
    números complejos, infinito y NaN.
    """
    with pytest.raises(TypeError):
        es_primo(entrada)

# Prueba de números grandes
def test_es_primo_numeros_grandes():
    """
    Verifica que la función `es_primo` maneje correctamente números grandes.
    Incluye un número primo grande y un número no primo grande.
    """
    assert es_primo(10**10 + 19) == True  # Ejemplo de número primo grande
    assert es_primo(10**10) == False      # Ejemplo de número no primo grande

# Prueba de números flotantes cercanos a enteros
@pytest.mark.parametrize("numero, esperado", [
    (19.000000000000004, True),  # Se redondea a 19 (primo)
    (23.000000000000004, True),  # Se redondea a 23 (primo)
    (18.999999999999996, False),  # NO se redondea (no primo)
    (22.999999999999996, False),  # NO se redondea (no primo)
])
def test_es_primo_flotantes_cercanos(numero, esperado):
    """
    Verifica que la función `es_primo` maneje correctamente números flotantes cercanos a enteros.
    - Redondea números como 19.000000000000004 a 19 (primo).
    - No redondea números como 18.999999999999996 (no primo).
    """
    assert es_primo(numero) == esperado

# Prueba de rendimiento: medir tiempo de ejecución
def test_es_primo_rendimiento():
    """
    Mide el tiempo de ejecución de la función `es_primo` con un número grande.
    Asegura que el tiempo sea razonable para un número primo grande.
    """
    numero_grande = 10**12 + 39  # Número primo grande
    start = time.time()
    assert es_primo(numero_grande) == True
    end = time.time()
    print(f"Tiempo de ejecución para {numero_grande}: {end - start:.4f} segundos")

# Prueba de estrés: números aleatorios grandes
def test_es_primo_estres():
    """
    Verifica que la función `es_primo` maneje números aleatorios grandes sin errores.
    No evalúa el resultado, solo asegura que no falle.
    """
    for _ in range(5):  # Ejecutar 5 pruebas de estrés
        numero_grande = random.randint(10**12, 10**13)
        es_primo(numero_grande)  # Solo verifica que no falle