import numpy as np
from scipy import signal as sg
import matplotlib.pyplot as plt
import control

c2 = 1
c1 = 3
c0 = 4

a2 = 3
a1 = 3
a0 = 2

licznik= c2, c1, c0
mianownik = 1, a2, a1, a0

fig, axs = plt.subplots(2)

# znalezienie biegunów i określeni czy są stabilne
poles = np.roots(mianownik)
for pole in poles:
    if (pole.real >= -1 and pole.real <=1) and (pole.imag >= -1 and pole.imag <=1):
        print(f"{pole} - Układ stabilny\n")
    else:
        print(f"{pole} - Układ niestabilny\n")

# odpowiedź impulsowa układu za pomocą scipy.signal.dlti
sys = sg.dlti(licznik, mianownik)
t1, y1 = sg.dimpulse(sys)
y1 = np.squeeze(y1)
#plt.plot(t1, y1)
axs[0].plot(t1, y1)
axs[0].set_title('Impulse response')

#zamiana na model stanowy

A = [[-a2, -a1, -a0], [1, 0, 0], [0, 1, 0]]
B = [[1], [0], [0]]
C = [c2, c1, c0]
D = [0]
print(f"A = {A},\n B = {B},\n C = {C},\n D = {D}")

# odpowiedź skokowa na podstawie modelu stanowego, x[0]=0, u[n]=1
sys = control.ss(A, B, C, D)
t2,y2 = control.step_response(sys)

axs[1].plot(t2, y2)
axs[1].set_title('Step response')

# implementacja dyskretnego sterownika LQR

Q = np.eye(3)
R = 1
K, S, E = control.dlqr(A, B, Q, R)
print(f"K = {K}")

# implementacja macierzy P równania Riccatiego

P = control.solve_discrete_are(A, B, Q, R)
print(f"P = {P}")


plt.show()