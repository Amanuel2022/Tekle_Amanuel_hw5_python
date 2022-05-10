from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. 
You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. The class would have attributes 
associated with the user’s username, password, registration date, and more. Methods would define the actions the user could take, 
such as registering, authenticating, logging in, and logging out. You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

print("First attempt at running class")
br = Arithmetic(3,19)
print(br.add())
print(br.divide())
print(br.remainder())
br.print_self()

print("second attempt")
cr = Arithmetic(8,6)
print(cr.add())
print(cr.divide())
print(cr.remainder())
print(cr.multiply())
print(cr.subtract())
print(cr.remainder())
cr.print_self()