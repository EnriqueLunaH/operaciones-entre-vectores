import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
from mpl_toolkits.mplot3d import Axes3D

from src.math.operations import calculate_angle, get_vector_limits

def plot_vectors(vectores, colores, labels):
  """
  Grafica una lista de vectores en el espacio 3D.

  :param vectores: Lista de vectores
  :param colores: Lista de colores para cada vector
  :param labels: Lista de etiquetas para cada vector
  """
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  for i in range(len(vectores)):
      ax.quiver(0, 0, 0, vectores[i][0], vectores[i][1], vectores[i][2], color=colores[i], label=labels[i])

  # Calcular los límites dinámicamente
  max_val = max([LA.norm(v) for v in vectores]) + 1
  ax.set_xlim([-max_val, max_val])
  ax.set_ylim([-max_val, max_val])
  ax.set_zlim([-max_val, max_val])

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.legend()
  plt.show()

def plot_vectors_and_angle(a, b):
  """
  Grafica dos vectores en 3D y muestra el ángulo entre ellos.
  """
  # Calcular el ángulo en radianes
  angulo_radianes = calculate_angle(a, b)
  angulo_grados = np.degrees(angulo_radianes)

  # Configuración del gráfico
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Graficar los vectores
  ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label=f"Vector A {a}")
  ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label=f"Vector B {b}")

  # Etiquetas y título
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title("Ángulo entre dos vectores 3D")

  # Mostrar el ángulo
  ax.text2D(0.05, 0.95, f"Ángulo: {angulo_grados:.2f}°", transform=ax.transAxes, fontsize=12, color="green")

  # Configuración de los límites
  max_val = max(LA.norm(a), LA.norm(b)) + 1
  ax.set_xlim([-max_val, max_val])
  ax.set_ylim([-max_val, max_val])
  ax.set_zlim([-max_val, max_val])

  plt.legend()
  plt.show()