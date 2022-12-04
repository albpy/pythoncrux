#student
#id,fname,lname,age,dept,college_name
#5students

class Students:
    def details(self,id_of,fname,lname,age,dept):
        self.id_of=id_of
        self.fname=fname
        self.lname=lname
        self.age=age
        self.dept=dept
    
        def prntdetails(self):
            print(self.id_of,self.fname,self.lname,self.age,self.dept)
student1=Students
student1.details(19,'Agj','jake',19,'mech')
student1.prntdetails()

