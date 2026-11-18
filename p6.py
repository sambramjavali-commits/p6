import sys

def employee(name, empid, dept, salary):
    return f"Name: {name}\nID: {empid}\nDepartment: {dept}\nSalary: {salary}"

if __name__ == "__main__":
    name = sys.argv[1]
    empid = sys.argv[2]
    dept = sys.argv[3]
    salary = sys.argv[4]

    result = employee(name, empid, dept, salary)
    print(result)