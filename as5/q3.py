
import os.path
import math
import matplotlib.pyplot as plt
import numpy as np
import urllib2
data1 = np.loadtxt("radioactive_sample_1.txt")
data2 = np.loadtxt("radioactive_sample_2.txt")


def r_mean(data1):
    temp1 = 0
    res1 = []
    for i in xrange(0,len(data1)):
        temp1 += data1[i]
        res1.append(temp1/(i+1))
    return res1    
    
    
  
plt.plot(r_mean(data1))
plt.title('Running sample mean plot for sample 1 ') 
plt.show()

plt.plot(r_mean(data2))
plt.title('Running sample mean plot for sample 2') 
plt.show



np.random.seed(20)
sample1 = np.random.uniform(-np.pi/2,np.pi/2,10000)
x1 =  np.tan(sample1)

np.random.seed(40)
sample2 = np.random.uniform(-np.pi/2,np.pi/2,10000)
x2 =  np.tan(sample2)

np.random.seed(120)
sample3 = np.random.uniform(-np.pi/2,np.pi/2,10000)
x3 =  np.tan(sample3)

np.random.seed(220)
sample4 = np.random.uniform(-np.pi/2,np.pi/2,10000)
x4 =  np.tan(sample4)


plt.plot(r_mean(x1),'r')
plt.plot(r_mean(x2),'b')
plt.plot(r_mean(x3),'g')
plt.plot(r_mean(x4),'black')
plt.title('Running sample mean plot for samples from X')
plt.show()
