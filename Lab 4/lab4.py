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