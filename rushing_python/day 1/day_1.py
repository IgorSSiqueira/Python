"""
def factorial_with_if_and_recursion(n):
    if n < 0:
        raise Exception('NO')
    elif n == 0 or n == 1:
        return 1    
    
    return n * factorial_with_if_and_recursion(n - 1)

def factorial_with_for(n):
    if n < 0:
        raise Exception('NO')
    
    factorial = 1
    for k in range(1, n): #[0, 1, ...., n - 1]
        factorial = factorial * (k + 1)
        
    return factorial


for n in range(0, 20):
    print(f'{n}! = {factorial_with_for(n)}')

1. Create a function that receives a number n and prints a triangle of * like the following:
    
```
In: triangle(4)
*
**
***
****
```

2. Create a function that receives a number n and string (or char) x and writes a triangle like the following:

```
In: other_triangle(4, '0')
Out:
    o
   ooo
  ooooo
 ooooooo
```

3.
Create a function that computes the roots of a 
quadratic function using the Bhaskara equation:
𝑎𝑥2+𝑏𝑥+𝑐=0
 
𝑥=−𝑏±𝑏2−4𝑎𝑐⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯√2𝑎
 
def bhaskara (a, b, c):
    ...
    return root_1, root_2
If the b^2 - 4ac value is negative, then raise an error


"""




url = 'https://gist.githubusercontent.com/metaphys/1257793/raw/032486ab7bf92bf6d50eb2619ebf9cf17d60fe4a/Xorg.8.log'

# with open("small-test.txt", "w") as f:
#     f.write("hello world\n")
#     f.write("hello world 2")

# #alternative
# f = open('small-test.txt', 'w')
# f.write('hello world 2')
# f.close


with open("xorg.8.log", "r") as f:
    for line in f.readlines():
        #We actually want to check if the line starts with [
        if "[" not in line:
            continue

        if '(EE)' not in line:
            continue

        #at this point of the code, we are in an error line of the
        #form "[timestamp] (EE) Error message"

        
        # Solution 1: Using absolute position 
        # time_stamp = line[1:11]
        # error_msg = line[18:].split

        # # Solution 2: Using split and join (better option)
        # print(line)
        separeted_line = line.split()
        # print(separeted_line)

        time_stamp =  separeted_line[1]
        time_stamp = time_stamp[0:-1]
        # print(time_stamp)
        error_msg = ' '.join(separeted_line[3:]) #all the way to the end

        # Solution 3: Using Regular expression (overkill) -> Not basic

        
        print(f'At time {time_stamp}, error {error_msg}')
        


# Exercise 4:

# Read a folder of log files like this one
# Search here: https://gist.github.com/search?q=Xorg.8.log&ref=searchresults
# Aggregate all error messages (massages with "(EE)")
# Order by time stamp
# Write to a new file

# Q: How to read all files in a folder
# Keep all messages in memory (probably using append)
# Sort the messages

