class Animal(object):
	def run(self):
		print("Animal is running...")

class Dog(Animal):
	pass

class Cat(Animal):
	pass


if __name__ == '__main__':
	dog = Dog()
	dog.run()

	cat = Cat()
	cat.run()
