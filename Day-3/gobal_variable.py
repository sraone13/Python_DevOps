x = 10  # both Global variable
y = 20

def my_function():
    a = x + y
    print(a)   # This will access the global variable 'y'
    
my_function()

b = x - y
print(b) # This will print -10


