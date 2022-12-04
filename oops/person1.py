class Person: #fname,lname,age,phone,loc
    def setvalue(self, fname, lname,age,phno,loc):
        #convert variables to instant variables
        self.fname=fname
        self.lname=lname
        self.age=age
        self.phno=phno
        self.loc=loc
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.phno,self.loc)
person1=Person()
person1.setvalue('vinay','k',26,12345,'erklm')
person1.printvalue()

person2=Person()
person2.setvalue('Aby','Denny',26, 8590861917, 'erklm')
person2.printvalue()
