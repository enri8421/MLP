import numpy as np
from utilities import *
from optimizer import *
import matplotlib.pyplot as plt



path = "data"

"https://worldpopulationreview.com/state-rankings/electoral-votes-by-state"

electors = np.loadtxt(path+'/electors_sorted')


data = np.zeros((5,51,2))

"https://www.fec.gov/help-candidates-and-committees/dates-and-deadlines/2020-reporting-dates/federal-election-activity-periods-each-state-2020/"
data[4] = np.loadtxt(path+'/2020_results')

"https://www.fec.gov/documents/1890/federalelections2016.xlsx"
data[3] = np.loadtxt(path+'/2016_results')

"https://www.fec.gov/documents/1695/tables2012.xls"
data[2] = np.loadtxt(path+'/2012_results')

"https://www.fec.gov/documents/1666/federalelections2008.xls"
data[1] = np.loadtxt(path+'/2008_results')

"https://www.fec.gov/documents/1631/2004tables.xls"
data[0] = np.loadtxt(path+'/2004_results')

name = np.loadtxt(path+'/state_name.csv',dtype="str")


P = [2,4,5,6,8]
n = 51
k = sum(electors)

g = 1000

seed(2)


State, size = create_US_sample(data,n)

print_sample(State)

result = 0
for i in range(g):
    result += simulate(n,k,P,electors,State,size)


print("probability of victory for republican = ",result/g)



new_State, new_size = find_best_distribution(State,n,electors)


print_sample(new_State)

result = 0
for i in range(g):
    result += simulate(n,k,P,electors,new_State,new_size)

print("new probability of victory for republican = ",result/g)


difference =[0]*n
for i in range(51):
  pr = 0
  po = 0
  for t in range(5):
    pr += State[t][i]
    po += new_State[t][i]

  difference[i] = State[4][i]/pr - new_State[4][i]/po


Z = [x for _,x in sorted(zip(difference,name))]
print(Z[:5])











