# def is a keyword that we use to define the function.
# addition is a function name here, a, b are a value or parameter.
# Observe the indentation(spacing) of the code within the function on line no. 11.
# On line 18, the pass statement allows defining an empty function without causing an error.
# Observe lines no. 13 and 14, same function called with different values.

#Task 1: Uncomment lines 21 & 22 and fix the error.
#Task 2: Call function subtraction after fixing the error with 156 and 100

def addition(a, b): 
    print(a + b)

addition(4, 6)  # Calls function with 4 and 6
addition(10, 20)  # Calls function with 10 and 20

# Example function with pass (a placeholder for future code)
def multiply(a, b):
    pass  # No implementation yet
multiply(4,5) # No output will be seen as pass given in the function body.

#def subtraction(a, b): 
#print(a - b)
