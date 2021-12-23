import math

c = 360
a = round(c * math.sin(math.radians(35)), 3)
b = round(c * math.cos(math.radians(35)), 3)
print(f"{a} {b} {a + b + c} {round(a * b * 0.5, 3)}")
