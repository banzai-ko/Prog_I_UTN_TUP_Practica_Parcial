import random


def asignar_modelo(marca: str) -> str:
    """
    Asigna un modelo aleatorio de la marca relacionada.
    """
    modelos_xiaomi = ["Redmi", "Pocophone", "Redmi Note", "Redmi 9"]
    modelos_nubia = ["Nubia", "Phobia", "Nubia 5G", "Nubia 4G"]
    modelos_infinix = ["Infi_X", "Hot 11",
                         "Hot 10", "Hot 9"]
    modelos_samsung = ["Samsung", "Galaxy", "S20", "S21"]
    match  marca:
        case "Xiaomi":
            modelo = random.choice(modelos_xiaomi)
        case "Nubia":
            modelo = random.choice(modelos_nubia)
        case "Infinix":
            modelo = random.choice(modelos_infinix)
        case "Samsung":
            modelo = random.choice(modelos_samsung)
    return modelo


def crear_dataset(filas: int) -> list[list]:
    """
    Crea un dataset de muestra con una matriz de n filas x  5 columnas(predefinidas) .
    Args:
        filas: Número de filas de la matriz.
        columnas: Número de columnas de la matriz.
    Returns:
        Una lista de listas, donde cada lista interna representa una fila.
    """

    dataset = []
    marcas = ["Xiaomi", "Nubia", "Infinix", "Samsung"]

    marca = random.choice(marcas)

    for i in range(filas):
        deposito = f"Deposito {i}"
        marca = random.choice(marcas)
        modelo = asignar_modelo(marca)
        precio = round(random.uniform(100, 400), 2)
        cantidad = random.randint(10000, 60000)
        elemento = [
            deposito,
            marca,
            modelo,
            precio,
            cantidad,
        ]
        dataset.append(elemento)
    return dataset
