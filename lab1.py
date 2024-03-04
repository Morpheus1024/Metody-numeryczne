import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
#pip install prettytable

def funSeriesExpansion(x,n):

    #y(n) = x^(2n+1)/(2n+1)

    a=2*n+1
    y = np.power(x, a)/a

    return y

n = 10
x = 0.7

# wypisanie w tabeli wskazanych wartości
table = PrettyTable()
table.field_names=["n", "wartość rozwinięcia", "bład bezwzględny", "błąd względny [%]"]  
y=[]
arctanh = np.arctanh(x)
print(f"arc tanh(0.7) = {arctanh}")

for i in range(0,n+1):
    f = funSeriesExpansion(x,i)
    y.append(f)
    rozwiniecie = np.sum(y)
    blad_bezwzgledny = rozwiniecie-arctanh
    blad_wzgledny = blad_bezwzgledny/arctanh*100
    table.add_row([i,rozwiniecie,blad_bezwzgledny,blad_wzgledny])

print(table)
#print (y)

x_wykres = np.linspace(0,1,1000)

fig, ax = plt.subplots()

#dla n=10

ax.plot(x_wykres, funSeriesExpansion(x_wykres,10), label='n=10', color='blue')
ax.plot(x_wykres, funSeriesExpansion(x_wykres,0), label='n=0', color='red')
ax.plot(x_wykres, funSeriesExpansion(x_wykres,2), label='n=2', color='yellow')
ax.plot(x_wykres, funSeriesExpansion(x_wykres,7), label='n=7', color='green')

ax.set(xlabel='x', ylabel='y', title='Rozwinięcie wyrażenia arc tangh(x), x∊(0;1)')
ax.legend()
ax.grid(True)
plt.show()