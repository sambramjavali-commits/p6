from p6 import employee

def test_employee():
    result = employee("Rahul", "101", "IT", "30000")
    assert result == "Name: Rahul\nID: 101\nDepartment: IT\nSalary: 30000"

def test_employee2():
    result = employee("Amit", "102", "HR", "25000")
    assert result == "Name: Amit\nID: 102\nDepartment: HR\nSalary: 25000"

def test_employee3():
    result = employee("Priya", "103", "Finance", "40000")
    assert result == "Name: Priya\nID: 103\nDepartment: Finance\nSalary: 40000"