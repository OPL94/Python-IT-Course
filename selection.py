a = 5
b = 10
c = 15

print(a if a > b else b)
print("a is bigger" if a > b else "b is bigger")
print("a is bigger" if a > b > c else "b is bigger" if b > c > a else "c is bigger")