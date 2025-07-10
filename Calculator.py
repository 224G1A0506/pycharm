class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
c=Calculator()
a=int(input())
b=int(input())
# print(c.add(a,b))
print(f"Addition of ({a}, {b}) is {c.add(a, b)}")
print(f"Subtraction of ({a},{b}) is {c.sub(a,b)}")
print(f"Multiplication of ({a},{b}) is {c.mul(a,b)}")
print(f"Division of ({a},{b}) is {c.div(a,b)}")