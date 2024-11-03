
file = open("C:/Users/Braya/Downloads/rosalind_ba3a (5).txt",'r') 
a = int(file.readline()) 
b = file.readline() 

def kmer_comp (size, string): #passing in size and the string composition 
	
	u_Kmers = [] #instantiate list -- used to append kmer composition in 

	#loop through the elgnth of string composition minus the given size 
	for i in range (len(string) - size + 1 ): 
		u_Kmers.append (string [i : i+size]) #everytime we append n characters into our list, where n is the same as the size given to us in the txt file 
	return u_Kmers #Return updated kmers list 



for i in (kmer_comp(a,b)): #loop that goes through the list created in my function kmper composition 
	print(i) #prints out each item in the list. 

