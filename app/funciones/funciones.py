from auxiliares import mostrar_menu
from validaciones import validar_opcion


def menu_principal() -> None:
  mostrar_menu()
  entrada = validar_opcion(1, 9)
  
  while True:
    match entrada:
      case 1:
        pass
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