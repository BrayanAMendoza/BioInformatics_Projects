
i = 1 #setting up my inital counter 
m_file = open("C:/Users/Braya/Downloads/rosalind_ini5 (1).txt","r") #opening local file as read format
for line in m_file.readlines(): #looping through the lines found in file 
    if i % 2 == 0: #condition that only returns even numbered lines 
        print(line.strip()) #prints line and removes "\n"

    i += 1 #everytime we loop the counter updates 









