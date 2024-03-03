# Metody Nummeryczne lab 1

## Numpy pomocne komendy na wektorach

- np.arange(10) #generuje wektor od 0 do 9
- np.zeros(10) #generuje wektor 10 zer
- np.ones(10) #generuje wektor 10 jedynek
- np.random.rand(10) #generuje wektor 10 liczb losowych z przedziału [0, 1]
- np.random.randn(10) #generuje wektor 10 liczb losowych z rozkładu normalnego
- vector_a + vector_b #dodawanie wektorów
- vector_a *2 #mnożenie wektora przez skalar
- np.linspace(0, 10, 100) #generuje wektor 100 liczb z przedziału [0, 10]
- np.eye(10) #generuje macierz 10x10 z jedynkami na przekątnej
- inverse_matrix = np.linalg.inv(matrix) #odwraca macierz
- np.dot(matrix_a, matrix_b) #mnożenie macierzy
- determinant = np.linalg.det(matrix) #wyznacznik

## Wyswietlanie danych w formie tekstowej

### użycie Pretty Table

```python
# pip install prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Name", "Age", "City"]

table.add_row(["Alice", 30, "New York"])
table.add_row(["Bob", 25, "San Francisco"])
table.add_row(["Charlie", 22, "Los Angeles"])

print(table)

+---------+-----+---------------+
| Name    | Age | City          |
+---------+-----+---------------+
| Alice   | 30  | New York      |
| Bob     | 25  | San Francisco |
| Charlie | 22  | Los Angeles   |
+---------+-----+---------------+
```

### Użycie numpy i fora

```python
import numpy as np

text_data = np.array([["Name", "Age", "City"],
                      ["Alice", "30", "New York"],
                      ["Bob", "25", "San Francisco"],
                      ["Charlie", "22", "Los Angeles"]])

for row in text_data:
    print("|".join(row))


Name   |Age|City          
Alice  |30 |New York      
Bob    |25 |San Francisco 
Charlie|22 |Los Angeles   
```

### Wyświetlanie wektora

```python
import numpy as np

vector = np.array([1, 2, 3, 4, 5])
print(f"Vector: {vector}")
```

```python
import numpy as np

vector = np.array([1, 2, 3, 4, 5])
vector_text = "[" + " ".join(map(str, vector)) + "]"
print(f"Vector: {vector_text}")
```

```python
import numpy as np

vector = np.array([1, 2, 3, 4, 5])
vector_text = np.array_str(vector)
print(f"Vector: {vector_text}")
```

__Wszyskie wyświetlają ten sam tekst:__
__Vector: [1 2 3 4 5]__

### Inne, wyświetlanie tekstu

```python
text = "Hello, world!"
print(text)
```

```python
name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))
```

```python
name = "Charlie"
age = 22
print(f"Name: {name}, Age: {age}")
```

## Użycie matplotlib do wyświetlanie funkcji na wykresie (podpisywanie osi itp)

```python
import numpy as np
import matplotlib.pyplot as plt

# Przykładowe dane
x = np.linspace(0, 2*np.pi, 100)
sin_values = np.sin(x)
cos_values = np.cos(x)

# Tworzenie obiektów figury i osi
fig, ax = plt.subplots()

# Rysowanie dwóch przebiegów na jednym wykresie z różnymi kolorami
ax.plot(x, sin_values, label='sin(x)', color='blue')
ax.plot(x, cos_values, label='cos(x)', color='red')

# Rysowanie dwóch przebiegów na jednym wykresie z różnymi stylami linii
#ax.plot(x, sin_values, label='sin(x)', linestyle='-', color='blue')  # Solid line
#ax.plot(x, cos_values, label='cos(x)', linestyle='--', color='red')  # Dashed line

# Dodawanie etykiet i tytułu
ax.set(xlabel='x', ylabel='y', title='Wykres funkcji sin(x) i cos(x)')
# Dodawanie legendy
ax.legend()
# Dodawanie siatki
ax.grid(True)
# Wyświetlanie wykresu
plt.show()
```

## Znajomość szeregu Maclaurina

### Definicja

#### Szczególny przypadek szeregu Taylora, gdy x0 = 0

__Suma od n=0 do nieskończoności, z kolejnych pochodnych funkcji dla x0=0 pomnożonych przez kolejną potęgę x, podzielonej przez n!__

[link do definicji](https://mathworld.wolfram.com/MaclaurinSeries.html)
>∑ f(pochodna n)(0)*x^n/n! = f(0) + f'(0)x/1! + f''(0)x^2/2! + f'''(0)x^3/3! + ...

### Szczególny przypadek w numpu dla e^x

```python
import numpy as np

def maclaurin_e_to_the_x(x, terms):
    result = np.zeros_like(x, dtype=float)
    factorial = 1

    for n in range(terms):
        result += x ** n / factorial
        factorial *= (n + 1)

    return result

# Przykład użycia
x_values = np.linspace(0, 1, 100)
approximation_3_terms = maclaurin_e_to_the_x(x_values, 3)
approximation_5_terms = maclaurin_e_to_the_x(x_values, 5)

print(f"Approximation (3 terms): {approximation_3_terms}")
print(f"Approximation (5 terms): {approximation_5_terms}")
```

### Ciekawe rozwiazanie w sympy

```python
import sympy as sp

def maclaurin_series(function, variable, terms):
    x = sp.symbols(variable)
    maclaurin_series = function.series(x, 0, terms).removeO()
    return maclaurin_series

# Przykłady użycia
# Dla funkcji e^x
e_to_the_x = sp.exp(x)
approximation_e_to_the_x = maclaurin_series(e_to_the_x, 'x', 5)
print(f"Approximation for e^x: {approximation_e_to_the_x}")

# Dla funkcji sin(x)
sin_x = sp.sin(x)
approximation_sin_x = maclaurin_series(sin_x, 'x', 5)
print(f"Approximation for sin(x): {approximation_sin_x}")

# Dla funkcji ln(1+x)
ln_1_plus_x = sp.log(1 + x)
approximation_ln_1_plus_x = maclaurin_series(ln_1_plus_x, 'x', 5)
print(f"Approximation for ln(1+x): {approximation_ln_1_plus_x}")
```
