#================================================
# Bracketing Method - 01 Bisection method 
#================================================


import numpy as np
import matplotlib.pyplot as plt
import copy 

def fnc(c):   #<----------- Edit the funcn as per reqmnts
    g = 9.81 
    m = 68.1
    t = 10.0
    v = 40.0
    val = g*m/c * (1-np.exp(-c*t/m)) - v
    return val 


def bisection(g1,g2):
    
    eps =  1E-11 #<-------------------Edit here
    if fnc(g1)* fnc(g2) < 0 :
    
     if np.abs(g1-g2) < eps :
         return g1 

     while np.abs(g1-g2) > eps :

      cr = (g1+g2)/2

      if fnc(g1) * fnc(cr) > 0 : 
         #print("g2",g2,"\t cr",cr,"\n")
         return  bisection(cr,g2)

      else :
        #print("g1",g1,"\t cr",cr,"\n")
         return bisection(g1,cr)
      

    else :
      print("Provide better initial guess")




# Preliminary inspection by graph 
# Uncomment the following line for new test cases and plugin the values

#cg = np.linspace(1.0,100,101) <----------- Edit here
#fg = np.zeros(len(cg))

#for i in range(len(cg)):
#    fg[i] = fnc(cg[i])

#plt.figure()
#plt.plot(cg,fg,'-k')
#plt.show()

# Observed from graph that root lies b/w c = 1, 20

cig = [1,20]  #<---------------Edit here

root = bisection(cig[0],cig[1])

print("\n The root is ",root) 

