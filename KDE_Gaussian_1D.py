from scipy import stats
import matplotlib.pyplot as plt

import numpy as np

f=open("/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe11khz_energies.txt","r")
f1=f.readlines()
values=[]

for x in f1:
	
	inter=float(x)
	values.append(inter)





kernel = stats.gaussian_kde(values,bw_method=0.05) #select bandwith
x = np.linspace(0, 1000, num= 5000) #x- values
kde_pdf = kernel.evaluate(x)
data=zip(*(x,kde_pdf))
plt.plot(x, kde_pdf)
plt.show()








#print(data)
np.savetxt('/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe1100khz_kde_0.05.txt', data,fmt='%1.3f', delimiter = " " ,newline = "\n")




