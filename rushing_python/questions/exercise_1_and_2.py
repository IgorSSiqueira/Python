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


"""
2. Create a function that receives a number n and string (or char) x and writes a triangle like the following:
In: other_triangle(4, '0')
Out:
    o
   ooo
  ooooo
 ooooooo

"""

def make_pyramid(x, lines: int = 5):
    for n in range(0, lines-1):  
        if n == 0:
            simbol = str(x)
            add = simbol + simbol
            space_number = lines
            print(simbol.rjust(len(simbol) + space_number))
            space_number = space_number -1
        
        simbol = simbol + add
        print(simbol.rjust(len(simbol) + space_number))
        space_number = space_number -1

make_pyramid('o', 4)