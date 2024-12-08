import numpy as np

def add_vectors(v1, v2):
  """
  Suma dos vectores componente a componente.

  :param v1: Lista o tupla del vector 1
  :param v2: Lista o tupla del vector 2
  :return: Vector resultante de la suma
  """
  if len(v1) != len(v2):
    raise ValueError("Ambos vectores deben tener la misma dimensión.")
  
  return [v1[i] + v2[i] for i in range(len(v1))]


def product_dot(v1, v2):
  """
  Calcula el producto punto entre dos vectores.

  :param v1: Lista o tupla del vector 1
  :param v2: Lista o tupla del vector 2
  :return: Escalar resultante del producto punto
  """
  if len(v1) != len(v2):
    raise ValueError("Ambos vectores deben tener la misma dimensión.")
  
  return np.dot(v1, v2)

def cross_product(v1, v2):
  """
  Calcula el producto cruz entre dos vectores.

  :param v1: Lista o tupla del vector 1
  :param v2: Lista o tupla del vector 2
  :return: Vector resultante del producto cruz
  """
  if len(v1) != 3 or len(v2) != 3:
    raise ValueError("Ambos vectores deben tener dimensión 3.")
  
  return np.cross(v1, v2)

def magnitude_calculate(v):
  """
  Calcula la magnitud de un vector.

  :param v: Lista o tupla del vector
  :return: Magnitud del vector
  """
  return np.linalg.norm(v)

def multiply_by_scale(v, escalar):
  """
  Multiplica un vector por un escalar.

  :param v: Lista o tupla del vector
  :param escalar: Escalar
  :return: Vector resultante de la multiplicación
  """
  return np.array(v) * escalar

def calculate_unitary_vector(v):
  """
  Calcula el vector unitario de un vector.

  :param v: Lista o tupla del vector
  :return: Vector unitario
  """
  return np.array(v) / np.linalg.norm(v)

def get_proyeccion(v1, v2):
  """
  Calcula la proyección de un vector sobre otro.

  :param v1: Lista o tupla del vector a proyectar
  :param v2: Lista o tupla del vector sobre el que se proyecta
  :return: Vector resultante de la proyección
  """
  return (np.dot(v1, v2) / np.linalg.norm(v2)) * np.array(v2)

def calculate_angle(v1, v2):
  """
  Calcula el ángulo entre dos vectores.

  :param v1: Lista o tupla del vector 1
  :param v2: Lista o tupla del vector 2
  :return: Ángulo entre los dos vectores
  """

  # Calcular la magnitud de los vectores
  magnitude_v1 = magnitude_calculate(v1)
  magnitude_v2 = magnitude_calculate(v2)

  # Calcular el producto punto de los vectores
  dot_product = product_dot(v1, v2)

  # Calcular el coseno del ángulo
  cos_theta = dot_product / (magnitude_v1 * magnitude_v2)

  # Limpiar el rango del coseno
  cos_theta = np.clip(cos_theta, -1, 1)

  # Calcular el ángulo
  theta = np.arccos(cos_theta)

  return theta

def get_vector_limits(vectores):
  """
  Calcula los límites de los ejes x e y para una lista de vectores.

  :param vectores: Lista de vectores
  :return: Tupla con los límites (x_min, x_max, y_min, y_max)
  """
  x_coords = [v[0] for v in vectores]
  y_coords = [v[1] for v in vectores]
  
  x_min, x_max = min(x_coords), max(x_coords)
  y_min, y_max = min(y_coords), max(y_coords)
  
  return x_min, x_max, y_min, y_max
