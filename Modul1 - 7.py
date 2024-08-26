grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print(students)
stud_l = list(students)
stud_l.sort()
#print(stud_l)
midd_note_A =sum(grades[0])/len(grades[0])
midd_note_B =sum(grades[1])/len(grades[1])
midd_note_J =sum(grades[2])/len(grades[2])
midd_note_K =sum(grades[3])/len(grades[3])
midd_note_S =sum(grades[4])/len(grades[4])
print ({stud_l[0]: midd_note_A, stud_l[1]: midd_note_B, stud_l[2]: midd_note_J, stud_l[3]: midd_note_K, stud_l[4]: midd_note_S})