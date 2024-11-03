#open file as read and split its contents 

rep = []
my_file = open("C:/Users/Braya/Downloads/rosalind_ini2 (3).txt","r") 
a = my_file.read().split(' ')   

#looping through file and removing \n character 
for i in a: 
    rep.append(i.replace("\n",""))

a = rep[0] 
b = rep[1] 

result = int(a)**2 + int(b)**2 
print(result) 