import time
i = 0
for k in range(1,2):
        print("opened file " + str(k))
        with open("/home/xspress3/Desktop/C++ code/fe_250khz" + str(k)+ ".txt", "r") as input1:
            
                count=6000
                count1=600
                q1=[] 
                x1=[] 
                q=[]
                x=[]
		thresholds=[]
                gradients=[]
                value=[]
                all_values=[]
                threshold=6100
                loops =0
                reset_full = False



                last_line = None
                
                for line2 in input1: 
                        if reset_full==False:
                                q1.append(int(line2))
                                count1=count1+1

				x1.append(q1[len(q1)-1]-q1[len(q1)-2])
			
				if last_line != None:
					line1 = last_line
			   		print(line2 + line1 + "Difference " +str(int(line2) -int(line1)))
				   	if ((int(line2) -int(line1))<-40 and count1 > 500):
						loops = loops +1
						reset_full = True
						count=0
					"""	if loops==1:
						    	print("first loop delete lists")
							del all_values[:]
                                                    	all_values=[]
							del gradients[:]
                                                 	gradients=[]
					                del value[:]
							value=[]
                                                        reset_full=False
							print(all_values)"""
					if (int(line2) -int(line1))<-40:
	                			print("start of reset")


					else:
						all_values.append(line2)
						print("appending " + line2)
				if (len(q1)==30):
					gradient1=sum(x1)/30
					gradients.append(gradient1)
					value.append(q1[29])
					del q1[0:29]
					del x1[0:29]
					q1=[]
					x1=[]
				else:
					all_values.append(line2)
				last_line = line2
					
				
			elif reset_full==True:
				print(gradients)
                                pos=-1
                                for i in gradients:
                                        pos = pos +1
					print("gradients is :" + str(i))
                                        if -10 <i < 10:
                                                threshold =value[pos]
						
						print ("thresholds is " + str(threshold))
						break
						time.sleep(10)

				for line3 in all_values:
					
		                        with open("data_output_test" + str(i) + ".txt","a") as output:
						count= count+1
						if int(line3)>0:		
							print(line3)
							q.append( int(line3) )
							print(q)
							x.append(q[len(q)-1]-q[len(q)-2])
							print(x)

							if (len(q)==10):
								gradient=sum(x)/10


								if gradient < -40 and count > 5000:
									print("end of reset") 
									print(q)
									print("difference: ")
									print(x)
									print("average: " + str(gradient))
									
									del q[0:10]
									del x[0:10]
									q=[]
									x=[]
									print("create new file ")
									time.sleep(10)

					
									i=i+1
									count=0
									

									del all_values[:]
                                                    			all_values=[]
									del gradients[:]
                                                		 	gradients=[]
					                		del value[:]
									value=[]
									reset_full= False
									break
									

								elif gradient < -40:
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

									
								elif q[0] < threshold:
									print("below threshold")
									del q[0:10]
									del x[0:10]
									q=[]
									x=[]
										


								else:
									a=str(q.pop(0))
									print("writing to file: "+str(a))
									print("difference: ")
									print(x)
									del x[0]
									output.write(a + "\n")
										

				
						


		    	
