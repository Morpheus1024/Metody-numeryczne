from scipy.optimize import newton
from scipy.optimize import bisect
import prettytable as pt
import numpy as np

# Definiowanie funkcji, dla której chcemy znaleźć miejsca zerowe
def funkcja(x):
    return x**3 - 6*x**2 + 11*x - 6

# Szukanie miejsca zerowego za pomocą metody Newtona
newton_x =[]
bisect_x = []

table = pt.PrettyTable()
for i in np.arange(0, 7, 0.25):
    miejsce_zerowe = newton(funkcja, i)
    newton_x.append(miejsce_zerowe)
    # print(f"Miejsce zerowe dla x = {i}: {miejsce_zerowe}")

table.add_column("x", np.arange(0, 7, 0.25))
table.add_column("newton", newton_x)

for i in np.arange(0, 7, 0.25):
    miejsce_zerowe = bisect(funkcja, 0, 7) ## wskazuje tylko jedno miejsce zerowe
    bisect_x.append(miejsce_zerowe)
    # print(f"Miejsce zerowe dla x = {i}: {miejsce_zerowe}")

table.add_column("bisect", bisect_x)

print(table)