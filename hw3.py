#open file loop through and split each lien 

my_file = open("C:/Users/Braya/Downloads/rosalind_ini3 (5).txt","r") 
firstline = my_file.readline().rstrip(' ')
firstline.split()
#print the contents that we want using indices 
print(firstline[0:8] + " " + firstline[100:111]) 


