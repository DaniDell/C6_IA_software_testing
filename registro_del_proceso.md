# Registro del Proceso de Resolución del Challenge CAP06

Este documento detalla los pasos realizados para resolver el ejercicio del challenge CAP06, con la ayuda de un asistente de inteligencia artificial.

---

## **Resumen Ejecutivo**

Este proyecto aborda el desarrollo y prueba de una función llamada `es_primo`, diseñada para determinar si un número es primo. A lo largo del proceso, se implementaron soluciones para manejar casos límite, optimizar el rendimiento y garantizar la robustez mediante pruebas unitarias exhaustivas.

**Resultados clave:**
- La función `es_primo` cumple con todos los requisitos del challenge.
- Todas las pruebas unitarias y de referencia pasaron exitosamente.
- Se documentó el proceso de desarrollo para futuras referencias y aprendizaje.

---

## **1. Inicio del Proyecto**

- **Objetivo:** Implementar y probar una función llamada `es_primo` que determine si un número es primo.
- **Requisitos iniciales:**
  - Manejar números enteros positivos, negativos y flotantes.
  - Optimizar la función para manejar números grandes.

---

## **2. Implementación Inicial**

1. **Creación de la función `es_primo`:**
   - Se implementó una versión básica de la función que verificaba si un número entero era primo.
   - Se añadieron validaciones iniciales para manejar entradas no válidas.

2. **Pruebas iniciales:**
   - Se escribieron pruebas unitarias en `func_test.py` para validar la funcionalidad básica.
   - Se ejecutaron las pruebas con `pytest`, y algunos casos fallaron debido a entradas flotantes y números negativos.

---

## **3. Manejo de Entradas Flotantes**

1. **Problema identificado:**
   - Los números flotantes cercanos a enteros, como `19.000000000000004`, no eran manejados correctamente.
   - Números como `18.999999999999996` eran redondeados incorrectamente.

2. **Solución propuesta:**
   - Se creó una función auxiliar llamada `validar_y_convertir_a_entero` para manejar flotantes.
   - Esta función:
     - Validaba si el número flotante estaba dentro de un margen de error (`1e-9`) de un entero.
     - Redondeaba y convertía a entero si era válido.
     - Lanzaba un `TypeError` si no era válido.

3. **Resultados:**
   - Se corrigieron los errores relacionados con flotantes.
   - Las pruebas para casos como `19.000000000000004` y `18.999999999999996` pasaron correctamente.

---

## **4. Optimización de la Función**

1. **Optimización del algoritmo:**
   - Se implementó un algoritmo eficiente para verificar divisores hasta la raíz cuadrada del número.
   - Se utilizó la forma `6k ± 1` para reducir el número de divisiones necesarias.

2. **Resultados:**
   - La función ahora maneja números grandes como `10**10 + 19` de manera eficiente.

---

## **5. Casos de Prueba Cubiertos**

1. **Números primos conocidos:**
   - Ejemplos: `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31`.
   - Resultado esperado: `True`.

2. **Números no primos conocidos:**
   - Ejemplos: `0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20`.
   - Resultado esperado: `False`.

3. **Números negativos:**
   - Ejemplos: `-1, -2, -3, -5, -11, -13`.
   - Resultado esperado: `False`.

4. **Números flotantes cercanos a enteros:**
   - Ejemplos: `19.000000000000004` (primo), `18.999999999999996` (no primo).
   - Resultado esperado: `True` o `False` según el caso.

5. **Entradas no válidas:**
   - Ejemplos: `"string"`, `None`, `[2, 3]`, `float('inf')`, `float('nan')`.
   - Resultado esperado: `TypeError`.

6. **Números grandes:**
   - Ejemplos: `10**10 + 19` (primo), `10**10` (no primo).
   - Resultado esperado: `True` o `False` según el caso.

---

## **6. Desafíos Encontrados**

1. **Manejo de números flotantes cercanos a enteros:**
   - **Problema:** Los números como `18.999999999999996` se redondeaban incorrectamente.
   - **Solución:** Implementar una función auxiliar que valide y redondee números flotantes solo si están dentro de un margen de error (`1e-9`).

2. **Optimización para números grandes:**
   - **Problema:** La función inicial era ineficiente para números grandes.
   - **Solución:** Usar un algoritmo basado en divisores hasta la raíz cuadrada y la forma `6k ± 1`.

3. **Errores en pruebas unitarias:**
   - **Problema:** Las pruebas fallaban para entradas como `float('inf')` y `float('nan')`.
   - **Solución:** Agregar validaciones específicas para estos casos en la función `es_primo`.

4. **Configuración del entorno:**
   - **Problema:** Dificultades para activar el entorno virtual en Git Bash.
   - **Solución:** Usar el comando `source "venv/Scripts/activate"` para activarlo correctamente.

---

## **7. Organización del Proyecto**

1. **Estructura de carpetas:**
   - Se organizó el proyecto en la carpeta `parte1/` con los siguientes archivos:
     - `func.py`: Implementación de la función `es_primo`.
     - `func_test.py`: Pruebas unitarias para `es_primo`.
     - `reference_test.py`: Pruebas de referencia proporcionadas por el challenge.
     - `solucion/`: Carpeta con una solución alternativa y sus pruebas.

2. **Archivos adicionales:**
   - Se creó un archivo `.gitignore` para ignorar archivos innecesarios como `__pycache__` y `.pytest_cache`.
   - Se añadió un archivo `README.md` para documentar el proyecto.

---

## **8. Próximos Pasos**

1. **Ampliar los casos de prueba:**
   - Probar números extremadamente grandes para evaluar los límites de rendimiento.
   - Incluir más casos límite para entradas no válidas.

2. **Automatización de pruebas:**
   - Configurar un pipeline de integración continua (CI) con GitHub Actions para ejecutar las pruebas automáticamente en cada commit.

3. **Documentación adicional:**
   - Crear un tutorial paso a paso para que otros desarrolladores puedan entender y usar la función `es_primo`.

4. **Exploración de optimizaciones adicionales:**
   - Investigar algoritmos más avanzados para verificar la primalidad de números extremadamente grandes.

---

## **9. Agradecimientos**

Agradezco la asistencia proporcionada por herramientas de inteligencia artificial, como Sourcegraph Cody y GitHub Copilot, que facilitaron la resolución de problemas técnicos y la optimización del código. También agradezco a los instructores del curso por proporcionar un desafío tan interesante.

---

## **10. Referencias**

1. [Documentación oficial de Python](https://docs.python.org/3/)
2. [Algoritmos para verificar números primos](https://en.wikipedia.org/wiki/Primality_test)
3. [Guía de pytest](https://docs.pytest.org/en/latest/)