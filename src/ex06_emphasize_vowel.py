"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """
    Convierte a mayúscula todas las apariciones de vowel en la frase.
    Sugerencia:
    - Comprueba que vowel es un solo carácter y está en "aeiou" (en minúscula).
    - Recorre la frase carácter a carácter y construye una nueva cadena.
    """
    # TODO: validar y transformar
    if len(vowel) != 1 or vowel.lower() not in "aeiou":
        raise ValueError("La vocal debe ser un solo carácter y estar en 'aeiou'")
    vowel_lower = vowel.lower()
    result = ""
    for char in phrase:
        if char.lower() == vowel_lower:
            result += char.upper()
        else:
            result += char
    return result
    raise NotImplementedError("Implementa emphasize_vowel(phrase, vowel)")