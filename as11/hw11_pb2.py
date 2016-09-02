# -*- coding: utf-8 -*-
"""
"""
import os.path
import math
import matplotlib.pyplot as plt
import numpy as np
plt.close("all")


def derivative_descent(x_ini, f, der_f, step, eps):
    if abs(der_f(x_ini)) > eps:
        return [x_ini] + derivative_descent(x_ini-step*der_f(x_ini),f,der_f,step,eps)
    else:
        return [x_ini]


def newton_method(x_ini, f, der_f, der2_f, eps):
    if abs(der_f(x_ini)) > eps:
        return [x_ini] + newton_method(x_ini- (der_f(x_ini)/der2_f(x_ini)),f, der_f, der2_f, eps)
    else:
        return [x_ini]  
    
def quadratic_approx(x, point, f, df, d2f):
    return f(point)+df(point)*(x- point) +0.5*d2f(point)*(x-point)**2


def trajectory(x,f):
    n = len(x)
    res = np.zeros((2, n*2 - 1))
    for i in range(n-1):
        res[0, 2*i] = x[i]
        res[0, 2*i+1] = x[i+1]
        res[1, 2*i:(2*i+2)] = f(x[i])
    res[0,2*n-2] = x[-1]
    res[1,2*n-2] = f(x[-1])
    return res
    
eps = 10**(-4)   
x_min = -2.
x_max = 2.
x = np.arange(x_min,x_max,1e-2)
f =lambda y: (1-np.exp(-y)) * y 
df =lambda y: (1-np.exp(-y)) + y * np.exp(-y)
d2f =lambda y: (2 -y) * np.exp(-y)

step = 0.2
x_ini = -1.8
sol_der_desc = np.array(derivative_descent(x_ini, f, df, step, eps))
plt.figure(figsize=(12, 9))  
plt.plot(x,f(x),lw=3)
traj = trajectory(sol_der_desc,f)
plt.plot(sol_der_desc, f(sol_der_desc), 'o', c="darkred",lw=3, markersize=10)
plt.plot(traj[0,:],traj[1,:],'--',c='darkred',lw=3)
plt.savefig('1.png')

step = 0.05
x_ini = -1.8
sol_der_desc = np.array(derivative_descent(x_ini, f, df, step, eps))
plt.figure(figsize=(12, 9))  
plt.plot(x,f(x),lw=3)
traj = trajectory(sol_der_desc,f)
plt.plot(sol_der_desc, f(sol_der_desc), 'o', c="darkred",lw=3, markersize=10)
plt.plot(traj[0,:],traj[1,:],'--',c='darkred',lw=3)
plt.savefig('2.png')


newton_sol = np.array(newton_method(x_ini, f, df, d2f, eps))
plt.figure(figsize=(12, 9))  
plt.plot(x,f(x),lw=3)
traj = trajectory(newton_sol,f)
plt.plot(newton_sol, f(newton_sol), 'o', c="darkred",lw=3, markersize=10)
plt.plot(traj[0,:],traj[1,:],'--',c='darkred',lw=3)
plt.ylim([-0.5,12])
plt.savefig('3.png')

plt.figure(figsize=(12, 9))  
plt.plot(x,f(x),lw=3)
traj = trajectory(newton_sol,f)
plt.plot(newton_sol, f(newton_sol), 'o', c="darkred",lw=3, markersize=10)
plt.plot(traj[0,:],traj[1,:],'--',c='darkred',lw=3)
plt.ylim([-0.5,12])
plt.plot(x,quadratic_approx(x, newton_sol[0], f, df, d2f), "--",c="red",lw=3,label="Quadratic approximation")
for i in range(1,4):
    plt.plot(x,quadratic_approx(x, newton_sol[i], f, df, d2f), "--",c="red",lw=3)
plt.ylim([-0.5,12])
plt.legend(fontsize=20,loc="upper right")
plt.savefig('4.png')