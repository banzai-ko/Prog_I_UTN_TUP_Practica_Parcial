def validar_opcion(num_min: int, num_max: int):
    """_summary_
Funcion para validar entrada del usuario
Debe ser numerica y este entre el minimo y el maximo
Argumentos:
num_min: Entero minimo
num_max: Entero maximo

Retorna: un entero con la entrada del usuario, 
"""
    opcion = input(f'Elija una opcion entre {num_min} y {num_max}: ')

    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)

    return int(opcion)