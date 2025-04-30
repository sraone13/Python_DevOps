import sys

def add(num1, num2):
    add = num1 + num2
    return add

def mul(num1, num2):
    m = num1 * num2
    return m

def sub(num1, num2):
    s = num1 - num2
    return s

num1 = int(sys.argv[1])
operational = sys.argv[2]
num2 = int(sys.argv[3])


if operational == "add":
    output = add(num1, num2)
    print(output)

if operational == "mul":
    out = mul(num1, num2)
    print(out)

if operational == "sub":
    out = sub(num1, num2)
    print(out)

