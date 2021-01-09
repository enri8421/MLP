from random import *
import numpy as np
import matplotlib.pyplot as plt



def simulate(n,k,P,a,State,size):
    res_el = 0
    for i in range(n):
        res_state = 0
        for p in range(len(P)):
            m = State[p][i]
            for j in range(m):
                if( randint(1,10) <= P[p]):
                    res_state +=1
        if(res_state == (size[i]/2)):
            res_el += (a[i])/2
        elif(res_state > (size[i]/2)):
            res_el += (a[i])
    return int(round(res_el/k))


def sample_uniform(n,N):
    t = len(N)
    State = [ ([0]*n ) for i in range(t)]
    size =  [0] * n
    for t in range(t):
        for i in range(N[t]):
            s = randint(0,n-1)
            State[t][s] += 1
            size[s] += 1
    return State,size

def sample_gauss(n,N):
    t = len(N)
    State = [ ([0]*n ) for i in range(t)]
    size =  [0] * n
    for t in range(t):
        for i in range(N[t]):
            s = round(gauss(n//2,n/6))
            if(s > (n-1)):
                s = n-1
            elif(s<0):
                s = 0
            State[t][s] += 1
            size[s] += 1
    return State,size

def sample_pro(n,N,z):
    t = len(N)
    State = [ ([0]*n ) for i in range(t)]
    size =  [0] * n
    for t in range(t):
        for i in range(N[t]):
            s = randint(0,n-1)
            if( (t==z) and (random() < 0.25) ):
                s = randint(0,n//2-1)
            State[t][s] += 1
            size[s] += 1
    return State,size



def create_US_sample(data,n):
    State = [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
    size = [0]*n
    for i in range(n):
        for y in range(5):
            a = min(data[y,i,0],data[y,i,1])
            State[2][i] += a//2
            State[1][i] += a//4
            State[3][i] += a//4
            if(data[y,i,0] > data[y,i,1]):
                State[4][i] += abs(data[y,i,0]-data[y,i,1])
            else:
                State[0][i] += abs(data[y,i,0]-data[y,i,1])
  
        for h in range(5):
            State[h][i] = int(round(State[h][i]/5000))
            size[i] += State[h][i]

    return State, size


def print_sample(State):
    n = len(State[0])
    plt.bar(range(n), State[0] , label="Blue Bar", color='b')
    plt.bar(range(n), State[1] , label="Blue Bar", color='lightskyblue',bottom=State[0])
    plt.bar(range(n), State[2] , label="Blue Bar", color='grey',bottom= [State[0][i]+State[1][i] for i in range(n)] )
    plt.bar(range(n), State[3] , label="Blue Bar", color='lightcoral',bottom= [State[0][i]+State[1][i]+State[2][i] for i in range(n)] )
    plt.bar(range(n), State[4] , label="Blue Bar", color='r',bottom= [State[0][i]+State[1][i]+State[2][i]+State[3][i] for i in range(n)] )

    plt.show()