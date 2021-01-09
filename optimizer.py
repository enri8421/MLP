from pulp import *
import numpy as np


def find_best_distribution(x,n,p):
  N = sum(x[4])
  K = int(sum(p)/2)
  problem = LpProblem("Problem", LpMaximize)
  h = -0.3*np.array(x[0]) - 0.1*np.array(x[1]) + 0*np.array(x[2]) + 0.1*np.array(x[3]) 
  H = 100000

  z = LpVariable.dicts("z",range(n),lowBound=0,cat='Continuous')
  a = LpVariable.dicts("a",range(n), cat='Binary')
  m = LpVariable("m",lowBound=0,cat='Continuous')
  problem += m


  problem += lpSum([z[i] for i in range(n)]) == N
  problem += lpSum([a[i]*p[i] for i in range(n)]) <= K
  for i in range(n):
    problem += h[i]  + 0.3*z[i]+ H*a[i] >= m


  solver = getSolver('PULP_CBC_CMD',msg = False)
  problem.solve(solver)

  new_size = [0]*n
  new_x = [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
  for i in range(n):
    for t in range(4):
      new_x[t][i] = x[t][i]
    new_x[4][i] = round(z[i].varValue)
    for j in range(5):
      new_size[i] += new_x[j][i]
  return new_x, new_size