from auxiliares import mostrar_menu, limpiar_pantalla, mostrar_matriz
from validaciones import validar_opcion
from dataset import crear_dataset


def menu_principal(datos) -> None:
  while True:
    mostrar_menu()
    entrada = validar_opcion(1, 9)
    match entrada:
      case 1:
        print("Matriz")
        mostrar_matriz(datos)
      case 2:
        pass
      case 3:
        pass
      case 4:
        pass
      case 5:
        pass
      case 6:
        pass
      case 7:
        pass
      case 8:
        pass
      case 9:
        print("Cerrando programa...")
        break 
      case _:
        print("Opción incorrecta")

  limpiar_pantalla()