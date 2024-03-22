import numpy as np
import matplotlib.pyplot as plt
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

