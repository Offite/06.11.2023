class Passport:

    def __init__(self, first_name, last_name,country, date_ot_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_ot_birth = date_ot_birth
        self.num_of_passport = num_of_passport

    def printInfo(self):
        print(f'''
Full name: {self.first_name} {self.last_name}       
Date of Birth: {self.date_ot_birth}              
Country: {self.country}
Passport: {self.num_of_passport}              
''')

p = Passport('Iven','Ivenov','Russia','14.05.2005','8221 457896')
p.printInfo()
