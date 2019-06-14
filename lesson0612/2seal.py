class Student(object):
	phone = 12344
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getInfo(self):
		print(self.age)
	
	def run(self):
		....
	def eat(self):

Bart = Student('Bart', 12)
Bart.getInfo()
Bart.eat()
