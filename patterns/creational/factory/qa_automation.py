from patterns.creational.factory.employee import Employee


class QAAutomation(Employee):

    def __init__(self, name: str, email: str, age: int, profession: str = "QA Automation Engineer"):
        super().__init__(name, email, age, profession)