#================================================
# Bracketing Method - 01 Bisection method 
#================================================


import numpy as np
import matplotlib.pyplot as plt


def fnc(c):
    g = 9.81 
    m = 68.1
    t = 10.0
    v = 40.0
    val = g*m/c * (1-np.exp(-c*t/m)) - v
    return val 


def bisection(g1,g2):
    if fnc(g1) * fnc(g2) > 0 :
        print("Provide better guess")
    elif fnc(g1) * fnc(g2) == 0 :
         return g1 
     else :
         cr = (g1+g2)/2
         



# Preliminary inspection by graph

cg = np.linspace(1.0,100,101)
fg = np.zeros(len(cg))

for i in range(len(cg)):
    fg[i] = fnc(cg[i])

plt.figure()
plt.plot(cg,fg,'-k')
#plt.show()

# Root lies b/w c = 1, 20

cig = [1,20]

if fnc(cig[0])*fnc(cig[1]) > 0 :
   print("Please provide a better guess")
   else:
       cr = (cig[0] + cig[1] )/2
