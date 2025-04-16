import pytest
from func import es_primo

@pytest.mark.parametrize("numero, esperado", [
    (2, True), (3, True), (5, True), (7, True), (11, True),  # Números primos
    (0, False), (1, False), (4, False), (6, False),          # Números no primos
    (-1, False), (-2, False),                                # Números negativos
    (7919, True), (7920, False),                             # Números grandes
])
def test_es_primo_valores_validos(numero, esperado):
    assert es_primo(numero) == esperado

@pytest.mark.parametrize("entrada", [
    "string", None, 3.14, [2, 3], {2, 3}, {2: 3}, (2, 3), b'2',
    bytearray(b'2'), range(2), frozenset([2, 3]), complex(2, 3),
    memoryview(b'2'), slice(2, 3), float('inf'), float('nan')
])
def test_es_primo_entradas_invalidas(entrada):
    with pytest.raises(TypeError):
        es_primo(entrada)

def test_es_primo_numeros_grandes():
    assert es_primo(10**10 + 19) == True  # Ejemplo de número primo grande
    assert es_primo(10**10) == False      # Ejemplo de número no primo grande

@pytest.mark.parametrize("numero, esperado", [
    (19.000000000000004, True),  # Se redondea a 19 (primo)
    (23.000000000000004, True),  # Se redondea a 23 (primo)
    (18.999999999999996, False),  # NO se redondea 
    (22.999999999999996, False),  # No se redondea 
])
def test_es_primo_flotantes_cercanos(numero, esperado):
    assert es_primo(numero) == esperado