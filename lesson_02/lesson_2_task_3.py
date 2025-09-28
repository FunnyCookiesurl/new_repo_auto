def square(side):
    area = side * side
    if isinstance(side, float):
        area = int(area) + 1 if area % 1 > 0 else area
    return area


print(square(5))
print(square(2.5))
print(square(3.7))
print(square(8))
