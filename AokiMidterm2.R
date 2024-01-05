library(ggplot2)
library(dplyr)

#Simulating genotypic frequencies at a single bi-allelic locus (A&G)
# in an inbreeding population
#Plot inbreeding frequency over 50 generations

#Starting allele frequency of the A allele is 0.2
AA=NULL
x=c(1,1,0,0,0,0,0,0,0,0)

#Starting population size is 1000 
N <- 1000 #1000 individuals, each individual is diploid --> 2*N

F <- 0.2 #population inbreeding rate

p=sum(x)/1000
q=1-p

gen_list=c()

for (i in 1:50) { #for loop over 50 generations
  gen_list=append(gen_list,x)
  df <- gen                     
  gen=sample(x,2*N,replace=TRUE, prob=NULL) 
  AA <- c(AA,sum(x)/N)
  print(gen)

  AA=(p^2+p*q*F) #changing genotype frequencies due to inbreeding
  print(AA)
  GG=(q^2+p*q*F)
  print(GG)
  AG=(2*p*q)*(1-F)
  print(AG)
}

gen = c(1:51) 
graph= data.frame(AA,gen)
ggplot(data=df, aes(x=gen,y=N))+ geom_line()

