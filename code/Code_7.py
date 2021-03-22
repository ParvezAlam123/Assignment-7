import numpy as np
import matplotlib.pyplot as plt

#theortical result
P_A=1/2
P_B=1/2
P_AB=1/6
X_1=np.random.binomial(1,0.5,1000)
X_2=np.random.binomial(1,0.5,1000)
c=0
for i in range(1000):
    if X_1[i]==1:
        c=c+1
    
P_X_1=c/1000
c=0
for i in range(1000):
    if X_2[i]==1:
        c=c+1
P_X_2=c/1000
c=0
for i in range(1000):
    if X_1[i]==1 and X_2[i]==1:
        c=c+1
P_X1X2=c/1000
X=[1]
plt.scatter(X,P_A,color='green', label='theortical result')
plt.scatter(X,P_X_1,color='red',label='experimental result')
plt.legend()
plt.xlabel('X_1')
plt.ylabel('P(A)')
plt.title('Simulation of P(A)')
plt.show()

plt.scatter(X,P_B,color='green',label='theortical result')
plt.scatter(X,P_X_2,color='red',label='experimental result')
plt.legend()
plt.xlabel('X_2')
plt.ylabel('P(B)')
plt.title('Simulation of P(B)')
plt.show()

plt.scatter(X,P_AB,color='green',label='theortical result')
plt.scatter(X,P_X1X2,color='red',label='experimental result')
plt.legend()
plt.xlabel('X_ intersection X_2')
plt.ylabel('P(A intersection B)')
plt.titile('Simulation of P(A intersection B)')
plt.show()

       

