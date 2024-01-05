#biopython code

from Bio import SeqIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



with open("qscores.txt","w") as f:
    base_quality=[]
    for record in SeqIO.parse("assignment1.fastq","fastq"):
        qscores=record.letter_annotations["phred_quality"]
        base_quality.append(qscores)
    df=pd.DataFrame(base_quality)
    #print(df.head)
    print(df.mean(0))
    fig, ax=plt.subplots(figsize=(12,5))
    df.mean(0).plot(ax=ax, c="black")
    df.plot
    plt.show()



