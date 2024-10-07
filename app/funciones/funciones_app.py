from auxiliares import (

    mostrar_stock,
    mostrar_matriz,
    sumar_existencias,
    recaudacion,
    mostrar_recaudacion,
    min_stock,
    depositos_max_stock,
    bubble_sort_indices,
    mayores_50_mil,
    calcular_stock_marca, obtener_mayor
)


def existencias(datos) -> None:
    # Mostrar Existecians
    print("Matriz")
    mostrar_matriz(datos)


def stock(datos) -> None:
    # 2. Calcular por cada depósito la cantidad total de unidades almacenadas entre todos los smartphones.
    mensaje = " \n 2. Total de existencias por marca"
    print(mensaje)
    stock = sumar_existencias(datos)
    mostrar_stock(stock)


def menos_unidades(dataset: list[list]) -> None:
    # 3. Smartphone con menos unidades en cada depósito
    mensaje = " \n 3. Smartphone con menos existencias"
    print(mensaje)
    menor = min_stock(dataset)
    mostrar_matriz(dataset, True, menor)


def maximo_por_marca(dataset: list[list]) -> None:
    # 4. Máxima cantidad de cada smartphone
    mensaje = " \n 4. Cantidad maxima por marca"
    print(mensaje)
    maximo = depositos_max_stock(dataset)
    mostrar_matriz(dataset, True, maximo[0])

    mostrar_matriz(dataset, True, maximo[1])

    mostrar_matriz(dataset, True, maximo[2])

    mostrar_matriz(dataset, True, maximo[3])


def maxima_recaudacion(dataset: list[list]) -> None:
    # 5. Deposito con maximo recaudación
    mensaje = " \n 5. Deposito con maxima recaudación"
    print(mensaje)
    rec = recaudacion(dataset)
    max_rec = bubble_sort_indices(rec)
    mostrar_matriz(dataset, True, max_rec[0])
    total = dataset[max_rec[0]][3] * dataset[max_rec[0]][4]
    print(f"Recaudación: {total}")


def mas_50_mil_unidades(dataset: list[list]) -> None:
   # 6. Cantidad de depósitos con más de 50,000 unidades
    mensaje = " \n 6. Cantidad de depósitos con más de 50,000 unidades: "
    result = mayores_50_mil(dataset)
    print(f"{mensaje} {len(result)}")
    mostrar_matriz(result)


def recaudacion_depositos(dataset: list[list]) -> None:
    # 8. Informe de recaudación por depósito
    mensaje = " \n 8. Total de recaudacion por depósito"
    print(mensaje)
    total = recaudacion(dataset)
    mostrar_recaudacion(total, dataset)


def unidades_por_marca(datos) -> None:
    # 7. Porcentaje de unidades por marca y marca con mayor porcentaje
    print(" \n7. Porcentaje de unidades por marca")
    xiaomi = calcular_stock_marca(datos, "Xiaomi")
    nubia = calcular_stock_marca(datos, "Nubia")
    infinix = calcular_stock_marca(datos, "Infinix")
    samsung = calcular_stock_marca(datos, "Samsung")
    total = xiaomi + nubia + infinix + samsung

    porcentaje_xiaomi = (xiaomi / total) * 100
    porcentaje_nubia = (nubia / total) * 100
    porcentaje_infinix = (infinix / total) * 100
    porcentaje_samsung = (samsung / total) * 100

    mensaje = f"Xiaomi: {porcentaje_xiaomi:.2f}%\n"
    mensaje += f"Nubia: {porcentaje_nubia:.2f}%\n"
    mensaje += f"Infinix: {porcentaje_infinix:.2f}%\n"
    mensaje += f"Samsung: {porcentaje_samsung:.2f}%\n"
    mayor = obtener_mayor(porcentaje_xiaomi, porcentaje_nubia,
                          porcentaje_infinix, porcentaje_samsung)
    mensaje += f" \nMarca con Mayor porcentaje: {mayor:.2f}%"
    print(mensaje)
