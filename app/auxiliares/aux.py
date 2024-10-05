
import os
from screen import menu_text


def mostrar_menu() -> None:
    """
    Mostrar el menu por pantalla
    """
    print(menu_text)


def limpiar_pantalla() -> None:
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')


def print_separator(separator: str, width: int) -> None:
    """Imprime una línea separadora.
    """
    print(separator * width)


def mostrar_matriz(dataset: list[list], mostrar_uno=False, indice=0) -> None:
    """Muestra la matriz de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """

    if mostrar_uno:
        mostrar_dataset = [dataset[indice]]
    else:
        mostrar_dataset = dataset

    encabezados = ["Deposito", "Marca", 'Modelo', "Precio", "Cantidad"]
    widht = len(encabezados) * 12 + 6
    print_separator('-', widht)
    print("|", end="")
    for encabezado in encabezados:
        print(f"{encabezado:^12}|", end="")
    print()
    print_separator('-', widht)
    for fila in mostrar_dataset:
        print("|", end="")
        for elemento in fila:
            print(f"{elemento:^12}|", end="")
        print()
    print_separator('-', widht)


def sumar_existencias(dataset: list[list]) -> list:
    """Suma las existencias de cada marca.

    Args:
        dataset: La matriz de datos.
    """
    xiaomi_stock = 0
    nubia_stock = 0
    infinix_stock = 0
    samsung_stock = 0

    for i in range(len(dataset)):
        marca = dataset[i][1]
        stock = int(dataset[i][4])

        if marca == "Xiaomi":
            xiaomi_stock += stock
        if marca == "Nubia":
            nubia_stock += stock
        elif marca == "Infinix":
            infinix_stock += stock
        elif marca == "Samsung":
            samsung_stock += stock

    existencias = [xiaomi_stock, nubia_stock,
                    infinix_stock, samsung_stock]

    return existencias


def print_separator(separator: str, width: int) -> None:
    """Imprime una línea separadora.
    """
    print(separator * width)


def mostrar_stock(stock: list) -> None:
    """Muestra la stock de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """

    encabezados = ["Xiaomi", "Nubia", 'Infinix', "Samsung"]
    widht = len(encabezados) * 12 + 5
    print_separator('-', widht)
    print("|", end="")
    for encabezado in encabezados:
        print(f"{encabezado:^12}|", end="")
    print()
    print_separator('-', widht)
    print("|", end="")
    for elem in stock:
        print(f"{elem:^12}|", end="")
    print()
    print_separator('-', widht)


def recaudacion(dataset: list[list]) -> list:
    """Calcula la recaudación por deposito.
    """

    recaudacion = []

    for i in range(len(dataset)):
        recaudacion.append(dataset[i][3] * dataset[i][4])

    return recaudacion


def mostrar_recaudacion(recaudacion: list) -> None:
    """Muestra la recaudación de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """

    encabezados = ["Deposito", "Recaudación"]
    widht = len(encabezados) * 16 + 3
    print_separator('-', widht)
    print("|", end="")
    for encabezado in encabezados:
        print(f"{encabezado:^16}|", end="")
    print()
    print_separator('-', widht)
    for i in range(len(recaudacion)):
        print("|", end="")
        print(f"{i+1:^16}|", end="")
        print(f"{recaudacion[i]:^16.2f}|", end="")
        print()
    print_separator('-', widht)


def min_stock(dataset: list[list]) -> list:
    """Calcula el smartphone con menos stock.

    Args:
        dataset: La matriz de datos.
    """
    first_run = True

    for i in range(len(dataset)):
        stock = dataset[i][4]

        if first_run or stock < min_stock:
            min_stock = stock
            min_stock_index = i
            first_run = False

    return min_stock_index


def max_stock(dataset: list[list], brand: str) -> list:
    """Devuelve el depósito con mayor stock por marca.

    Args:
        dataset: La matriz de datos.
        brand: La marca del smartphone.
    Returns:  
      Indice del deposito con mayor stock de esa marca.

    """
            
    first_run = True

    for i in range(len(dataset)):
        stock = dataset[i][4]
        marca = dataset[i][1]
        if marca == brand:
            if first_run or stock > max_stock:
                max_stock = stock
                max_stock_index = i
                first_run = False

    return max_stock_index
def depositos_max_stock(dataset: list[list]) -> list:
    """Devuelve una lista con los depositos con mayor stock por marca.

    Args:
        dataset: La matriz de datos.
    Returns:  
      Lista de depositos con mayor stock de cada marca.

    """
    lista_res = [(
        max_stock(dataset, 'Xiaomi'),
        max_stock(dataset, 'Nubia'),
        max_stock(dataset, 'Infinix'),max_stock(dataset, 'Samsung'))]
    
    return lista_res