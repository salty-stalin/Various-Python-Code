with open("output_energy.out", "r") as input:
    with open("energies output.txt", "w") as output: 
        for line in input:
            if line.strip("\n") >= "0" :
                output.write(line)
