class Student():
#	paint = False
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Teacher():

	pass


#student1 = {'name':'Jane', 'age':15 }
#student2 = { }

Jane = Student('Jane', 20)
Bob = Student('Bob', 19)
Jane.paint = True
print(Jane.name)
