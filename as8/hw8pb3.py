import numpy as np
import matplotlib.pyplot as plt
import os.path

plt.close("all")
 
data = np.load("heart_disease_data.npz") 


# Function that outputs the position of x that contain val
def ind_x_eq_val(x, val):
    return np.where(x==val)[0]


# Function that counts the number of entries equal to val in x
def count_x_eq_val(x, val):
    return len(ind_x_eq_val(x, val))/float(len(x))
    

# Function that computes a Gaussian pdf with mean mu and std sig at the values in x
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / sig / np.sqrt(2 * np.pi)


# Estimate the pmf of H
P_H0 = count_x_eq_val(data["heart_disease"],0)
P_H1 =count_x_eq_val(data["heart_disease"],1)

# Estimate the conditional pmf of S given H
P_S_H0 = np.zeros(2)
P_S_H1 = np.zeros(2)
for ind_S in range(2):
    P_S_H0[ind_S] = np.sum(((data["heart_disease"]==0) * (data["sex"]==ind_S))==1) / float(sum(data["heart_disease"]==0))
    P_S_H1[ind_S] = np.sum(((data["heart_disease"]==1) * (data["sex"]==ind_S))==1) / float(sum(data["heart_disease"]==1))

# Estimate the conditional pmf of C given H
P_C_H0 = np.zeros(4)
P_C_H1 = np.zeros(4)
for ind_C in range(4):
    P_C_H0[ind_C] = np.sum(((data["heart_disease"]==0) * (data["chest_pain"]==ind_C))==1) / float(sum(data["heart_disease"]==0))
    P_C_H1[ind_C] = np.sum(((data["heart_disease"]==1) * (data["chest_pain"]==ind_C))==1) / float(sum(data["heart_disease"]==1))

# MAP estimate

temp = np.transpose(np.vstack((P_S_H0[data['sex_test'].astype(int)]*P_C_H0[data['chest_pain_test'].astype(int)]
                               *P_H0,P_S_H1[data['sex_test'].astype(int)]*P_C_H1[data['chest_pain_test'].astype(int)]*P_H1)))
MAP_estimate_S_C = np.zeros(len(temp[:,1]))
for i,j in enumerate(temp):
    MAP_estimate_S_C[i] = 0 if j[0]>j[1] else 1 
                     
    


error_rate_S_C = np.sum(MAP_estimate_S_C!=data['heart_disease_test'])/float(len(data['heart_disease_test']))

print "Probability of error " + str(error_rate_S_C)

## Estimate conditional pdf of X given H
mean_X_H = np.zeros(2)
std_X_H = np.zeros(2)
mean_X_H[0]= np.mean(data['cholesterol'][np.where(data['heart_disease']==0)])
std_X_H[0] =  np.std(data['cholesterol'][np.where(data['heart_disease']==0)])
mean_X_H[1]= np.mean(data['cholesterol'][np.where(data['heart_disease']==1)])
std_X_H[1] =np.std(data['cholesterol'][np.where(data['heart_disease']==1)])

n_plot = 100
for i in range(2):
    plt.figure(figsize=(12, 9))  
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left() 
    yticks = ax.yaxis.get_major_ticks()
    yticks[0].label1.set_visible(False) 
    plt.xticks(fontsize=22) 
    plt.yticks(fontsize=22) 
    plt.xlabel("Cholesterol", fontsize=22)  
    plt.hist(data['cholesterol'][np.where(data['heart_disease']==i)],
             60,normed=True,edgecolor = "none", color="skyblue")
    plt.plot(np.linspace(50, 450, n_plot),gaussian(np.linspace(50, 450, n_plot), 
                     mean_X_H[i], std_X_H[i]), color="darkred", lw=2)
                 

# MAP estimate
temp1 = np.transpose(np.vstack((P_S_H0[data['sex_test'].astype(int)]*P_C_H0[data['chest_pain_test'].astype(int)]*P_H0*gaussian(data['cholesterol_test'], mean_X_H[0], std_X_H[0]),
                                P_S_H1[data['sex_test'].astype(int)]*P_C_H1[data['chest_pain_test'].astype(int)]*P_H1*gaussian(data['cholesterol_test'], mean_X_H[1], std_X_H[1]))))
MAP_estimate_S_C_X = np.zeros(len(temp1[:,1]))
for i,j in enumerate(temp1):
    MAP_estimate_S_C_X[i] = 0 if j[0]>j[1] else 1 
    
error_rate_S_C_X = np.sum(MAP_estimate_S_C_X!=data['heart_disease_test'])/float(len(data['heart_disease_test']))
print "Probability of error using cholesterol " + str(error_rate_S_C_X)
