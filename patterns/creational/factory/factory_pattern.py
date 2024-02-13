from python_developer import PythonDeveloper
from employee import Employee
from qa_automation import QAAutomation
from java_qa import JavaQA


class EmployeeFactory:

    def get_employee_by_type(self, employee_type: str):
        if employee_type == "python":
            return PythonDeveloper(name="Gleb", age=29, email="default email python")
        if employee_type == "java":
            return JavaQA(name="Vlad", age=33, email="default email java")
        if employee_type == "qa":
            return QAAutomation(name="Sasha", age=29, email="default email QA")
        else:
            print("No such Employee found!!!")
            print("Will return Employee with null fields!!!")
            return Employee(name="null", age=0, email="null", profession="null")


if __name__ == "__main__":

    employee_factory = EmployeeFactory()

    null_employee = employee_factory.get_employee_by_type("vlad")
    python_employee = employee_factory.get_employee_by_type("python")
    java_employee = employee_factory.get_employee_by_type("java")
    qa_employee = employee_factory.get_employee_by_type("qa")

    print("=======================================================")
    python_employee.working_activities()
    print("=======================================================")
    java_employee.working_activities()
    print("=======================================================")
    qa_employee.working_activities()
    print("=======================================================")
    null_employee.working_activities()

