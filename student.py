import random
from data import student_array

list_length = len(student_array)

n = random.randint(0, list_length - 1)
print(student_array[n])
