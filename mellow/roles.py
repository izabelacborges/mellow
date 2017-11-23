from rolepermissions.roles import AbstractUserRole

class Teacher(AbstractUserRole):
    """
    Essentially this class will control Teachers permissions
    """
    available_permissions = {
        'create_class': True,
        'create_assignment': True,
    }

class Student(AbstractUserRole):
    """
    Essentially this class will control Students permissions
    """
    available_permissions = {
        'edit_patient_file': True,
    }