library(ggplot2)
library(dplyr)


#Simulating genetic drift under binomial sampling process 

#Starting allele frequency of one allele equal to 0.2
x=c(0,0,1,1,1,1,1,1,1,1)
allele_freqarray <- 0.2

#For Population Size N=10, set N=20 (10*2)
N <- 20
#You can vary population size -> N = 100 & 1000 

freqarray = NULL
freqarray <- 2:10

for (i in 1:100) { #for loop over 100 generations to sample with replacement
  new_gen=sample(x,N,replace=TRUE, prob=NULL) #randomly picks an allele (independent)
  replace(x, new_gen, values=count) #replaces the frequency after each generation. 
  freqarray <- c(freqarrary,sum(x)/N)
  print(new_gen)}

gen = c(1:101) #for 100 generations plus initial generation
graph= data.frame(freqarray,gen)
ggplot(data=new_gen, aes(x=gen,y=freqarray))
  + geom_line()

