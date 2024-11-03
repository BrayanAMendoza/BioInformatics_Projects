#Open file read from it, remove new line character and split the file 
my_file = open("C:/Users/Braya/Downloads/rosalind_dna (2).txt",'r') 
dna = my_file.read()
dna_as_list = dna.replace('\n',' ').split()
#initialzie nucleotides count 
A = 0
C = 0
G = 0
T = 0
#loops through string given and counts the number of times each letter is present 
for i in dna_as_list:  
    if i == 'A':
        A += 1
    elif i == "T":
        T += 1
    elif i == "C":
        C += 1
    elif i=="G":
        G += 1

print(str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T))


my_file.close()