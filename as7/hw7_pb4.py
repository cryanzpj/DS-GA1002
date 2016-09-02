import numpy as np
import matplotlib.pyplot as plt
import os.path

plt.close("all")
### CHANGE PATH TO WHEREVER YOU SAVE THE DATA FILES ### 
men_chol = np.loadtxt("cholesterol_men.txt", delimiter=',') 
women_chol = np.loadtxt("cholesterol_women.txt", delimiter=',') 

def run_permutation_test_mean(data, n1, n2):
    res = []
    for i in xrange(100000):
        permute = np.random.permutation(data)
        res.append(np.mean(permute[:n1]) - np.mean(permute[n1:]))
    return res
    
def run_permutation_test_median(data, n1, n2):
    res = []
    for i in xrange(100000):
        permute = np.random.permutation(data)
        res.append(np.median(permute[:n1]) - np.median(permute[n1:]))
    return res

def compute_p_value(res, val):
    return sum(np.array(res) >= val)*1.0/len(res)


test_statistic_mean = np.mean(men_chol) - np.mean(women_chol)
test_statistic_median = np.median(men_chol) - np.median(women_chol)
data = np.hstack((men_chol,women_chol))

print "Difference in sample mean is " + str(test_statistic_mean)
print "Difference in sample median is " + str(test_statistic_median)

tries = 3
n = 100000
for i_try in range(tries):
    res_mean = run_permutation_test_mean(data, len(men_chol), len(women_chol))
    res_median = run_permutation_test_median(data, len(men_chol), len(women_chol))
    p_value_mean = compute_p_value(res_mean, test_statistic_mean)
    p_value_median = compute_p_value(res_median, test_statistic_median)
    print "p value for difference in sample mean is " + str(p_value_mean)
    print "p value for difference in sample median is " + str(p_value_median)
    plt.figure(figsize=(12, 9))  
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["right"].set_visible(False)   
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  
    plt.xticks(fontsize=22) 
    plt.yticks(fontsize=22) 
    plt.xlim([-25,25])
    plt.ylim([0,0.075])
    ax.set_xticks([-20, -10, 0, 10, test_statistic_mean])
    # plt.xlabel("Mean(men) - mean(woem)", fontsize=20)      
    plt.hist(res_mean,100,normed=True,edgecolor = "none", color="skyblue", label='Approximate pdf under null hypothesis')
    plt.plot([test_statistic_mean, test_statistic_mean],[0, 0.075],ls="dashed", color="darkred", lw=2)
    plt.title("Difference in sample mean")
    
    plt.figure(figsize=(12, 9))  
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["right"].set_visible(False)   
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  
    plt.xticks(fontsize=22) 
    plt.yticks(fontsize=22) 
    plt.xlim([-25,25])
    #plt.ylim([0,0.075])
    ax.set_xticks([-20, -10, 0, 10, test_statistic_median])
    # plt.xlabel("Mean(men) - mean(woem)", fontsize=20)      
    plt.hist(res_median,100,normed=True,edgecolor = "none", color="skyblue", label='Approximate pdf under null hypothesis')
    plt.plot([test_statistic_median, test_statistic_median],[0, 0.11],ls="dashed", color="darkred", lw=2)    
    plt.title("Difference in sample median")
