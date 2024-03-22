# Metody numeryczne Lab 4

## Metoda iteracyjnego podstawiania - Metoda punktu stałego

### Teoria i założenia
Metoda służy do iteracyjnego przybliżenia wartości pierwiastka danej funkcji. Nie wymaga znajomości przedziału jego wystąpienia. Metoda nie zawsze zbiega do właściwejgo rozwiazania.

Chcąc obliczyc pierwiastki funkcji $f(x)=0$ przekształcamt wzór do postaci $g(x)=x$ poprzez dodanie obustronne $x$. Znając "starą wartość" $x$ możemy wyznaczyć nową: $x_{i+1} = g(x_i)$. Możemy rozpocząć iterowanie rozwiązanie poprzez podstawienie na początku np. $x_0 = 0$. 

### Kryterium jakości
W celu sprawdzenia postępów stosuje się oszacowanie błędu względnego:

$$
e = |\frac{x_{i+1}-x_{i}}{x_{i+1}}| * 100\%
$$

### Monotoniczność
Zwróćmy uwagę, że prawdziwy błąd względny z i-tej iteracji stanowi około 0.5 −
0.6 wartości błędu z iteracji i−1. Jest to własność metody punktu stałego i
nazywa się ona **zbieżnością liniową**. Można wykazać, że błąd względny $i+1$ iteracji jest proporcjonalny do $i$ iteracji oraz pochodnej funckcji $g(x)$:

$$
E_{i+1} = g'(x)E_i
$$

Monotoniczność błędu zależy od wartości $g'(x)$
- $|g'(x) <1|$ - błąd się zmniejsza
- $|g'(x) >1|$ - błąd się zwiększa
  
Jeżeli pochodna jest dodatnia to wszystkie błędy będą miały ten sam znak, a gdy jest ujemna, to znak będzie się zminieniał za każdą iteracją.

### Implementacja w Pythonie

```python
import numpy as np

def funkcja(x):
    #x_i+1 = e^(-x_i)
    return np.exp(-x)

def iterative_substitution(ilosc_iteracji, x_0):
    
    x_i=[]
    e = []

    for i in range(ilosc_iteracji):
        if i==0:
            x_i.append(x_0)
            e.append("")
        else:
            x_i.append(funkcja(x_i[i-1]))
            e.append(abs(x_i[i]-x_i[i-1])/x_i[i]*100)
    return x_i, e

if __name__ == "__main__":
    print(iterative_substitution(10, 0))
```

## Metoda Newtona-Raphsona

### Teoria

Do oszacowania pieriastka $x_i$ prowadzi się styczną z punktu $(x_i,f(x_i))$ do osi $OX$. Punkt przecięcia stycznej z osią jest uznawany za kolejne oszacowanie pierwiastka.

$$
f'(x_i)=\frac{f(x_i)-0}{x_i - x_{i+1}} \iff x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

### Implementacja w pythonie przy użyciu rozwinięcia Taylora do pierwszej pochodnej i macierzy Jackobego

```python
# metoda iNewtona - Ralphsona dla funkcji f(x) = e^(-x) - x
# użycie szeregu taylora do przybliżenia pochodnej i macierzy Jackobego
import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt

# dla f(x) = x^10 -1

def funkcja(x):
    #x_i+1 = x_i - (x_i^10-1)/(10x_i^9)
    return x- (x**10 - 1)/pochodna(x)

def pochodna(x):
    return 10*x**9

def taylor(a, x):
    #f(x) = f(a) +  (x-a)f'(a)
    return funkcja(a) + pochodna(a)*(x-a)

def jacobian(x):
    #macierz Jacobiego - macierz o wielkości 1x1 to pochodna
    return pochodna(x)

def NR(x_0, ilosc_iteracji):

    x_i =[]
    e=[]

    for i in range(ilosc_iteracji+1):
        if i==0:
            x_i.append(x_0)
            e.append(100)
        else:
            x_i.append(funkcja(x_i[i-1]))
            e.append(abs(x_i[i]-x_i[i-1])/x_i[i]*100)
    return x_i, e
    
if __name__ =="__main__":

    x_i,e = NR(0.5, 42)
    pt1 = pt.PrettyTable()
    pt1.add_column("i", np.linspace(0,42,43))
    pt1.add_column("x_i", x_i)
    pt1.add_column("e%", e)

    print(pt1)

    plt.plot(np.linspace(0,42,43), x_i)
    plt.plot(np.linspace(0,42,43), e, 'r')
    plt.show()
```

## scipy.optimize