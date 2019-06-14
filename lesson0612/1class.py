class Student(object):
	pass

bart = Student()
print(bart)


class Teacher(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

bart = Teacher('Bart', 19)
Jane = Teacher('Jane', 18)
print(Jane.name)

