 
  

import os 
  

def main(): 
    i = 0
      
    for filename in os.listdir("/home/xspress3/Desktop/data/fe noise/fe noise with 0s 38,000/"): 
        dst ="fe_noise" + str(i) + ".txt" #file name
        src ='/home/xspress3/Desktop/data/fe noise/fe noise with 0s 38,000/'+ filename #source
        dst ='/home/xspress3/Desktop/data/fe noise/fe noise with 0s 38,000/'+ dst #target
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst)
        i += 1
  

if __name__ == '__main__': 
      
    
    main() 

