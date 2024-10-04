from screen import menu_text


def mostrar_menu() -> None:
    """ 
    Mostrar el menu por pantalla
    """
    print(menu_text)


def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def mostrar_matriz(dataset):
    """Muestra la matriz de forma tabular.

    Args:
        dataset: La matriz a mostrar.
    """

    encabezados = ["Deposito", "Marca", 'Modelo', "Precio", "Cantidad"]
    print("-" * (len(encabezados) * 12 + 2))
    print("|", end="")
    for encabezado in encabezados:
        print(f"{encabezado:^12}|", end="")
    print()
    print("-" * (len(encabezados) * 12 + 3))
    for fila in dataset:
        print("|", end="")
        for elemento in fila:
            print(f"{elemento:^12}|", end="")
        print()
    print("-" * (len(encabezados) * 12 + 3))