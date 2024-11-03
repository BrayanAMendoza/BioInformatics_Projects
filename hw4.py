my_file = open("C:/Users/Braya/Downloads/rosalind_ini4 (2).txt","r") 
a = my_file.read().split(' ') 
rep = [] #creating a replacement list

#loop through file and remove newline char 
for i in a: 
    rep.append(i.replace("\n",""))
    
(list(rep)) 


start = int(rep[0]) #sets the start as index 0 of repalcement list 
end = int(rep[1]) #sets the end as index 1 of replacement list 
result = 0

for x in range(start, end + 1): #loop from start to end and checks if number is odd 
    if x % 2 != 0:
        result += x #sums up all odd numbers/ints 

print(result) #prints final output 


