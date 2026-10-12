"""Práctica de arreglos y vectores: control básico de inventario."""

# Ambos arreglos utilizan el mismo índice para identificar un producto.
productos = ["Arroz", "Aceite", "Azucar", "Leche", "Cafe"]
cantidades = [12, 7, 4, 9, 3]


def mostrar_inventario():
    """Recorre los vectores y señala los productos con pocas unidades."""
    print("\nINVENTARIO ACTUAL")
    for indice in range(len(productos)):
        aviso = "Stock bajo" if cantidades[indice] < 5 else "Disponible"
        print(f"{indice}. {productos[indice]}: {cantidades[indice]} unidades - {aviso}")


def consultar_producto():
    """Obtiene el producto correspondiente a un índice."""
    try:
        indice = int(input("Indica el indice del producto (0 al 4): "))
    except ValueError:
        print("Debes escribir un numero entero.")
        return

    if 0 <= indice < len(productos):
        print(f"{productos[indice]} tiene {cantidades[indice]} unidades.")
    else:
        print("Ese indice no existe en el inventario.")


def modificar_cantidad():
    """Permite actualizar una posición del vector de existencias."""
    try:
        indice = int(input("Indice del producto que deseas modificar: "))
        if indice < 0 or indice >= len(productos):
            print("Ese indice no existe en el inventario.")
            return
        nueva_cantidad = int(input("Nueva cantidad disponible: "))
    except ValueError:
        print("Debes escribir numeros enteros.")
        return

    if nueva_cantidad < 0:
        print("La cantidad no puede ser negativa.")
        return

    cantidades[indice] = nueva_cantidad
    print(f"Cantidad de {productos[indice]} actualizada a {nueva_cantidad}.")


def calcular_resumen():
    """Suma las unidades y cuenta los artículos cuyo stock es bajo."""
    total_unidades = 0
    productos_bajos = 0
    for cantidad in cantidades:
        total_unidades += cantidad
        if cantidad < 5:
            productos_bajos += 1
    print(f"Total de unidades disponibles: {total_unidades}")
    print(f"Productos con stock bajo: {productos_bajos}")


def buscar_producto():
    """Localiza un producto por su nombre mediante un recorrido."""
    nombre = input("Nombre del producto que deseas buscar: ").strip().lower()
    for indice in range(len(productos)):
        if productos[indice].lower() == nombre:
            print(f"Encontrado: {productos[indice]} - {cantidades[indice]} unidades.")
            return
    print("Producto no encontrado.")


def menu():
    """Repite las opciones hasta que el usuario selecciona salir."""
    while True:
        print("\n--- CONTROL DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Consultar por indice")
        print("3. Modificar cantidad")
        print("4. Calcular resumen")
        print("5. Buscar por nombre")
        print("6. Salir")
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            modificar_cantidad()
        elif opcion == "4":
            calcular_resumen()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
