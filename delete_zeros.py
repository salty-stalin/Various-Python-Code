with open("/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe1100khz_std.txt", "r") as input:
    with open("/home/xspress3/Desktop/xspress5_final/Results/fe1100khz/fe1100khz_std.txt2", "w") as output: 
        for line in input:
            if line.strip("\n") != "#VALUE!":
                output.write(line)
