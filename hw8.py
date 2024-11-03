
my_file = open("C:/Users/Braya/Downloads/rosalind_rna (2).txt",'r') 
dna = my_file.read()
dna_as_list = dna.replace('\n',' ').split()
#lines 2-4 are simply opening the file,removing the newline character and split it 

dna_s = ''.join(dna_as_list) #i chance dna from list to a string 

def RNATrans(dna_s): #This function takes in dna as a string and simply replaces T with U 
    return dna_s.replace("T","U")


print(RNATrans(dna_s)) #Calls RNATRans function 