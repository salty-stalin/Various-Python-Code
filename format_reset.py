
i = 0
for k in range(0,1):
    print("opened file " + str(k))
    with open("/home/bramley/Desktop/xspress5/ketek_fe_250khz" + str(k)+ ".txt", "r") as input1:
	count=4000 #count so the decreasing gradient isnt taken as end of reset again
	threshold=6100 #begining of reset threshold for Fe55
	q = []
	x = []
        for line2 in input1:
    	    
	    with open("/home/bramley/Desktop/xspress5/fe250khz_resets/data_output" + str(i) + ".txt","a") as output:
		count= count+1
		if int(line2)>0:		
                    print(line2)
		    q.append( int(line2) ) #append values
		    print(q)
		    x.append(q[len(q)-1]-q[len(q)-2]) #append difference
                    print(x)

		    if (len(q)==10):  
		        gradient=sum(x)/10
		        gradient2=sum(x[0:2])/2
		        gradient4=sum(x[2:4])/2
		        gradient6=sum(x[4:6])/2
		        gradient10=sum(x[6:10])/10
		        if (gradient) < -40 and count > 5000: #reset bigins
			    print("end of reset ")
			    print("values: ")
			    print(q)
			    print("difference: ")
			    print(x)
			    print("average: " + str(gradient))
			    
			    del q[0:10]
			    del x[0:10]
			    q=[]
			    x=[]
		            print("create new file ")
			    
			    print("gradients")
			    print( str(gradient2) + " " + str(gradient4)+" "+ str(gradient6) +" "+ str(gradient10) )
			    i=i+1
			    count=0
		        elif (gradient) < -40:  #reset continues
			    print("end of reset ")
			    print("values: ")
			    print(q)
			    print("difference: ")
			    print(x)
			    print("average: " + str(gradient))
			    del q[0:10]
			    del x[0:10]
			    q=[]
			    x=[]			    
			elif q[0] < threshold: #below threshold
			    print("below threshold")
			    del q[0:10]
			    del x[0:10]
			    q=[]
			    x=[]
			    


		        else: 			#write to file
			    a=str(q.pop(0))
			    print("writing to file: "+a)
			    print("difference: ")
			    print(x)
			    del x[0]
			    output.write(a + "\n")
			    
