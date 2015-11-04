from random import randint
import math

def distanceProblem():
    n = randint(-20, 20)
    m = randint(-20, 20)
    d1 = 2*n*m
    d2 = n**2 - m**2

    Ax = randint(-100, 100)
    Ay = randint(-100, 100)

    Bx = Ax
    By = Ay

    direction = randint(0, 1)
    if (direction == 0):
        Bx += d1
        By += d2
    else:
        Bx += d2
        By += d1

    ans = int(n**2 + m**2)

    userAns = int(input("Find the distance between A(" + str(Ax) + ", " + str(Ay) + ") " +
          "and B(" + str(Bx) + ", " + str(By) + "): "))

    while (ans != userAns):
        
        userAns = int(input("That is incorrect. Try again: "))

    print("Correct!")

def slopeProblem():
    Ax = randint(-10, 10)
    Ay = randint(-10, 10)

    slope = randint(-5, 5)
    mult = randint(-5, 5)
    
    Bx = Ax + mult
    By = Ay + mult*slope

    A = tuple([Ax, Ay])
    B = tuple([Bx, By])

    ans = slope

    userAns = int(input("Find the slope of a line, which passes through point " +
                        "A" + str(A) + " and B" + str(B) + ": "))
    
    while (ans != userAns):
        
        userAns = int(input("That is incorrect. Try again: "))

    print("Correct!")
