class Problem19: 
    def __init__(self, masses, AA_letters):
        peptide = "" #create empty peptide string 
        f = open("C:/Users/Braya/Downloads/rosalind_ba11d (8).txt", 'r') #Open file in read mode 
        counter = 0 #create couter and intialize it to 0
        data = f.readline().strip().split() #split the data file strip it of \n character and split it   

        massDict = self.AMMD(masses, AA_letters) #initializing massDict variable by calling Amino mass dictionary function, also passing masses and their letters as they are required in the AMMD function
        for i in data: #for loop that iterates each item in data list 
            if i == "1": #if the item is 1 then we use Amino dictionary for lookup and concatenate it to the peptide string variable 
                peptide += massDict[counter+1]
                counter = 0 #we then reset the counter to 0 
            else: #in the case that it is not a 1 then we don't concatenate anything to the peptide's variable and instead simply increment the counter 
                counter += 1 
        
        print(peptide) #after iterating through all the items inside our data list we print the string representation of the peptide 


    def AMMD(self, a , b): #Amino mass dictionary function that takes in two variables a and b representative of the number masses and actual letters of the amino acids 
        mass_weights = (a) #pass a and converts its contents to a tuple 
        Amino_acid_letters = list(b) #pass b and converts it into a list 
        mass = dict(zip(mass_weights, Amino_acid_letters)) #Creates dictionary using dict where key and values are the number masses and the actual letters for the amino acids 
        
        return mass #return the mass dictionary 

if __name__ == "__main__":
    #Line 31 and 32 are set values and strings representing the masses and amino acid letters used in the problem and textbook 
    masses = 57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186 
    AA_letters = "GASPVTCILNDKQEMHFRYW"
    Problem19(masses, AA_letters) #call problem19 class and pass the required fields 



