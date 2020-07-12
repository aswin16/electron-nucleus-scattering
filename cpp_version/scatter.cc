#include<iostream>
#include<cmath>


using namespace std;

const int h_ = 1;
const int e = 0.303;



/**** integration using simpsons***/
double integrate(double (*f)(double) ,double a,double b,int n){
    

    double x[n];
    
    double h = (b-a)/n;


    


    x[0] = a;
    x[n-1] = b;

    for(int i = 1; i < n-1; i++){

            x[i] = x[i-1] +h;


        }

    double sumthrees = 0;
    double sumtwos = 0;



    for(int j = 1;j<n;j++){

            if (j%3 ==0) sumtwos += 2*f(x[j]);
            else sumthrees += 3*f(x[j]);

        }


   

    double integral =  (3*h/8)*(f(x[0]) + sumtwos + sumthrees + f(x[n-1]));

        

    return integral;

}
/**********************/

double wood_sax(double x , int A, int Z, double d){

    double R;
   // double d =0.513;
   // int A = 32;
    R = 1.18*pow(A,1/3);
    return pow(x,2)/(1 + exp((x-R)/d));
    }

double norm_woodsax(int Z, int A,double d){

    double wsax_integral;
    double x;
    wsax_integral = integrate(wood_sax(x,A,Z,d),0,1000,100000);
    double rho0; 
    rho0= Z/(4*M_PI*wsax_integral);

    return rho0 ;
}


/**defining fourier transform**/
/**splitting into real and imaginary parts**/

double ftreal(double r,int Z, double rho0,double q,double R,double d){

    return (1/Z*e)*cos(q*r/h_)*rho0*(1/(1+exp(r-R)/d));

}

double ftimag(double r,int Z, double rho0,double q,double R,double d){

    return (1/Z*e)*cos(q*r/h_)*rho0*(1/(1+exp(r-R)/d));

    }

/*******************************************************/
    





int main(){
    cout << " input Z,d,qlimit,num,A " <<endl;

    int Z,num,qlim,A;
    double d,rho0;


    rho0 = norm_woodsax(Z,A,d);

    
    cout << rho0<<endl;


    //cout<< norm_woodsax(8);


    }
