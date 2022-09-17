# Suppose there is XYZ Company and there are different departments like production, marketing, finance, sales etc. Manager of the company want to know about the detail of the employees who are highly paid in each of the department. Write a program using the concept of classes to implement the same.
# show the highest salary in each department
# 
class xyz:
    #departments
    production=list()
    marketing=list()
    finance=list()
    sales=list()
    
    
    def __init__(self, name, salary, dep):
        self.name = name
        self.salary = salary
        self.dep = dep
        d=(self.name, self.salary, self.dep)
        if dep == "p":
            self.production.append(d)
        elif dep == "m":
            self.marketing.append(d)
        elif dep == "f":
            self.finance.append(d)
        elif dep == "s":
            self.sales.append(d)
        else:
            print("Invalid department")
            

def max(l, dep):
    max = 0
    for i in l:
        if i.dep == dep:
            if i.salary > max:
                max = i.salary
                name = i.name
    return name, max
        


def dataInput():
    x=xyz
    l=list()
    n = eval(input("Enter the number of employees: "))
    for i in range(0, n):
        name = input("Enter the name: ")
        salary = eval(input("Enter the salary: "))
        dep = input("Enter the department: ")
        l.append(xyz(name, salary, dep))

    print("Highest salary in production is", max(l, "production"))
    print("Highest salary in marketing is", max(l, "marketing"))
    print("Highest salary in finance is", max(l, "finance"))
    print("Highest salary in sales is", max(l, "sales"))
    


dataInput()


# Create student class which is derived from course and result is from Student. With the help of appropriate attributes and functions find out Grade of student according to CGPA.
# class course:
#     def __init__(self, name, code, credit):
#         self.name = name
#         self.code = code
#         self.credit = credit
# class result(course):
#     def __init__(self, name, code, credit, grade):
#         self.grade = grade
#         course.__init__(self, name, code, credit)
# class student(result):
#     def __init__(self,id):
#         print("Enter the details of the student")
        
        
        
# s=student()