# Control de inventario con arreglos en Python

## Descripción
Programa de consola que registra cinco productos de una tienda y sus cantidades disponibles mediante dos listas de Python. Cada posición de la lista `productos` corresponde a la misma posición de la lista `cantidades`.

## Objetivo
Practicar arreglos (listas), índices, recorridos con `for`, decisiones con `if`, búsquedas, modificaciones y cálculos.

## Lenguaje utilizado
Python 3. No utiliza librerías externas.

## Funcionalidades
- Mostrar cinco productos e indicar si tienen poco inventario (menos de 5 unidades).
- Consultar un producto por su índice (de 0 a 4).
- Cambiar la cantidad de un producto, validando los datos.
- Calcular el total de unidades y cuántos productos tienen stock bajo.
- Buscar un producto por su nombre.
- Mostrar un mensaje para entradas y opciones no válidas.

## Cómo ejecutar
1. Instalar Python 3 desde [python.org](https://www.python.org/downloads/).
2. Descargar este repositorio y abrir una terminal en su carpeta.
3. Ejecutar `python inventario.py` (o `python3 inventario.py`, según el sistema).
4. Escribir el número de una opción del menú y seguir las instrucciones.

## Datos iniciales

| Índice | Producto | Cantidad |
|---|---|---:|
| 0 | Arroz | 12 |
| 1 | Aceite | 7 |
| 2 | Azúcar (`Azucar` en el programa) | 4 |
| 3 | Leche | 9 |
| 4 | Café (`Cafe` en el programa) | 3 |

Inicialmente existen **35 unidades** y **2 productos con stock bajo**. Las modificaciones se mantienen mientras el programa permanece abierto; al reiniciarlo se recuperan los valores iniciales.

## Pruebas realizadas
- Mostrar inventario: aparecen cinco artículos.
- Resumen inicial: 35 unidades y dos productos con stock bajo.
- Consultar índice 2: se muestra Azucar con cuatro unidades.
- Cambiar índice 4 a 10: Cafe pasa a diez unidades y el total asciende a 42.
- Índice fuera de rango: se muestra un aviso en lugar de cerrar el programa.

## Autor
Kedwin Amadis Tejada — ITLA, Introducción a la Programación, Capítulo IX.
