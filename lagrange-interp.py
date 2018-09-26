from functools import reduce
import sympy as sym
X = sym.Symbol('X')

def Lagrange(points):
    
    P=[reduce((lambda x,y: x*y),[(X-points[j][0])/(points[i][0] - points[j][0]) for j in range(len(points)) if i != j])*points[i][1] for i in range(len(points))]
    
    return sum(P)

print("Enter every points in this format : x y \nStop the list by entering 0")

p1=0
points=[]
while True:    
    p1 = [int(x) for x in input("Enter point coord: ").split()]
    if p1 == [0]:
        break
    points+=[p1]
print(points)
P=Lagrange(points)
print(P)

import matplotlib.pyplot as plt
import numpy as np

def graph(P,points):
    plt.plot([points[i][0] for i in range(len(points))], [points[i][1] for i in range(len(points))], 'ro')
    plt.title('P(X)=' + str(P))

    xmin=min([points[i][0] for i in range(len(points))])-1
    xmax=max([points[i][0] for i in range(len(points))])+1

    t1 = np.arange(xmin, xmax, 0.02)

    def f(t):
        t2 = []
        for i in t :
            t2 += [P.subs(X,i)]
        return t2

    plt.plot(t1,f(t1),'r--')
    plt.show()

graph(P,points)