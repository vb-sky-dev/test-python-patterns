from patterns.creational.factory.employee import Employee


class JavaQA(Employee):

    def __init__(self, name: str, email: str, age: int, profession: str = "Java QA Engineer"):
        super().__init__(name, email, age, profession)

