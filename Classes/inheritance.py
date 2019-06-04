class Laborer():
    def __init__(self,name,salary,department):
        print("The Struct Function of The Laboring Class")
        self.name=name
        self.salary=salary
        self.department=department
    def showinformation(self):
        print("Showing information of the laboring class\n")
        print("Name: {}\nSalary: {}\nDepartment: {}\n".format(self.name,self.salary,self.department))
    def raisesalary(self,raise_amount):
        print("The salary has been raise")
        self.salary += raise_amount
    def changedepartment(self,new_dep):
        print("Department changed to {}".format(new_dep))
        self.department=new_dep

"""class Administrator():
    pass
"""

class Administrator(Laborer):   ## Yonetici de ayni zamanda bir calisandir...
    
    def __init__(self,name,salary,department,managed_person_count):
        print("The Struct Function of the Administrator Class")
        super().__init__(name,salary,department)    ## super anahtar kelimesi base class in fonksiyonlarini cagirabilmemizi sagliyor...
        """self.name=name
        self.salary=salary
        self.department=department"""
        self.managed_person_count=managed_person_count
    def showinformation(self):
        print("Showing information of the administrator class\n")
        print("Name: {}\nSalary: {}\nDepartment: {}\nManaged Person Count: {}".format(self.name,self.salary,self.department,self.managed_person_count))
    def raise_managed_person_count(self,number):
        print("Raising number of managed person...")
        self.managed_person_count+=number

yonetici = Administrator("Zümrüd-ü Anka",9999999999,"Entrepreneur",1000000000)
yonetici.showinformation()
yonetici.raise_managed_person_count(25)
yonetici.showinformation()