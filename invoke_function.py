import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()




#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file

print("Invoking function with mix of default arguments and required")
introduction_with_mix_of_default_args("Amanuel")

print("Invoking function with required arguments that returns sum of the two numbers ")
print(product_of_two_num(2,4))

print("Invoking function with required arguments ")
print(add_all_nums(5,6,74,5,4))

print("Invoking a lambda function")
print(double2(22))

print("Invoking a function with required arguments that doubles given num")
print(double(99))

