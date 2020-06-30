import clr

#from System import String
#from System.Collections import *
clr.AddReference(r'D:\rabota\csharp+dll_python\cdp\ClassLibrary1\obj\x64\Debug\ClassLibrary1.dll')  
# The R lets python interpret the string RAW so you can put in Windows paths easy
from MyNameSpace import MyClass
my_instance = MyClass()
x = my_instance.hello(3.1)
print(x)  # Output: Hello from Mrs. C and Mr. Sharp
