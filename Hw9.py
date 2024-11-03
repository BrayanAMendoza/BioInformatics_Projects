my_file = open("C:/Users/Braya/Downloads/rosalind_revc.txt",'r') 
dna = my_file.read()
dna_as_list = dna.replace('\n',' ').split()
dna_sequence = ''.join(dna_as_list)

#1-4 Just opening the textfile, taking out the newline character, splitting it, and converting it into a string 


#The rc (reverse complement) first takes in a sequence, then reverses the given sequence 
#Next using the complements that I've defined within the function as a diciontary the sequence finds the correspodning complements
def r_c(sequence):
    complements = {"A":"T", "C":"G","T":"A","G":"C"}
    dna_seq = reversed(sequence)
    dna_seq = [complements[i] for i in dna_seq]

    return ''.join(dna_seq) 




print(r_c(dna_sequence)) #Calls the reverse complement function and passes dna_sequence which is the file we've read above. 