"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    price_str = price_str.replace(",", ".")
    partes = price_str.split(".")
    if len(partes) != 2:
        raise ValueError("El precio debe tener exactamente dos partes separadas por '.' o ','")
    euros_str, centimos_str = partes
    if not euros_str.isdigit() or not centimos_str.isdigit():
        raise ValueError("Tanto euros como céntimos deben ser numéricos")
    if len(centimos_str) != 2:
        raise ValueError("Los céntimos deben tener exactamente dos dígitos")
    euros = int(euros_str)
    centimos = int(centimos_str)
    return (euros, centimos)
    raise NotImplementedError("Implementa euros_cents(price_str)")