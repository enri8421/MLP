from utilities import *
from allocation import *
from scipy import stats



P = [8,6,5,4,2]
N = [10001,10001,10001,10001,10001] #acrual N = N*5
n = 50
k = 401

g = 10000


seed(2)
result = 0
for i in range(g):
    State, size = sample_uniform(n,N)  
    a = compute("dhondt",size,k,verbose=False)
    result += simulate(n,k,P,a,State,size)


print("p value unifrom = ", stats.binom_test(result, g, p=0.5))

result = 0
for i in range(g):
    State, size = sample_gauss(n,N)  
    a = compute("dhondt",size,k,verbose=False)
    result += simulate(n,k,P,a,State,size)


print("p value gauss = ", stats.binom_test(result, g, p=0.5))


result = 0
for i in range(g):
    State, size = sample_pro(n,N,4)  
    a = compute("dhondt",size,k,verbose=False)
    result += simulate(n,k,P,a,State,size)


print("p value pro = ", stats.binom_test(result, g, p=0.5))
