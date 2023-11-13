"""
1. Create a function that receives a number n and prints a triangle of * like the following:
    
```
In: triangle(4)
*
**
***
****
```

"""
def make_triangle(x):
    triangle = '*'

    for n in range(0, x-1):
        if n == 0:
            print(triangle)
        
        triangle = triangle + '*'
        print(triangle)

make_triangle(10)