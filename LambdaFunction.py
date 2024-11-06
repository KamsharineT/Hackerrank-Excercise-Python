# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a:a*10

print(x(2))

j = lambda a,b:a/b
print(j(10,2))

# you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
def testfn(n):
    k = lambda z : z*n
    return k

ans = testfn(9)

print(ans(7))
