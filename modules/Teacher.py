class Teacher(object):
    """讲师类定义teacher_name,teacher_salary, 包含teacher_class"""
    
    def __init__(self, teacher_name, teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_class = []
    
    def teacher_add_class(self, class_name, class_obj):
        self.teacher_class[class_name] = class_obj
