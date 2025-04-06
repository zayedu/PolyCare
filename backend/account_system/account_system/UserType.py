'''
There are three types of users that will be using this app. 
The categories are defined below:

1: Patient: The person who will be using the app for the purposes of determining 
the likelihood of having PCOS.

2: Physician: The doctor(s) that may use the patient's likelihood calculation
to assist in determining next steps in the patient's care.

3: HCN: The healthcare providers that may find the calculation helpful in 
navigating the patient's health journey
'''

class UserType:
    PATIENT = 1
    PHYSICIAN = 2
    HCN = 3

    @classmethod
    def get_name(cls, value):
        if value in {'Patient', 'Physician', 'HCN'}:   #in case the input is the name itself
             return value
        
        if isinstance(value, str) and hasattr(cls, value.upper()):
             result = getattr(cls, value.upper())
             return cls.get_name(result)
    
        names = {
            1: 'Patient',
            2: 'Physician',
            3: 'HCN'
        }
        return names.get(value)

    
         
    @classmethod
    def get_value(cls, name):
        if hasattr(cls, name.upper()):
            return getattr(cls, name.upper())
        map_val = {'Patient': cls.PATIENT, 'Physician': cls.PHYSICIAN, 'HCN': cls.HCN}
        return map_val.get(name)

'''
def main():
    user_type_value = 2
    user_type_name = UserType.get_name(user_type_value)
    print(f"The name of the user type with the value {user_type_value} is: {user_type_name}")
    user_name = UserType.get_value('PATIENT')
    print (user_name)
    print(UserType.get_name(1))
    print(UserType.get_name('PATIENT'))
    print(UserType.get_name('Patient'))
    print(UserType.get_name(UserType.PHYSICIAN))
   


if __name__ == '__main__':
        main()

'''