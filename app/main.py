"""
Una empresa se dedica al almacenamiento y posterior distribución de smartphones en el país.
Para ello cuentan con 20 depósitos en Berazategui, que generalmente se encuentran en las
inmediaciones de las estaciones del ferrocarril.

Los depósitos pueden almacenar 4 marcas diferentes de smartphones: Xiaomi, Nubia, Infinix y
Samsung. La oficina central recibe mensualmente una planilla de existencias donde se indican
las existencias de cada smartphone para cada depósito.

Menú de opciones a implementar:

1. Obtener existencias: Crear una función que cargue la existencia de cada smartphone en
   todos los depósitos.
2. Calcular por cada depósito la cantidad total de unidades almacenadas entre todos los
   smartphones.
3. Mostrar el nombre del smartphone que almacenó menos unidades en cada depósito.
4. Determinar la máxima cantidad de unidades almacenadas de cada smartphone.
5. Identificar el depósito con mayor recaudación, teniendo en cuenta un vector con los valores
   por unidad de cada marca de smartphone.
6. Determinar la cantidad de depósitos que hayan almacenado más de 50,000 unidades entre
   los 4 smartphones.
7. Calcular el porcentaje de unidades de cada smartphone sobre el total de unidades almacenadas,
   y mostrar la marca con el máximo porcentaje.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
"""
from funciones import menu_principal
from dataset import crear_dataset
datos = crear_dataset(20)

"""
    _summary_ Entrada al programa
    Main principal
    """
if __name__ == "__main__":

    menu_principal(datos)
