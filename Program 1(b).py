from scipy.stats import binom
n=10
p=0.5
k=2
pro_suc=binom.pmf(k,n,p)
print("Probability of 2 success out of 10 ",pro_suc)
