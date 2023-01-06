class Employee:
    fullname = ""
    email = ""

    def __init__(self, first_name, last_name):
        self.fullname = first_name + " " + last_name
        self.email = f'{first_name}.{last_name}@and.digital'.lower()


e = Employee("John", "Smith")

print(e.fullname)
print(e.email)
