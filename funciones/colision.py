from math import sqrt

def detectar_colision(x_1, y_1, x_2, y_2):
    distancia = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    if distancia <= 27:
        return True
    else: 
        return False