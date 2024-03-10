import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt

model = gp.Model('Problem2')
n = 2000
ratio = model.addVar(lb=0)
g = model.addVars(n + 1, lb=0)
G = model.addVars(n + 1, lb=0)

# Set the objective
model.setObjective(ratio, GRB.MAXIMIZE)

model.addConstr(g[n] == 1)
model.addConstr(G[0] == 0) 

for x in range(1, n + 1):
    model.addConstr(G[x] == G[x - 1] + 1 / n * g[x - 1]) #Get sum

for x in range(1, n + 1):
    model.addConstr(g[x - 1] <= g[x]) #increasing func g

# competitive ratio = min ......    
for x in range(1, n):
    for y in range(1, n + 1):
        model.addConstr(ratio <= G[x - 1]  + (1 - (y - 1) / n) * (1 - g[x])+ G[y - 1]) 
        
model.optimize()

g_values = [g[i].x for i in range(n + 1)]
plt.plot(range(n + 1), g_values)
plt.xlabel('x')
plt.ylabel('g(x)')
plt.title('Graph of Function g')
plt.show()