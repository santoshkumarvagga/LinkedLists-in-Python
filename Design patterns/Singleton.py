'''
Singleton is a creational design pattern that lets you ensure that a class has 
only one instance, while providing a global access point to this instance.
'''

class A():
    def __str__(self):
        return "I'm the only one"

    def roar(self):
        return 'Grrr'

a = A()
b = A()

print(a is b) #expect False

# here a and b are diff objects.
print("id of a",id(a))
print("id of b",id(b))

# to make them same objects, 
'''
step 1: Make class private - just append a leading single underscore to class name
step 2: Create a private variable, of module level scope and intialise it to None. 
step 3: 
'''