# Program to create a new list containing cube of each number


li = [1, 2, 3, 4, 5]

cube_list = []

for i in li:
    cube = i * i * i
    cube_list = cube_list + [cube]

print("Original List =", li)
print("Cube List =", cube_list)