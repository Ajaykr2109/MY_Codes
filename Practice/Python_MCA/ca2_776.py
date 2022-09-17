# Suppose there is XYZ Company and there are different departments like production, marketing, finance, sales etc. Manager of the company want to know about the detail of the employees who are highly paid in each of the department. Write a program using the concept of classes to implement the same.

class xyz:
    class production:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    class marketing:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    class finance:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    class sales:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    def max(self, obj):
        max = 0
        for i in obj:
            if i.salary > max:
                max = i.salary
                name = i.name
        return name, max

    # check for highest salary in production, marketing, finance, sales and print the name of the employee and his salary


def dataInput():
    x=xyz()
    n = eval(input("Enter the number of employees: "))
    for i in range(0, n):
        name = input("Enter the name: ")
        salary = eval(input("Enter the salary: "))
        dep = input("Enter the department: ")
        if dep == "production":
            x.production.append(x.production(name, salary))
        elif dep == "marketing":
            x.marketing.append(x.marketing(name, salary))
        elif dep == "finance":
            x.finance.append(x.finance(name, salary))
        elif dep == "sales":
            x.sales.append(x.sales(name, salary))
        else:
            print("Invalid department")
            dataInput()


    # x=xyz()
    # x.production("A", 10000)
    # x.production("B", 20000)
    # x.production("C", 30000)

    # d = x.marketing("D", 10000)
    # e = x.marketing("B", 20000)
    # f = x.marketing("C", 30000)

    # g = x.finance("A", 10000)
    # h = x.finance("B", 20000)
    # x.finance = x.finance("C", 30000)

    # x.sales = x.sales("A", 10000)
    # x.sales = x.sales("B", 20000)
    # x.sales = x.sales("D", 40000)


def main():
    x = xyz()
    dataInput()
    print(x.max(x.production))
    print(x.max(x.marketing))
    print(x.max(x.finance))
    print(x.max(x.sales))


main()

# class xyz:
#     def production(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def marketing(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def finance(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def sales(self, name, salary):
#         self.name = name
#         self.salary = salary
