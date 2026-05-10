
numbers = [1, 2, 3, 4, 5]

squares = []
cubes = []

for i in numbers:
    square = i * i
    cube = i * i * i

    squares = squares + [square]
    cubes = cubes + [cube]

print("Numbers List =", numbers)
print("Squares List =", squares)
print("Cubes List =", cubes)