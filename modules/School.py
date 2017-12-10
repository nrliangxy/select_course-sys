class School(object):
    """学校类，包含名称，地址，课程，班级，教室"""
    def __init__(self, school_name, school_addr):
        self.school_name = school_name
        self.school_addr = school_addr
        self.school_course = {}
        self.school_class = {}
        self.school_teacher = {}
        