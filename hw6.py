my_file = open("C:/Users/Braya/Downloads/rosalind_ini6 (3).txt","r") #opening file 
a = my_file.read().split(' ') #reading the file and spliting it by spaces 

w_count = {} #creates a dictionary to keep word count 

for i in a: #for loop that goes through broken/split up file and 
    if i in w_count: #checks if word is already in the word count, if so it adds one to how many times its been repeated 
        w_count[i] += 1
    else:
        w_count[i] = 1 #otherwise leaves the word count as is. 



for key, value in w_count.items(): #gets and prints out the key and value pair found in w_count dictionary. 
    print(key, value)
