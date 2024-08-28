import math

def interpolacion_lineal(x0, y0, x1, y1, x):
    """
    Realiza la interpolación lineal entre dos puntos para aproximar el valor de y en un punto x.
    :param x0: Valor de x en el primer punto.
    :param y0: Valor de y en el primer punto (f(x0)).
    :param x1: Valor de x en el segundo punto.
    :param y1: Valor de y en el segundo punto (f(x1)).
    :param x: El valor de x donde se quiere aproximar el valor de y.
    :return: El valor aproximado de y en x.
    """
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def main():
    # Definir la función f(x) = e^x
    f = math.exp

    # Pedir al usuario que ingrese los puntos y el valor de x a aproximar
    x0 = float(input("Ingrese el valor de x0: "))
    x1 = float(input("Ingrese el valor de x1: "))
    x = float(input(f"Ingrese el valor de x donde desea aproximar f(x): "))

    # Calcular los valores de f(x0) y f(x1)
    y0 = f(x0)
    y1 = f(x1)

    # Realizar la interpolación
    y_aprox = interpolacion_lineal(x0, y0, x1, y1, x)
    print(f"\nAproximación de f({x}) usando interpolación lineal: {y_aprox:.5f}")

    # Calcular el valor real para comparar (si la función es conocida)
    y_real = f(x)
    print(f"Valor real de f({x}): {y_real:.5f}")
    
if __name__ == "__main__":
    main()

