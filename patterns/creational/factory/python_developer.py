from patterns.creational.factory.employee import Employee


class PythonDeveloper(Employee):

    def __init__(self, name: str, email: str, age: int, profession: str = "Python Development Engineer"):
        super().__init__(name, email, age, profession)
