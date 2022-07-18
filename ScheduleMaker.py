
max_employee_hours = 40
required_managers = 2



class Employee:
    
    '''
    name = string
    age = int
    desired_hours = int
    availibility = NOT SURE YET
    '''

    def __init__(self,name,age,desired_hours,availibility):
        self.name = name
        self.age = age
        self.desired_hours = desired_hours
        self.availibility = availibility

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_desired_hours(self):
        return self.desired_hours

    def get_availibility(self):
        return self.availibility

    def set_desired_hours(self, new_desired_hours):
        self.desired_hours = new_desired_hours
        return self.desired_hours
    
    def set_availibility(self, new_availibility):
        self.availibility = new_availibility
        return self.availibility

    def __str__(self):
        return "Employee:\nName: " + self.name


class Manager(Employee):
    def isManager(self):
        return 'yes'

    def __str(self):
        return "Manager\nName: " + self.name

employee_list = ['Blake Liu','Anne Rhode','Jeremy Teeter']
manager_list = ['Anne Rhode','Jeremy Teeter']

#manager_object_list

#needs json of employee data!
for x in range(len(manager_list)):
    manager_list[x] = Manager("Anne",46,45,"who knows")
print(manager_list[0])
print(manager_list[1])
