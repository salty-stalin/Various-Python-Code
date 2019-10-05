i = 0
for k in range(0,1):
    print("opened file " + str(k))
    with open("/home/xspress3/Desktop/data/fe 250khz/fe250khz with 0s 100000/fe_250khz" + str(k) + ".txt", "r") as input1:

        last_line = None
        for line2 in input1:
    	
	    with open("/home/xspress3/Desktop/data/testcode/Python_code/format_data_output_250khz_verstion2/data_output" + str(i) + ".txt", "a") as output: 
	        if last_line != None:
	    	    line1 = last_line
	   	
	            print("line1: " +line1 + "line2: " + line2 + "difference: " + str((int(line2)-int(line1))))
	            if (int(line2) -int(line1))<-40:
	                print("start of reset")
	            elif int(line2) and int(line1) <10:
	                print("start of reset")
	            elif ((int(line2)-int(line1))>1000):
	                print("Create new file ")
	                i=i+1


                    else:
	                output.write(line2)
	            	#print("writing to file")
                else:
	            output.write(line2)
	        last_line = line2
