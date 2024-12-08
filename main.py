import numpy as np
import matplotlib.pyplot as plt
import os

from src.math.operations import add_vectors, product_dot, cross_product, magnitude_calculate, multiply_by_scale, calculate_unitary_vector, get_proyeccion, calculate_angle
from src.components.graphics import plot_vectors, plot_vectors_and_angle
from src.components.vector import get_data_vector

if __name__ == "__main__":
  # Solicitar la cantidad de elementos de los vectores
  qty_elements = int(input("Ingrese la cantidad de elementos de los vectores: "))

  while True:
    os.system("cls")
    print("=== Menu ===")
    print("1. Suma")
    print("2. Producto punto")
    print("3. Producto cruz")
    print("4. Magnitud")
    print("5. Multiplicación por un escalar")
    print("6. Vector unitario")
    print("7. Proyección")
    print("8. Ángulo")
    print("9. Salir")

    option = int(input("Seleccione una opción: "))
    os.system("cls")

    if option == 9:
      break

    if option < 1 or option > 9:
      print("Opción inválida.")
      continue

    if option == 1:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      # Sumar los vectores
      result_add = add_vectors(v1, v2)

      # imprimir el resultado de la suma
      print(v1, "+", v2, "=", result_add)

      # Graficar los vectores 1 y 2 y el resultado de la suma
      vectors = [v1, v2, result_add]
      colors = ['r', 'b', 'g']
      labels = ['Vector 1', 'Vector 2', 'Resultado']
      plot_vectors(vectors, colors, labels)

    if option == 2:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      # Calcular el producto punto
      dot_product = product_dot(v1, v2)

      # Imprimir el resultado del producto punto
      print(v1, "•", v2, "=", dot_product)
      
      # Graficar los vectores 1 y 2
      vectors = [v1, v2]
      colors = ['r', 'b']
      labels = ['Vector 1', 'Vector 2']
      plot_vectors(vectors, colors, labels)

    if option == 3:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      # Calcular el producto cruz
      cross_product_result = cross_product(v1, v2)

      # Imprimir el resultado del producto cruz
      print(v1, "x", v2, "=", cross_product_result)

      # Graficar los vectores 1 y 2 y el resultado del producto cruz
      vectors = [v1, v2, cross_product_result]
      colors = ['r', 'b', 'g']
      labels = ['Vector 1', 'Vector 2', 'Resultado']
      plot_vectors(vectors, colors, labels)

    if option == 4:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      # Calcular la magnitud de los vectores
      magnitud_v1 = magnitude_calculate(v1)
      magnitud_v2 = magnitude_calculate(v2)

      # Imprimir la magnitud de los vectores
      print(v1, " su magnitud es: ", magnitud_v1)
      print(v2, " su magnitud es: ", magnitud_v2)

      # Graficar los vectores 1 y 2
      vectors = [v1, v2]
      colors = ['r', 'b']
      labels = ['Vector 1', 'Vector 2']
      plot_vectors(vectors, colors, labels)

    if option == 5:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      scalar = int(input("Ingrese el escalar: "))

      # Calcular la multiplicación de un vector por un escalar
      result_product = multiply_by_scale(v1, scalar)

      # Imprimir el resultado de la multiplicación
      print(v1, " * ", scalar, " = ", result_product)

      # Graficar los vectores 1 y el resultado de la multiplicación
      vectors = [v1, result_product]
      colors = ['r', 'b']
      labels = ['Vector 1', 'Resultado']
      plot_vectors(vectors, colors, labels)

    if option == 6:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)

      # Calcular el vector unitario
      unit_vector = calculate_unitary_vector(v1)

      # Imprimir el vector unitario
      print(v1, " su vector unitario es: ", unit_vector)

      # Graficar los vectores 1 y el vector unitario
      vectors = [v1, unit_vector]
      colors = ['r', 'b']
      labels = ['Vector 1', 'Vector Unitario']
      plot_vectors(vectors, colors, labels)

    if option == 7:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      while True:
        # preguntar si se quiere calcular la proyección de v1 sobre v2 o de v2 sobre v1
        print("¿Qué proyección desea calcular?")
        print("1. Proyección de v1 sobre v2")
        print("2. Proyección de v2 sobre v1")
        print("3. Salir")
        option_proyeccion = int(input("Seleccione una opción: "))
        os.system("cls")

        # incializar la variable proyeccion
        proyeccion = []

        if option_proyeccion == 1:
          # Calcular la proyección de v1 sobre v2
          proyeccion = get_proyeccion(v1, v2)

          # Imprimir la proyección
          print("La proyección de ", v1, " sobre ", v2, " es: ", proyeccion)

          # Graficar los vectores v1, v2 y la proyección
          vectors = [v1, v2, proyeccion]
          colors = ['r', 'b', 'g']
          labels = ['Vector 1', 'Vector 2', 'Proyección']
          plot_vectors(vectors, colors, labels)
        elif option_proyeccion == 2:
          # Calcular la proyección de v2 sobre v1
          proyeccion = get_proyeccion(v2, v1)

          # Imprimir la proyección
          print("La proyección de ", v2, " sobre ", v1, " es: ", proyeccion)

          # Graficar los vectores v1, v2 y la proyección
          vectors = [v2, v1, proyeccion]
          colors = ['r', 'b', 'g']
          labels = ['Vector 2', 'Vector 1', 'Proyección']
          plot_vectors(vectors, colors, labels)

        elif option_proyeccion == 3:
          break
        else:
          print("Opción inválida.")
          continue

    if option == 8:
      # limpiar la pantalla
      os.system("cls")

      # Solicitar los vectores
      v1 = get_data_vector(1, qty_elements)
      v2 = get_data_vector(2, qty_elements)

      # Calcular el ángulo entre dos vectores
      angle_radians = calculate_angle(v1, v2)
      angle_degrees = np.degrees(angle_radians)

      # Imprimir el ángulo entre los dos vectores
      print("El ángulo entre ", v1, " y ", v2, " es: ", angle_radians, "radianes")
      print("El ángulo entre ", v1, " y ", v2, " es: ", angle_degrees, "°")

      # Graficar los vectores v1 y v2 y el ángulo entre ellos
      plot_vectors_and_angle(v1, v2)
      
  print("¡Hasta luego!")