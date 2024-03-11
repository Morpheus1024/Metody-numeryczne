import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
#pip install prettytable

#funkcja z poprzedniego labu to arc tanh(x)

def funDerivativeApprox(x,dx,fun):
    
    przyb_pochodnej = (fun(x+dx)-fun(x-dx))/(2*dx)

    return przyb_pochodnej

x = 0.5

dx = []
dx_wartosc = 2
for i in range (0,20):
    dx_wartosc=dx_wartosc/5
    dx.append(dx_wartosc)

# print(dx)
# print(len(dx))
    
pochodna_arc_tanh = []

table = PrettyTable()
table.field_names=["dx", "wartość obliczonej pochodnej", "bład bezwzględny"]

dx = np.array(dx)
pochodna_arc_tanh = funDerivativeApprox(x, dx, np.arctanh)
blad_przyblizenia = pochodna_arc_tanh - 1/(1+x**2)


for i in range(0,20):
    table.add_row([dx[i],pochodna_arc_tanh[i],pochodna_arc_tanh[i]-1/(1+x**2)])

print(table)

plt.subplot(1,2,1)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('dx')
plt.ylabel('blad przybliżenia')
plt.title('Wykres błędu przybliżenia')

plt.plot(dx,blad_przyblizenia)

print(f"Najmniejszy błąd względny występuje dla dx = {dx[np.argmin(np.abs(blad_przyblizenia))]}")

przedzial_x = np.linspace(0,1,101)

blad_przyblizenia_na_wykresie =[]

blad_przyblizenia_na_wykresie = funDerivativeApprox(przedzial_x, dx[np.argmin(np.abs(blad_przyblizenia))], np.arctanh) - 1/(1+przedzial_x**2)

plt.subplot(1,2,2)
plt.title("Dla dx dającego najmniejszy błąd względny")
plt.xlabel('x')
plt.ylabel('blad przybliżenia')
plt.plot(przedzial_x,blad_przyblizenia_na_wykresie)
plt.show()
