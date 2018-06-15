class Parent(object):

	def implicit(self):
		print("PARENT implicit")

	def override(self):
		print("PARENT override()")

	def altered(self):
		print("PARENT alerted()")

class Child(Parent):

	def override(self):
		print("CHILD override()")

	def altered(self):

		print("CHILD, BEFORE PARENT altered()")
		super(Child,self).altered()		
		print("CHILD, AFTER PARENT alerted()")	



dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()		