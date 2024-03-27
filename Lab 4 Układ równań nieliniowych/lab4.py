import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import bisect
from scipy.optimize import newton

# y = 3x**2 - 5*x + 0.5
# 2y = -x**2+3xy

# Define the functions
def f1(x):
    return 3*x**2 - 5*x + 0.5

def f2(x):
    return (-x**2)/(2-3*x)

# Define the function for the system of equations
def system(x):
    return f1(x) - f2(x)

def iteracyjne_podstawienie(x, y):
    #y_new = 3*x**2-5*x+0.5
    #x_new = np.sqrt(3*x*y_new-2*y_new)

    x_new = 0.6*x**2 +0.1 -0.2*y
    y_new = -0.5*x_new**2+1.5*x_new*y

    return x_new, y_new

def NR_implementacja_wlasna(x):

    #przekształcone równania (te same co w iteracyjnym podstawieniu)
    # f1 = 0.6*x**2 +0.1 -0.2*y
    # f2 = -0.5*x**2+1.5*x*y

    # df1_dx = 1.2*x
    # df1_dy = -0.2

    # df2_dx = 1.5*y-x
    # df2_dy = 1.5*x

    # detJ=df1_dx*df2_dy-df1_dy*df2_dx

    # if detJ!=0:
    #     x_new = x- (f1*df2_dy-f2*df1_dy)/detJ
    #     y_new = y- (f2*df1_dx-f1*df2_dx)/detJ

    #     return x_new, y_new
    # else: return x,y
    ## nieststey implementacja daje błędne wyniki, które mogą wynikać m.in. ze złego punktu startowego

    ##inne, prostrze rozwiazanie:

    f = 3*x**2-5*x+1/2 - (-x**2)/(2-3*x)

    df_dx = (54*x**3 -120*x**2 + 88*x-20)/(9*x**2-12*x+4)

    x_new = x - f/df_dx

    return x_new


# Rozwiązanie graficzne

x = np.linspace(0, 2, 1000)
y1 = 3*x**2 - 5*x + 0.5
y2 = (-x**2)/(2-3*x)

#plt.plot(x, y1, label='y = 3x**2 - 5*x + 0.5')
#plt.plot(x, y2, label='2y = -x**2+3xy')
#plt.ylim(-2, 3)
#plt.legend()

fig, axs = plt.subplots(2, 2)

# Subplot 1
axs[0, 0].plot(x, y1, label='y = 3x**2 - 5*x + 0.5')
axs[0, 0].plot(x, y2, label='2y = -x**2+3xy')
axs[0, 0].set_title('Wszystkie miejsca zerowe')
axs[0, 0].legend()
axs[0, 0].set_ylim(-2, 3)

# Subplot 2
axs[0, 1].plot(x, y1, label='y = 3x**2 - 5*x + 0.5')
axs[0, 1].plot(x, y2, label='2y = -x**2+3xy')
axs[0, 1].set_title('1. miejsce zerowe')
axs[0, 1].legend()
axs[0, 1].set_xlim(0, 0.2)
axs[0, 1].set_ylim(-0.5, 0.5)

# Subplot 3
axs[1, 0].plot(x, y1, label='y = 3x**2 - 5*x + 0.5')
axs[1, 0].plot(x, y2, label='2y = -x**2+3xy')
axs[1, 0].set_title('2. miejsce zerowe')
axs[1, 0].legend()
axs[1, 0].set_xlim(0.5, 0.59)
axs[1,0].set_ylim(-1.5, -1.3)

# Subplot 4
axs[1, 1].plot(x, y1, label='y = 3x**2 - 5*x + 0.5')
axs[1, 1].plot(x, y2, label='2y = -x**2+3xy')
axs[1, 1].set_title('3. miejsce zerowe')
axs[1, 1].legend()
axs[1, 1].set_xlim(1.7, 1.8)
axs[1,1].set_ylim(0.94, 0.95)

# Display the figure with subplots
#plt.tight_layout()

# miejsca przecięć: 
## x=0.108, y=-0.007
## x= 0.585, y= -1.389
## x = 1.75, y = 0.9425

# Znaleźć jedno rozwiązanie układu
## scipy.optimize.bisection

# W pobliży x = 0.108:
print("\n   Metoda bisekcji ze scipy:")
solution = bisect(system, 0, 0.2)
print(f"x1 = {solution}, y1 = {f1(solution)}")
# W pobliży x = 0.585:
solution = bisect(system, 0.4, 0.6)
print(f"x2 = {solution},  y2 = {f1(solution)}")
# W pobliży x = 1.75:
solution = bisect(system, 1.5, 1.8)
print(f"x3 = {solution},  y3 = {f1(solution)}")
print()
      
## metoda iteracyjnego powstawienia
x1, y1 = 0.1, 0
ilosc_iteracji=10

for i in range(ilosc_iteracji+1):
    x1, y1 = iteracyjne_podstawienie(x1, y1)

print(f"    Metoda punltu stacjonarnego po 100 iteracjach: \nx={x1}, y={y1}")

#Metoda Newtona-Raphsona
print("\n   Metoda N-R:")

##scipy.optimize.newton:
print("\nZe scipy.optimize.newton:")
x= np.linspace(0,2,20)
for i in x:
    if 2-3*i !=0:
        miejsce_zerowe = newton(system,i)
        print(f"x = {miejsce_zerowe}, y = {f1(miejsce_zerowe)}")

## implementacja własna
print("\n   NR implementacja własna")

x2 = 0.4

for i in range(ilosc_iteracji+1):
    #x2,y2 = NR_implementacja_wlasna(x2, y2)
    #print(f"x = {x2}, y = {y2}")
    x2 = NR_implementacja_wlasna(x2)

    print(x2, f1(x2))

plt.show()