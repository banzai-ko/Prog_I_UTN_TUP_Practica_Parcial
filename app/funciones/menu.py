
from auxiliares import mostrar_menu, limpiar_pantalla
from validaciones import validar_opcion
from .funciones_app import (existencias, stock, menos_unidades, maximo_por_marca,
                            maxima_recaudacion, mas_50_mil_unidades, recaudacion_depositos,
                            unidades_por_marca)


def menu_principal(datos) -> None:
    while True:
        mostrar_menu()
        entrada = validar_opcion(1, 9)
        match entrada:
            case 1:
                existencias(datos)
            case 2:
                stock(datos)
            case 3:
                menos_unidades(datos)
            case 4:
                maximo_por_marca(datos)
            case 5:
                maxima_recaudacion(datos)
            case 6:
                mas_50_mil_unidades(datos)
            case 7:
                unidades_por_marca(datos)
            case 8:
                recaudacion_depositos(datos)
            case 9:
                print("Cerrando programa...")
                break
            case _:
                print("Opción incorrecta")

    limpiar_pantalla()
