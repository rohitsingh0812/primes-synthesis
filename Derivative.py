import math
import random

class Specification:
    bounds={}
    params={}
    output = ""

    def __init__(self):
        return
    
    def template(self):
        return

    def setOutput(self, output):
        Specification.output = output

    def setParams(self, p):
        Specification.params = p

    def constraints(self):
        return

    def correct(self):
        return


class PolynomialDerivative(Specification):

    def __init__(self):
        Specification.params = {'x':1, 'p':0, 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}
        Specification.bounds = {'x': 1, 'p': 5, 'a': 9, 'b': 9, 'c': 9, 'd': 9, 'e': 9, 'f': 9, 'g':9}
            
        
    def template(self):
        params = Specification.params
        output = ""
        output += "Find the derivative of: \n"
        count = 0
        for i in range(97, 97+params['p']):
            ## print params['p']
            if i == 97:
                output += str(params[chr(i)]) + "x^" + str(params['p']-count)
            elif (params[chr(i)] != 0):
                output += " + " + str(params[chr(i)]) + "x^" + str(params['p']-count)
            count += 1
        output += " + " + str(params[chr(int(params['p'])+97+1)])
        output += "\n at x=" + str(params['x'])
        return output

    def constraints(self):
        params = Specification.params
        bounds = Specification.bounds
        for key in params.keys():
            if abs(params[key]) > bounds[key]:
                return False
        return True

    def compute(self):
        userAns = input("Your solution: ")
        while not self.isCorrect(userAns):
            userAns = input("Incorrect! Try again: ")
        print "Correct!"

    def isCorrect(self, userAns):
        if self.calcDeriv() == userAns and self.constraints():
            return True
        return False
        
    def calcDeriv(self):
        deriv = 0
        params = Specification.params
        count = params['p']
        for i in range(97, 97+params['p']):
            if params[chr(i)] != 0:
                ## print ((count)*params[chr(i)]) * pow(params['x'],(count-1))
                deriv += ((count)*params[chr(i)]) * pow(params['x'],(count-1))
            count -= 1
        ## print "Deriv " + str(deriv)
        return deriv

class Solver:

    problem = PolynomialDerivative()
    
    def __init__(self, p):
        problem = p

    def setProblemParams(self):
        params={}
        bounds = Solver.problem.bounds

        for key in bounds.keys():
            ## print "Vals: " + str(params)
            val = random.randint(1, bounds[key])
            if key != 'p' and random.randint(1,2) == 1:
                val *= -1
            params[key] = val
        Solver.problem.setParams(params)
                 
    

p = PolynomialDerivative()
## print p.bounds
s = Solver(p)
s.setProblemParams()
print Solver.problem.template()
print Solver.problem.compute()
        
