from auxiliares import (
    mostrar_menu,
    mostrar_stock,
    mostrar_matriz,
    sumar_existencias,
    limpiar_pantalla,
    recaudacion,
    mostrar_recaudacion,
    min_stock,
    max_stock
)
from validaciones import validar_opcion


def menu_principal(datos) -> None:
    while True:
        mostrar_menu()
        entrada = validar_opcion(1, 9)
        match entrada:
            case 1:
                print("Matriz")
                mostrar_matriz(datos)
            case 2:
                # 2. Calcular por cada depósito la cantidad total de unidades almacenadas entre todos los smartphones.
                mensaje = " \n 2. Total de existencias por marca"
                print(mensaje)
                stock = sumar_existencias(datos)
                mostrar_stock(stock)
            case 3:
                # 3. Smartphone con menos unidades en cada depósito
                mensaje = " \n 3. Smartphone con menos existencias"
                print(mensaje)
                menor = min_stock(datos)
                mostrar_matriz(datos, True, menor)
                pass
            case 4:
              # 4. Máxima cantidad de cada smartphone
                mensaje = " \n 4. Cantidad maxima por marca"
                print(mensaje)
                maximo = max_stock(datos)
                mostrar_matriz(maximo)
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                # 8. Informe de recaudación por depósito
                mensaje = " \n 8. Total de recaudacion por depósito"
                print(mensaje)
                total = recaudacion(datos)
                mostrar_recaudacion(total)
            case 9:
                print("Cerrando programa...")
                break
            case _:
                print("Opción incorrecta")

    limpiar_pantalla()
