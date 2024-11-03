motif = ''
file = open("C:/Users/Braya/Downloads/rosalind_subs (1).txt",'r')

#opening file and intializing motif 

sequence = file.readline().strip() 
sub_sequence = file.readline().strip()

#lines 6-7 reading both lines and then stripping them 

for i in range(len(sequence)): #for loop the length of sequence 
    a = sequence[i:i+len(sub_sequence)] #accessing the ith index of sequence 

    if a== sub_sequence: #checking to see if a is equal to the sub_sequence 
        
        motif = motif + str(i + 1) + ' '
 
print(motif) #printing motif 






