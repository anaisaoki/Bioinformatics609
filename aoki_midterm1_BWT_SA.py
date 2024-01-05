
file = open("referencegenome.fasta", "r")
sequence=""
for line in file:
    if line[0]=='>':
        sequenceid=line[0:].strip() #need to skip seq id line
    else:
        sequence+=line.strip()
        print(file.read())

#Burrow-Wheeler Transform
#Generate suffix array, each letter rotates from last to first 
seq_string = sequence + "$"
input = seq_string
table=[input[i:]+input[:i] for i in range(len(input))]
print('table=', table)

#Next, the list is sorted alphabetically
table= sorted(table)
print('sorted table =', table)

#BWT is the letters in the last column, extracting last column
last_column=[row[-1:] for row in table]
bwt = ''.join(last_column)
print(bwt)
   
#Generating Suffix Array
s=seq_string
suffix_array = [t[1] for t in sorted((s[i:],i) for i in range(len(s)))]

print(suffix_array)


