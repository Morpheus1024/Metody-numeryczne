# metoda iteracyjnego podstawienia
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
