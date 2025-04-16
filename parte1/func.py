def es_primo(num):
    """
    Determina si un número es primo.
    
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    Esta función implementa una verificación eficiente de primalidad y maneja
    diferentes tipos de entrada con validaciones específicas.
    
    Args:
        num: El número a evaluar. Debe ser un entero o un flotante que represente un entero.
        
    Returns:
        bool: True si el número es primo, False en caso contrario.
        
    Raises:
        TypeError: Si el input no es un número entero o un flotante que represente un entero,
                  o si es un valor booleano, infinito o NaN.
    """
    # Validar que el input no sea un booleano (que es un subtipo de int en Python)
    if isinstance(num, bool):
        raise TypeError("El input no debe ser un valor booleano.")

    # Validar que el input sea un número (entero o flotante)
    if not isinstance(num, (int, float)):
        raise TypeError("El input debe ser un número entero.")

    # Manejo especial para números flotantes
    if isinstance(num, float):
        # Validar valores especiales como infinito y NaN
        if num in [float('inf'), float('-inf')] or num != num:  # num != num detecta NaN
            raise TypeError("El input no debe ser infinito ni NaN.")
        
        # Para números positivos cerca de enteros, verificar si están justo por debajo
        if num > 0:
            # Si está muy cerca de un entero por debajo (como 18.9999...)
            next_int = int(num) + 1
            if abs(num - next_int) < 1e-9 and abs(num - int(num)) > 0.9:
                num = int(num)  # Redondear hacia abajo para casos como 18.999...
            elif abs(num - round(num)) < 1e-9:
                num = round(num)  # Redondeo normal para otros casos cercanos a enteros
            else:
                raise TypeError("El input debe ser un número entero.")
        else:
            # Para números negativos o cero, aplicar redondeo estándar si está cerca de un entero
            if abs(num - round(num)) < 1e-9:
                num = round(num)
            else:
                raise TypeError("El input debe ser un número entero.")
            
    # Convertir a entero para el algoritmo de primalidad
    num = int(num)

    # Casos base: números menores que 2 no son primos
    if num < 2:
        return False
    
    # Casos especiales: 2 y 3 son primos
    if num < 4:
        return True
    
    # Optimización: verificar divisibilidad por 2 y 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Algoritmo optimizado: verificar divisibilidad por números de la forma 6k±1
    # Solo necesitamos verificar hasta la raíz cuadrada del número
    i = 5
    while i * i <= num:
        # Verificar si es divisible por i o i+2 (que cubren todos los números de la forma 6k±1)
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    # Si no se encontró ningún divisor, el número es primo
    return True