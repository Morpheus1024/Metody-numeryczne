import numpy as np
import matplotlib.pyplot as plt

# Generowanie danych
x = np.linspace(1, 100, 1000)  # Przykładowe wartości x
y = np.log(x)  # Logarytm naturalny z x

fig, ax = plt.subplots()
# Tworzenie wykresu w skali logarytmicznej
plt.plot(x, y)
plt.plot(x, y, '.')  # Dodanie punktów na wykresie
plt.xscale('log')  # Ustawienie skali logarytmicznej na osi x
plt.yscale('log')  # Ustawienie skali logarytmicznej na osi y

# Dodanie etykiet i tytułu
plt.xlabel('Wartości x')
plt.ylabel('Wartości log(x)')
plt.title('Wykres w skali logarytmicznej')

# Wyświetlenie wykresu
plt.show()
