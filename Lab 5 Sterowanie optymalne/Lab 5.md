# Metody numeryczne Lab 5
## Bieguny transmitancji i stabilność
### Teoria
Dla układów dyskretnoczasowych mowa jest o stabilności, gdy wszystkie bieguny - miejsca zerowe mianownika - znajdują się wewnatrz okręgu jendostkowego płaszczyzny zespolonej.
W przypadku postaci układu stanowego, analizowane są wartości własne macierzy A. Jeżeli nie przekracają jedności na płaszczyźnie zespolonej, to odpowiedź układu będzie ograniczona, a tym samym stabilna.
Przykład:

$$
G(z) = \frac{c_2z^2+c_1z+c_0}{z^3+a_2z^2+a_1z+a_0}
$$

Powyższą transmitancję możemy zapisać za pomocą następującego modelu stanowego:

$$
A = 
\begin{bmatrix}
-a_2 & -a_1 & -a_0\\
1 & 0 & 0\\
0 & 1 & 0
\end{bmatrix}
, B = 
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}
, C = 
\begin{bmatrix}
c_2 & c_1 & c_0
\end{bmatrix}
, D =
0
$$
### Implementacja w Pythonie - numpy.roots
```python
import numpy as np
#licznik:
c2=2
c1 = 3
c0 = 5
licznik= c2, c1, c0

#minownik
a2 = 1
a1 = 1
a0 = 1
mianownik = 1, a2, a1, a0

roots = np.roots(mianownik)
for root in roots:
    if (root.real >= -1 and root.real <=1) and (root.imag >= -1 and root.imag <=1):
        print(f"{root} - Układ stabilny\n")
    else:
        print(f"{root} - Układ niestabilny\n")

```

## Odpowiedź impulowa
### Implementacja w Pythonie - scipy.signal.dlti
```python
import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt

c1 = 3
c0 = 4

a1 = 1
a0 = 2

licznik= c1, c0
mianownik = a1, a0
#H(z) = (3z + 4) / (z + 2)

t, y = sg.dlti(licznik, mianownik, dt=0.1).step(n=20)
print(t)
y = np.squeeze(y)
plt.plot(t, y)
plt.show()
```


