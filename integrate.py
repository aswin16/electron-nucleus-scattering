import numpy as np
import matplotlib.pyplot as plt



def naivesimpson(f,a,b):
    
    m = (a+b)/2
    fa = f(a)
    fb = f(b)
    fm = f(m)
    integral = ((b-a)/6)*(fa +4*fm + fb)
    return integral



def simpsons(f,a,b):
    return ((b-a)/8)*(f(a) + 3*f((2*a + b)/3) + 3*f((a + 2*b)/3) + f(b))
    


def comp_simpsons(f,a,b,n):
    
    x = np.linspace(a,b,n)
    #fx = np.zeros(n)
    h = (b-a)/n
    sumthrees = 0
    sumtwos = 0
                                        
    for i in range(1,n-1):
        if i%3 == 0:                                                 
            sumtwos += 2*f(x[i])
                                                                                
        else:
                                                                                                            
            sumthrees +=    3*f(x[i])



                                                                                                                
    integral = (3*h/8)*(f(x[0]) + sumtwos + sumthrees + f(x[n-1]))

    return integral
                                                                                                                                        
                                                                                                                                                                                                                                                                            
                                                                                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                            
