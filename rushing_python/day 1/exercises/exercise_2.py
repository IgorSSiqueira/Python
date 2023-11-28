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
    symbol = str(x)
    add = symbol + symbol
    space_number = lines
    print(symbol.rjust(len(symbol) + space_number))
    space_number = space_number -1
    
    for n in range(1, lines):           
        symbol = symbol + add
        print(symbol.rjust(len(symbol) + space_number))
        space_number = space_number -1

make_pyramid('o', 5)




# def make_pyramid(x, lines: int = 5):
#     symbol = str(x)
#     add = symbol + symbol
#     space_number = lines
#     print(symbol.rjust(len(symbol) + space_number))
#     space_number = space_number -1
    
#     for n in range(1, lines-1):           
#         symbol = symbol + add
#         print(symbol.rjust(len(symbol) + space_number))
#         space_number = space_number -1

# make_pyramid('o', 4)