a = 23
b = 7
c = a + b
d = a / b
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)
print("Sum of %d and %d is %d"%(a,b,c))
print("Div of %d and %d is %f"%(a,b,d))

print("Sum of {} and {} is {}".format(a,b,c))
print("Div of {} and {} is {:.2f}".format(a,b,d))
print("Sum of {2} and {0} is {1}".format(b,c,a))

#f-strings
print(f"Sum of {a} and {b} is {c}")
print(f"Div of {a} and {b} is {d:.2f}")
