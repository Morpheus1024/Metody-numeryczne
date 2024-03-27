# Metody numeryczne Lab 4

## Metoda iteracyjnego podstawiania
### Teoria i założenia

Metoda opera się na przekształceniu układu rówań w taki sposób, by każde równanie opisywało daną niewiadomą. Przykładowe równania:

$$
x_1 = \sqrt{x_1*x_2}+10 x_2^2
$$

$$
x_2 = x_1^2+\frac{1}{\sqrt{x_2}}
$$

Następnie podstawiamy przykładowe wartości do równiani np. $x_1=1$, $x_2=1.5$. Otrzymujemy w ten sposób nowe wartosći szukanych zmiennych i ponawiamy podstawienie.
**Trzeba pamiętać, by do równania z $x_2$ podstawić wyliczoną wartość $x_1$.**
Niestety, metoda nie zawsze zbiega do prawidłowych wartości równania. Dużo zależy od bliskości wartości początkowych od tych rzecywistych jak i postaci równań opisujących dane niewiadome.

### Implementacja w Pythonie

```python
import numpy as np
import matplotlib.pyplot as plt

def uklad_rownan(x1,x2):
    x1_new=np.sqrt(10-x1*x2)
    x2_new=np.sqrt((57-x2)/(3*x1_new))
    return x1_new,x2_new

if __name__=="__main__":
    
    x1 = 2
    x2 = 2
    x1_values = []
    x2_values = []

    iteracje=100
    for i in range(iteracje+1):
        x1,x2=uklad_rownan(x1,x2)
        x1_values.append(x1)
        x2_values.append(x2)
    
    OX = np.linspace(0,iteracje,iteracje+1)
    plt.plot(OX,x1_values,label=f"x1:{x1_values[-1]}")
    plt.plot(OX,x2_values,label=f"x2:{x2_values[-1]}")
    plt.legend()
    plt.show()
```

## Metoda Newtona-Raphsona

### Teoria

Do oszacowania pieriastka $x_i$ prowadzi się styczną z punktu $(x_i,f(x_i))$ do osi $OX$. Punkt przecięcia stycznej z osią jest uznawany za kolejne oszacowanie pierwiastka.

$$
f'(x_i)=\frac{f(x_i)-0}{x_i - x_{i+1}} \iff x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

### Wykorzystanie rozwinięcia Taylor'a

Do oszacowania wartości funkcji w kolejnym punkcie iteracji można użyć następującego wzoru:

$$
f(x_{i+1})=f(x_i)+(x_{i+1}-x_{i})f'(x_i)
$$

Dla układu wielu zmiennych równanie przyjmuje następującą postać:

$$
f_{1,i+1} = f_{1,i}+(x_{1,i+1}-x_{1,i})\frac{df_{1,i}}{dx_{1}}+(x_{2,i+1}-x_{2,i})\frac{df_{1,i}}{dx_{2}}
$$

$$
f_{2,i+1} = f_{2,i}+(x_{1,i+1}-x_{1,i})\frac{df_{2,i}}{dx_{1}}+(x_{2,i+1}-x_{2,i})\frac{df_{2,i}}{dx_{2}}
$$

Po podstawieniu $f_{1,i+1}=0$ i $f_{2,i+1}=0$ otrzymujemy przekształcone równania:

$$
x_{1,i+1} = x_{1,i} - \frac{f_{1,i}\frac{df_{2,i}}{dx_2} - f_{2,i}\frac{df_{1,i}}{dx_2}}{det(J)}
$$

$$
x_{2,i+1} = x_{2,i} - \frac{f_{2,i}\frac{df_{1,i}}{dx_1} - f_{1,i}\frac{df_{2,i}}{dx_1}}{det(J)}
$$

gdzie $det(J)$ to wyznacznik macierzy Jacobiego.

### Implementacja w pythonie przy użyciu rozwinięcia Taylora do pierwszej pochodnej i macierzy Jackobego

```python
import numpy as np
import prettytable as pt

def uklad_rownan(x1,x2):

    f1 =x1**2 + x2*x1-10
    f2= x2+3*x1*x2**2-57

    ## macierz jakobiego:
    df1_dx1=2*x1+x2
    df1_dx2=x1

    df2_dx1=3*x2**2
    df2_dx2=1+6*x1*x2

    ## wyznacznik jakcobiego:
    detJ=df1_dx1*df2_dx2-df1_dx2*df2_dx1

    x1_new = x1- (f1*df2_dx2-f2*df1_dx2)/detJ
    x2_new = x2- (f2*df1_dx1-f1*df2_dx1)/detJ

    return x1_new,x2_new

if __name__ == '__main__':

    x1=1.5
    x2=3.5

    x1_values=[]
    x2_values=[]

    iteracje=10

    table = pt.PrettyTable()
    table.field_names = ["Iteracja", "x1", "x2"]

    for i in range(iteracje+1):
        x1,x2=uklad_rownan(x1,x2)
        x1_values.append(x1)
        x2_values.append(x2)  
        table.add_row([i,x1,x2])

    print(table) 
```
## scipy.optimize

### scipy.optimize.newton i scipy.optimize.bisect

```python
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
```