import math

class Specification:
    dict bounds, params

    def __init__():
        return
    
    def template(self):
        return

    def setOutput(self, output):
        output = output

    def setParams(self, p):
        params = p

    def constraints(self):
        return

    def correct(self):
        return

    def bounds(self):
        return


class PolynomialDerivative:

    def __init__():
        params = {'x':0, 'p':0, 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
        bounds = {'x': 100, 'p': 5, 'a': 9, 'b': 9, 'c': 9, 'd': 9, 'e': 9, 'f': 9}
            
        
    def template(self):
        print "find the derivative of: "
        for i in range(params['p']):
            if params[i] != 0:
                print params[i] + "x^" + values[-1] + " + "
        print values[5] + "x^" + values[-1] " at x = " params[x]

    def constraints(self):
        for key in params.keys():
            if abs(params[key]) > bounds[key]:
                return False
        return True
        
    def compute(self):
         userAns = input("Your solution: ")
         while not isCorrect(userAns):
             userAns = input("Incorrect! Try again: ")
        print "Correct!"

    def isCorrect(userAns):
        if calcDeriv() == userAns && constraints():
            return True
        return False
        
    def calcDeriv():
        int deriv = 0, count=1
        for i in range(97, 97+params['p']):
            if params[chr(i)] != 0:
                deriv += ((count)*params[chr(i)]) * (params['x']**(count-1))
            count ++
        
            
        deriv += params['p']

class Solver:

    Specification spec
    
    def __init__(self, specification):
        spec = specification

    def setProblemParams():
        dict params, bounds = spec.bounds

        for key in bounds.keys():
            int val = randint(1, bounds[key])
            if randint(1,2) == 1:
                val *= -1
            params[key] = val
        spec.setParams(params)
                 
    

PolynomialDerivative p
Solver s
s.setProblemparams()
print p.template()
        
