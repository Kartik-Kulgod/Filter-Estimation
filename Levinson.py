import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

tps = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]; # A sample time frame
h = np.array([math.sin(t) for t in tps])/np.array(tps);# the impulse response
x = np.random.randn(1,300);# Input white signal
otpt = signal.lfilter(h,1,x);# Output
N = len(h);
u = 0;
t = [];
y = [];
while(u<N):
	t.append(float(np.matrix(np.hstack((x,np.zeros((1,u))))) * np.matrix(np.vstack((np.zeros((u,1)),x.transpose())))));
	y.append(float(np.matrix(np.hstack((otpt,np.zeros((1,u))))) * np.matrix(np.vstack((np.zeros((u,1)),x.transpose())))));
	u = u + 1;

print(t)


#t = [3,2,1]; # The auto correlation matrix
#y = [1,2,2.5]; #The cross-correlation matrix
f = [[0]]; # The forward vector
b = [[0]]; # The backward vector
f.append([1/t[0]]); # The starting value
b.append([1/t[0]]); # The starting value
lt = len(t);
ef = np.zeros(lt+1);
eb = np.zeros(lt+1);
n = 2;
while(n<=lt):
	ef[n] = np.matrix(t[n-1:0:-1])*np.matrix(f[n-1]);
	eb[n] = np.matrix(t[1:n:1])*np.matrix(b[n-1]);
	f_temp = (1/(1 - eb[n]*ef[n]))*np.vstack((f[n-1],0)) - (ef[n]/(1-ef[n]*eb[n]))*np.vstack((0,b[n-1]));
	f.append(f_temp);
	b_temp = (1/(1 - eb[n]*ef[n]))*np.vstack((0,b[n-1])) - (eb[n]/(1-ef[n]*eb[n]))*np.vstack((f[n-1],0));
	b.append(b_temp);
	n = n+1;

#print(b)

from scipy.linalg import toeplitz

T = toeplitz(t);
hest = [y[0]/T[0][0]];
#print(x)

n=2;
while(n<=lt):
	temp1 = np.matrix(T[n-1][0:n:1])
	temp2 = np.matrix(np.vstack((hest,0)));
	ex = temp1*temp2
	hest = float(y[n-1] - ex)*np.array(b[n]) + np.vstack((hest,0));
	n = n+1;

#print(hest)

plt.plot(tps,h,'o',tps,hest,'x')
plt.show()