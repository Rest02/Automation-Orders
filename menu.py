from prep_mario import Preparar_pedido
from pruebas import pruebas_imprimir_boleta
from datetime import datetime





menu = """
1. Preparar pedido
2. Pruebas de imprimir boleta
3. Salir
"""

while True:
    print(menu)
    opcion = str(input("Introduce la opción: "))
    if opcion == "1":
        numero_pedido = str(input("Introduce el número de pedido: "))
        Preparar_pedido(numero_pedido)
        print("Pedido preparado")
    elif opcion == "2":
        numero_pedido = str(input("Introduce el número de pedido: "))
        try:
            pruebas_imprimir_boleta(numero_pedido)
            print("Boleta impresa correctamente")
        except Exception as e:
            print(f"Ocurrió un error al intentar imprimir la boleta: {e}")
    elif opcion == "3":
        break
    else:
        print("Opción inválida")