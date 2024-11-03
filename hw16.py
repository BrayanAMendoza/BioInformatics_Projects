file = open("C:/Users/Braya/Downloads/rosalind_ba3d (2).txt",'r')

num = file.readline()
seq = file.readline()

m = {}
length_of_string = len(seq)

left = 0 
right = 4-1
left_se = ''
right_se = ''

while right < length_of_string:
    left_se = seq[left:right]
    left +=1
    right +=1

    right_se = seq[left:right]

    if left_se not in m:
        m[left_se] = right_se
    
    else:
        m[left_se] += ',' + right_se

for key,value in enumerate(m):
    print(value + " ->" + m[value])