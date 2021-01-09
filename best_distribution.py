from utilities import *
from allocation import *
from optimizer import *
import matplotlib.pyplot as plt


P = [8,6,5,4,2]
N = [10001,10001,10001,10001,10001] #acrual N = sum(N)
n = 50
k = 401

seed(2)


State, size = sample_pro(n,N,0)  
a = compute("dhondt",size,k,verbose=False)

g = 1000
result = 0
for i in range(g):
    result += simulate(n,k,P,a,State,size)


print("probability of victory = ",1- result/g)

new_State, new_size = find_best_distribution(State,n,a)
new_a = compute("dhondt",new_size,k,verbose=False)

result = 0
for i in range(g):
    result += simulate(n,k,P,new_a,new_State,new_size)

print("new probability of victory = ", 1-result/g)








N = [10001,10001,10001,10001,7501] #acrual N = sum(N)
State, size = sample_pro(n,N,0)  
a = compute("dhondt",size,k,verbose=False)


result = 0
for i in range(g):
    result += simulate(n,k,P,a,State,size)


print("probability of victory = ",1- result/g)

new_State, new_size = find_best_distribution(State,n,a)
new_a = compute("dhondt",new_size,k,verbose=False)

result = 0
for i in range(g):
    result += simulate(n,k,P,new_a,new_State,new_size)

print("new probability of victory = ", 1-result/g)

plt.bar(range(n), State[0] , label="Blue Bar", color='b')
plt.bar(range(n), State[4] , label="Blue Bar", color='r',bottom=State[0])
plt.show()


plt.bar(range(n), new_State[0] , label="Blue Bar", color='b')
plt.bar(range(n), new_State[4] , label="Blue Bar", color='r',bottom=new_State[0])
plt.show()






