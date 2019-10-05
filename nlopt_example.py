import nlopt



from numpy import *
def myfunc(x, grad):  #square root of x
    if grad.size > 0:
        grad[0] = 0.0
        grad[1] = 0.5 / sqrt(x[1])	#partial derivative
    return sqrt(x[1])
def myconstraint(x, grad, a, b): #constaints x2 > (2x1)^3 and x2 > (-x+1)^3

    if grad.size > 0:
        grad[0] = 3 * a * (a*x[0] + b)**2
        grad[1] = -1.0
    return (a*x[0] + b)**3 - x[1]

opt = nlopt.opt(nlopt.LD_MMA, 2)
opt.set_lower_bounds([-float('inf'), 0])
opt.set_min_objective(myfunc) # minimise
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,2,0), 1e-8) # in equality constaint
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
opt.set_xtol_rel(1e-4) #tolerance
x = opt.optimize([1.234, 5.678]) #initial guess
minf = opt.last_optimum_value()
print("optimum at ", x[0], x[1])
print("minimum value = ", minf)
print("result code = ", opt.last_optimize_result())

