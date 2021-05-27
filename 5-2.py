from gurobipy import *
m = Model("transport project")
# Create variables
x = [m.addVar(vtype=GRB.BINARY, name='x'+str(i+1)) for i in range(11)]
# Integrate new variables
m.update()
# Set objective
m.setObjective(4*x[0] + 5*x[1] + 3*x[2] + 4.3*x[3] + x[4] + 1.5*x[5] + 2.5*x[6] + 0.3*x[7] + x[8] + 2*x[9], GRB.MAXIMIZE)
# Add constraints
m.addConstr(2*x[0] + 3*x[1] + 1.5*x[2] + 2.2*x[3] + 0.5*x[4] + 1.5*x[5] + 2.5*x[6] + 0.1*x[7] + 0.6*x[8] + x[9] <= 5) 
m.addConstr(x[0] + x[1] + x[2] + x[3] <= 1)
m.addConstr(x[4] + x[5] + x[6] <= 1)
m.addConstr(x[7] + x[8] + x[9] <= 1)
m.addConstr((x[1] + x[3])*(1 - (x[5] + x[6])) == 0)
m.optimize()