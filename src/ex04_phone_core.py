"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    partes = s.strip().split("-")
    if len(partes) != 3:
        raise ValueError("El teléfono debe tener exactamente 3 partes separadas por '-'")
    if not partes[0].startswith("+"):
        raise ValueError("La primera parte debe comenzar por '+'")
    if not partes[1].isdigit():
        raise ValueError("La parte central debe ser numérica")
    return partes[1]
    
    raise NotImplementedError("Implementa phone_core(s)")