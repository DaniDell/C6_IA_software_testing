# Reporte de Reflexión

## **Desafíos Encontrados**

1. **Manejo de números flotantes cercanos a enteros:**
   - **Problema:** Los números como `18.999999999999996` y `19.000000000000004` no eran manejados correctamente debido a imprecisiones en la representación de números flotantes en Python.
   - **Solución:** Implementé una función auxiliar que valida si un número flotante está dentro de un margen de error (`1e-9`) de un entero. Esto permitió redondear correctamente los números válidos y lanzar errores para los no válidos.

2. **Optimización para números grandes:**
   - **Problema:** La función inicial era ineficiente para números grandes, ya que verificaba divisores hasta el número mismo.
   - **Solución:** Usé un algoritmo optimizado que verifica divisores hasta la raíz cuadrada del número y utiliza la forma `6k ± 1` para reducir el número de divisiones necesarias.

3. **Errores en pruebas unitarias:**
   - **Problema:** Las pruebas fallaban para entradas como `float('inf')` y `float('nan')`.
   - **Solución:** Agregué validaciones específicas en la función `es_primo` para manejar estos casos y lanzar un `TypeError`.

4. **Configuración del entorno:**
   - **Problema:** Dificultades para activar el entorno virtual en Git Bash.
   - **Solución:** Usé el comando `source "venv/Scripts/activate"` para activarlo correctamente.

---

## **Lecciones Aprendidas**

1. **Importancia del testing:**
   - Escribir pruebas unitarias me ayudó a identificar errores en la lógica de la función y a manejar casos límite que no había considerado inicialmente.
   - Las pruebas también me permitieron refactorizar el código con confianza, sabiendo que los cambios no romperían la funcionalidad existente.

2. **Manejo de números flotantes:**
   - Aprendí sobre las imprecisiones en la representación de números flotantes en Python y cómo usar márgenes de error para manejarlas correctamente.

3. **Optimización de algoritmos:**
   - Implementar un algoritmo eficiente para verificar números primos me enseñó la importancia de considerar el rendimiento, especialmente para entradas grandes.

4. **Organización del proyecto:**
   - Aprendí a estructurar un proyecto de manera modular, separando la lógica principal de las pruebas y documentando cada paso del proceso.

---

# Reporte de Reflexión

## **Conclusión**

Este ejercicio me permitió comprender la importancia del testing optimizado con IA en el desarrollo de software. Las pruebas no solo garantizan que el código funcione correctamente, sino que también ayudan a identificar errores, manejar casos límite y mejorar la calidad del software. Además, aprendí a usar herramientas como `pytest` y `pytest-cov` para automatizar y medir la cobertura de las pruebas, lo que es esencial en proyectos reales.

Usé Cody con el modelo Claude 3.7 y GitHub Copilot con el modelo GPT-4o en conjunto:

[Captura Visual estudio Code con ambos chats IA abiertos](imagenes/Captura_de_pantalla_2025-04-16_130016.png)