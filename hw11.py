
#Lines 6-15 simply opening the file, reading it, splitting it by newline character 
#Meaning that I'm converting it into a list with index 0 and 1. Where index 0 is the first line, and index 1 is the second line 
#Next I set a = first line and b = second line. After this I convert both A and B into a string 

my_file = open("C:/Users/Braya/Downloads/rosalind_hamm (1).txt",'r') 
dna = my_file.read()
dna_content_list = dna.split("\n")

a = dna_content_list[0]
b = dna_content_list[1]


dna_sequence1 = ''.join(a)
dna_sequence2 = ''.join(b)


count = 0 #intializing count to 0

for i in range(0,len(dna_sequence1)): #for loop that is from 0 to the length of a which is the first line of dna 
    if dna_sequence1[i] != dna_sequence2[i]: #if sttement that checks if the index from a and b are not equal to each other
        count += 1 #In which case the counter goes up by 1 everytime this if statement is true 

print(count) #Simply returns the count as an integer. 