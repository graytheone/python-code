class Student(object):
		
	def __init__(self, name):
		self.__name = name

	def getName(self):
		return self.__name


Bart = Student("abc")
#print(Bart.__name)
Bart.__name = 'sugar'
print(Bart.__name)
#print(Bart.getName())
