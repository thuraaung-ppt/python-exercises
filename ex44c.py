
class Parent(object):

	def altered(self):
		print("PARENT alerted()")


class Child(Parent):		

	def altered(self):

		print("CHILD, BEFORE PARENT altered()")
		super(Child,self).altered()		
		print("CHILD, AFTER PARENT alerted()")		



dad = Parent()
son = Child()

dad.altered()
son.altered()		
