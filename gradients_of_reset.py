import numpy as np
i = 0
for k in range(1,2):
    print("opened file " + str(k))
    with open("/home/bramley/Desktop/xspress5/fe250khz_resets/data_output" + str(k)+ ".txt", "r") as input1:
	q = []
	x = []
	grad=[]
        for line2 in input1:
    	    
	    
		if int(line2)>10:		
                    print(line2)
		    q.append( int(line2) )
		    print(q)
		    x.append(q[len(q)-1]-q[len(q)-2])
                    print(x)

		    if (len(q)==10):
		        gradient=sum(x)/10
			with open("/home/bramley/Desktop/xspress5/gradients.txt","a") as output:
			    output.write(str(gradient) + "  " + str(q[9]) + "\n")
			grad.append(gradient)
			del q[0:10]
			del x[0:10]

    max_val=max(grad)
    print(max_val)
    bins=np.arange(0,max_val,10)


    data=zip(*np.histogram(grad,bins))
    print(data)
    np.savetxt('test.txt', data,fmt='%1.3f', delimiter = " " ,newline = "\n")


	       
	    
	

		        
			    
