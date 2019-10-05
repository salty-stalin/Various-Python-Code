import numpy as np
import matplotlib.pyplot as plt

f=open("/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe11khz_energies.txt","r")
f1=f.readlines()
values=[]
prob=[]
for x in f1:
	
	inter=float(x)
	values.append(inter)
max_val=1000
print(max_val)
bins=np.arange(0,max_val,0.5)
hist, bin_edges = np.histogram(values,bins)
hist=np.append(hist,[0])
#print(np.histogram(values,bins))

data=zip(*np.histogram(values,bins))
plt.plot(bins, hist)
plt.show()
#np.savetxt("/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe1100khz_histogram_0.5bins.txt", data,fmt='%1.3f', delimiter = " " ,newline = "\n")
