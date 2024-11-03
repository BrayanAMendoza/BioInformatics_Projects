file = open("C:/Users/Braya/Downloads/rosalind_ba3c (2).txt",'r') 
d = {} 

content = file.read().strip().split() 

content.sort() 
k = len(content[0]) 
#Embeded loops so as to traverse the contents/kmers inside content 
for i in content: 
    for j in content:
        prefix = i[1:k] #set prefix to be the index of i from 1 to k (calcualted above)
        suffix = j[0:k-1] #set suffix to be the index of j from 0 to k-1

        if suffix == prefix: #checking to see if they are equal 
            d[i] = '-> ' + j + '' #if so then we apply the following format 

for key,value in d.items():  
    print(key,value) 

