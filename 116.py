class Person:
    def __init__(self, name, age, job, country):
        self.name = name
        self.age = age
        self.job = job
        self.country = country

    def talk(self):
        print(f"""
Hi, My name is {self.name}
Im {self.age} years old and Im from {self.country}
Im a {self.job}
        """)


kamyar = Person("Kamyar", 25, "Civil Engineer", "Iran")
kamyar.talk()
