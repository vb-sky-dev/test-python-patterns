
class Employee:
    def __init__(self, name: str, email: str, age: int, profession: str):
        self.name = name
        self.email = email
        self.age = age
        self.profession = profession

    def employee_say(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def working_activities(self):
        self.employee_say()
        print(f"I am working like {self.profession}")

