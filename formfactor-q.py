# electron-nucleus elastic scattering
# witten by Aswin
# 11 July 2020


#importing necessary packages
import numpy as np   #matrix manipulation
import scipy as sp   # scientific python
import matplotlib.pyplot as plt # visualization
from scipy.integrate import quad # integration
from scipy.special import expit
from integrate import comp_simpsons  #simpsons integration fn called from integrate.py file





#fundamental constants 
# in natural units

h_= 1 #hbar
e = 0.303 #charge of electron


#***fn to plot form factor vs momentum transfer**#

#function arguments
#Z - atomic number
#d - diffusiveness of surface
#A - mass number
#num - resolution
#q_lim - upper boundary for momentum transfer 'q'

def plot(num,Z,d,A,q_lim):
    
    R = 1.18*(A**(1/3)) #half value radius in fermi -approximate relation
    
    #normalization constant of 
    #Woods-Saxon charge distribution
    
    wSax = lambda r: (r**2)/(1+expit((r-R)/d)) 
    #wSax_integral,error = quad(wSax,0,np.inf)  #function call : quad - used for integration
    wSax_integral = comp_simpsons(wSax,0,10000000,1000)
    rho0 = Z/(4*np.pi*wSax_integral)  #normalization constant 
    
    
    #########################
    
    
    #plotting form factor vs momentum transfer
   
    #integral_quad = np.zeros(num)  # array of dimension 'num' initialized with 0
    integral_simp = np.zeros(num)
    
        
    Q = np.linspace(1,q_lim,num)   


    for i in range(num):
        
        
        q = Q[i]  # taking values of momentum transfer b/w 0 and q_lim
     
        #calculating fourier transform
        #of woods saxon distribution
    
    
        freal = lambda r :(1/Z*e)*np.cos(q*r/h_)*rho0*(1/(1+expit(r-R)/d))
    
        fimag = lambda r :1/(Z*e)*np.sin(q*r/h_)*rho0*(1/(1+expit((r-R)/d)))
        
        #integration using quad from scipy package
        
        #real_integral_quad,error_real = quad(freal,0,30)
        #imag_integral_quad,error_imag = quad(fimag,0,30)

        #integration using simpson
        
        real_integral_simp = comp_simpsons(freal,0,30,1000)
        imag_integral_simp = comp_simpsons(fimag,0,30,1000)
        
        #integral_quad[i] = 4*np.pi*np.sqrt(np.square(real_integral_quad)+np.square(imag_integral_quad))  # RHS is |F|
   
        integral_simp[i] = 4*np.pi*np.sqrt(np.square(real_integral_simp)+np.square(imag_integral_simp)) 
    
    q = np.linspace(0,q_lim,num)

    #plt.plot(q,integral_quad)    # momentum transfer vs form factor  ,integration done using quad
    
    plt.plot(q,integral_simp,'b')    # integration using simpsons
    

  
    
    
    
    




#print('enter the following')
#print('num- (resolution)divisons in plot(optimum around 50),Z,A,d-diffusiveness,qlim-upper bound on q')

#num = input("resolution: ")

#Z = input("Z: ")

#A = input("A: ")

#d = input("d: ")

#q_lim = input("q_lim: ")


plot(49,8,0.5,32,20)

#plot(int(num),int(Z),float(d),int(A),float(q_lim))

