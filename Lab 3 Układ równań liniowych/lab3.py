import numpy as np
from scipy.linalg import lu, solve_triangular
import scipy as sp

# 1:  0 = Qa*Ca + Ws + E12*(C2 - C1)
# 2:  0 = Qb*Cb + E12*(C1 - C2) + E23*(C3 - C2)
# 3:  0 = E23*(C2 - C3) + E35*(C5 - C3) + E34*(C4 - C3)
# 4:  0 = E34*(C3 - C4) - Qc*C4
# 5:  0 = Wg - Qd*C5 + E35*(C3 - C5)




def liczenie_macierzy(E12, E23, E34, E35, Wg, Ws, ca, cb, Qa, Qb, Qc, Qd, Lu_if):
    A = [
        [-E12, E12, 0, 0, 0],
        [E12, -E12 - E23, E23, 0, 0],
        [0, E23, -E23 - E34 - E35, E34, E35],
        [0, 0, E34, -E34 - Qc, 0],
        [0, 0, E35, 0, -Qd -E35]
    ]

    B = [
        [-Ws-Qa*ca],
        [-Qb*cb],
        [0],
        [0],
        [-Wg]
    ]


        # Zastosowanie rozkłądu LU
    P, L, U = lu(A)
    
    if Lu_if:
        print("Trójkątna dolna:", "\n", L, "\n")
        print("Trójkątna górna:", "\n", U, "\n")

    # Rozwiązanie układu równań

    c = np.linalg.solve(A, B,)
    print("Macierz c:", "\n", c)

    return c, L, U, A, B


if __name__ == "__main__":

    #pierwotne wartości

    Qa = 200
    ca = 2
    Ws = 1500

    Qb = 300
    cb = 2

    Qc = 150
    Qd = 350

    Wg = 2500

    E12 = 25
    E23 = 50
    E34 = 50
    E35 = 25

    # rozwiazanie dla pierwotnych wartości
    co1,L1, U1, A1, B1 = liczenie_macierzy(E12,E23, E34, E35, Wg, Ws, ca, cb, Qa, Qb, Qc, Qd, True)

    # Ws = 800, Wg = 1200
    print("\n Dla Ws = 800 i Wg = 1200 \n")
    co2, L2, U2, A2, B2 = liczenie_macierzy(E12,E23, E34, E35, 1200, 800, ca, cb, Qa, Qb, Qc, Qd, False)

    print(f"\nPorównanie otrzymanych wektorów:")
    print(f"c1:\n{co1} \n c2:\n {co2}")

    print("\n Widać zmniejszenie na każej z wartości stężenia CO panującej w każdym pomieszczeniu. Wynika to ze zmniejszenia wartości strumienia obu źródeł C.O")

    # wyznacznie macierzy odwrotnej metodą LU
    A1_inv = np.dot(np.linalg.inv(U1), np.linalg.inv(L1))
    A2_inv = np.dot(np.linalg.inv(U2), np.linalg.inv(L2))
    print("\n Macierz odwrotna A^(-1) \n", A1_inv)

    #znalezienie udziału procentowego

    grill = 2500 *A1_inv[3][4]/co1[3] *100
    palacze = 1500 *A1_inv[3][0]/co1[3]*100
    ulica = (200*2*A1_inv[3][0]+300*2*A1_inv[3][1])/co1[3]*100

    grill2 = 1200 *A2_inv[3][4]/co2[3] *100
    palacze2 = 800 *A2_inv[3][0]/co2[3]*100
    ulica2 = (200*2*A2_inv[3][0]+300*2*A2_inv[3][1])/co2[3]*100

    print(f"\nUdział procentowy grilla w pokoju dla dzieci to {-grill}%, dla palaczy to {-palacze}%, a ulicy to {-ulica}%")
    print("\nDla drugiego przpadku:")
    print(f"\nUdział procentowy grilla w pokoju dla dzieci to {-grill2}%, dla palaczy to {-palacze2}%, a ulicy to {-ulica2}%")


    
