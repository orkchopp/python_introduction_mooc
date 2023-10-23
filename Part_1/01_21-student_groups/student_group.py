import math
num_students = int(input("Enter the number of students on the course: "))
group_size = int(input("Enter the desired group size: "))

print(f'Number of groups formed: {math.ceil(num_students/group_size)}')