import math
n=int(input("Enter the number:"))
fibonacci_formula_add=5*n*n+4
fibonacci_formula_sub=5*n*n-4
if(math.isqrt(fibonacci_formula_add)**2==fibonacci_formula_add or math.isqrt(fibonacci_formula_sub)==fibonacci_formula_sub):
    print("It's a Fibonacci Number!")
else:
    print("It's not a Fibonacci Number!")
