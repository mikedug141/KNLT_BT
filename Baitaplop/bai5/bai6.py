import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_detals = [('Jame', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
students = np.array(students_detals, dtype=data_type)
print ("Original Array: ")
print (students)
print ("sort by Heigh")
print (np.sort(students, order='Heigh'))