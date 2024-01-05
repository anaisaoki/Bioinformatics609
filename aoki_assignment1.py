#Quality Scores from FASTq file

"""
#this code works to read only quality score lines
with open("assignment1.fastq")as f:
    lines=f.readlines()
    qualityscorelines=lines[3::4]
    print(qualityscorelines)
"""
"""
#looping array 
for qualityscores in f:
    print(qualityscores)
    
#another possible code
#array(data type,value list):

#use append to add value mentioned in its argument at the end of an array
"""
# --- Code begins here ----
import numpy as np


with open("assignment1.fastq")as f:
    for line in f.read().split("\n")[3::4]:
        for base in range(len(line)-1):
            print(ord(line[base])-33)





print('done')



    #qualityscorelist = [(line.strip()).split()for lines in f]
    #print(qualityscorelines)
#Counter variable
    #print(ord(qualityscorelines[[]])

#for value in range(41):
#    qscore=input()
#    value = ord(qscore)
#    print('The quality scores are' + str(value))
    
#print('done')
