my_dictionary = {}
file = open("C:/Users/Braya/Downloads/rosalind_gc (4).txt",'r')
my_file = file.read().split()

#lines above are simply intializing a dictionary and sequence. Next I open the file and read it 

for entry in my_file: #this for loop checks for '>' and if it finds it then we replace it with an empty space 
    if entry[0] == '>':
        seq_name = entry.replace('>','')
        seq = ""
    else:
        seq += entry #increase sequence with entry 
    my_dictionary[seq_name] = seq #next we add the ith content to my_dictionary 

cg_dictionary = {}
#again initalizing cg dictionary and nucleotides.  

for name, seq in my_dictionary.items(): #for loop that places cg_contents into cg_dictionary throughout the items in my_dictionary     
    cg_nucleotide = 0
    nucleotide_count = len(seq)

    for letter in seq: #for loop checks for G and C and if there is a match the cg_nucleotide increases by one everytime 
        if letter == 'G':
            cg_nucleotide += 1

        elif letter == 'C':
            cg_nucleotide += 1 
    
        cg_contents = (cg_nucleotide/nucleotide_count)*100 
        cg_dictionary[name] = cg_contents 



max_name = ''
max_value = 0
#initalizing max_name and max_value 

for name, value in cg_dictionary.items(): #for loop that checks if value > max_value if so then this value will be set to the new max_value.
    
    if value > max_value: 
        max_value = value
        max_name = name


        
print(max_name)
print(max_value)




