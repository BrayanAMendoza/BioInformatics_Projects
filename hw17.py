file = open("C:/Users/Braya/Downloads/rosalind_ba3e (10).txt","r")
mers = file.read().strip().split()  
graph = {} 

mers.sort()
k = len(mers[0]) 

for item in mers: #traverses through each item in mers 
    #setting/establishing prefix and suffix below 
    prefix = item[:k-1] 
    suffix = item[1:]

    if prefix not in graph: #checks if the prefix is not in the graph, if this is the case we add it to the graph dictionary with value being the suffix 
        graph[prefix] = '-> '  + suffix + ' '  
    else: #otherwise if the prefix is in the dictionary/graph and it reappears then we use concatnation to add it as another value in the dictionary
        graph[prefix] += ',' + suffix


for key, value in graph.items(): 
    print(key, value) 
