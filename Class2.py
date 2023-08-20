# class A:
#     def sayhello(self):
#         print("Hello")
#
#
# class B(A):
#     def saybye(self):
#         print("Goodbye")
#
#
# a = A()
# b = B()
#
# b.saybye()
# b.sayhello()


class Father:
    def __init__(self, fname, address, job):
        self.familyname = fname
        self.address = address
        self.job = job

    def sayhello(self):
        print("Hello")


class Child(Father):
    def __init__(self, fname, address, uni, job=None):
        super().__init__(fname, address, job)
        self.university = uni

    def saybye(self):
        print("Goodbye")


pedar = Father("Ahmadi", "Ekbatan", "Teacher")
farzand = Child("Ahmadi", "Ekbatan", "Sharif", "Engineer")
print(farzand.job)
