def my_function():
    x = 10 # Local variable
    print(x)

my_function()
print(x)   # This will raise an error since 'x' is not defined outside the function.