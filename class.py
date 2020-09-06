class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_other_info(self):
        print(f"{self.name}'s email: {self.email} {self.name}'s phone number: {self.phone}.")

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-685-3456")

sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone)
print(jordan.email, jordan.email)





