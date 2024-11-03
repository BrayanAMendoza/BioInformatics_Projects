comp = "" #composition read from the file 
c = "" #counter
gpath_content = "" #Will hold the complete gpath content  
switch = True 

with open("C:/Users/Braya/Downloads/rosalind_ba3b (8).txt", 'r') as file: 
    comp = file.readlines() 
    comp = [x.strip() for x in comp] #strip comp of unwanted chars

for i in comp: 
    if switch: 
        gpath_content = i 
        switch = False   
        continue  
    c = i #update char string  
    c = c[-1:]  
    gpath_content += c #append current char to gpath

print(gpath_content) #returns gpath_content which is the kmer string seqeucne 

