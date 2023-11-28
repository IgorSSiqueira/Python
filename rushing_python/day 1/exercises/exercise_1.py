
# 1. Create a function that receives a number n and prints a triangle of * like the following:
# ```
# In: triangle(4)
# *
# **
# ***
# ****
# ```


def make_triangle(x):
    triangle = '*'

    print(triangle)
    for _ in range(1, x):    
        triangle += '*'
        print(triangle)

make_triangle(4)

