"""
mod_func_def.py:  imports a module and then goes through the module's namespace
to find any functions and print the names of the functions and their arguments,
in the same way as it might appear in a def statement.
"""
import inspect
def mod_func_def(module):
    module = __import__(module)
    classobjects = [obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]
    
    for obj in classobjects:
        print("'def {0}{1}'".format(str(obj).split()[1], inspect.formatargspec(*inspect.getfullargspec(obj))))
        
if __name__ == "__main__":
    mod_func_def("json")