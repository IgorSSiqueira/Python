"""
Exercise 3.
Create a function that computes the roots of a 
quadratic function using the Bhaskara equation:
    𝑎𝑥2+𝑏𝑥+𝑐=0
    
$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
-> x = (-b +/- sqrt(b^2 - 4ac))/2a    

def bhaskara (a, b, c):
    ...
    return root_1, root_2
If the b^2 - 4ac value is negative, then raise an error

"""

# import math

# def bhaskara(a, b, c):
#     delta =  math.pow(b, 2) - 4*a*c
    
#     if delta < 0:
#         raise Exception('Delta is negative')

#     root1 = (-b + math.sqrt(delta))/2*a    
#     root2 = (-b - math.sqrt(delta))/2*a

#     print('Root 1: ' + str(root1))
#     print('Root 2: ' + str(root2))

# bhaskara(1, 5, 2)


import math

def bhaskara(a, b, c):
    delta =  b ** b - 4*a*c
    
    if delta < 0:
        raise Exception('Delta is negative')

    sqrt_delta = math.sqrt(delta)
    root1 = (-b + sqrt_delta) / (2 * a)    
    root2 = (-b - sqrt_delta) / (2 * a)

    print('Root 1: ' + str(root1))
    print('Root 2: ' + str(root2))

bhaskara(1, 5, 2)