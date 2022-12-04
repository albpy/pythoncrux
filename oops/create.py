#class object reference

class Person:
    def reading(self):      #it is the function in the class.It is called method.
        #self==>instance_keyword
        #self is called instance_keyword.It is to create instance variable

        print("Person reading books")
    def writting(self):
        print("person writing a book")

"""Object is created outside class with the help of class"""
obj1=Person()
obj1.reading()
obj1.writting()

