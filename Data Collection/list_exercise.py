data = [
    [101, "John", [67,78,76,88,56]],
    [102, "Sam", [90,88,77,80,50]],
    [103, "Tom", [55,58,66,70,77]],
    [104, "Nick", [81,70,56,45,62]],
    [105, "Adam", [59,79,86,67,56]]
    ]

'''
1. Print Name and Total marks of each student
2. Print Name and Average marks of each student
3. Print Percentange of student
'''
for i in range(len(data)):
    marks = data[i][-1]
    name = data[i][1]
    #total_marks = sum(marks)
    total_marks = 0
    for j in marks:
        total_marks += j
    print(f"Total marks of {name} are : {total_marks}")
