data = {
    "names" : ["John", "Sam", "Mac", "Smith", "Adam"],
    "salary" : [56000, 45000, 78000, 40000, 50000],
    "dept" : ["IT", "HR", "IT", "IT", "HR"]
    }

'''
1. Fetch salary of Mac
2. Get total salary of IT department
'''
index = data["names"].index("Mac")
salary = data["salary"][index]
print("Salary is :", salary)

total_salary = 0
for i in range(len(data["dept"])):
    if data["dept"][i] == "IT":
        total_salary += data["salary"][i]

print("Total salary of IT department is :",total_salary)
