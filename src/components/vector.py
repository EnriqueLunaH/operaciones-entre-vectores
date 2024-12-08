def get_data_vector(vector_num, qty_elements):
  vector = []
  print("Ingrese los elementos del vector ", vector_num, ":")
  
  for i in range(qty_elements):
    element = int(input(f"Elemento {i+1}: "))
    vector.append(element)

  return vector