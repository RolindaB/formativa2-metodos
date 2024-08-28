import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    """Realiza la interpolación de Lagrange para aproximar el valor de y en un punto x.
    :param x_values: Lista de valores de x.
    :param y_values: Lista de valores correspondientes de y.
    :param x: El valor de x donde se quiere aproximar el valor de y.
    :return: El valor aproximado de y en x."""
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Ejemplo de uso
x_values = [0.698, 0.733, 0.768, 0.803]
y_values = [0.7661, 0.7432, 0.7193, 0.6946]
x = 0.75

y_approx = lagrange_interpolation(x_values, y_values, x)
print(f"El valor aproximado de y en x={x} es {y_approx}")
