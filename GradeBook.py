last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics','calculus','poetry','history']
grades = [98,97,85,88]
grade_book = zip(subjects, grades)


full_gradebook= last_semester_gradebook + list(grade_book) 

print(full_gradebook)