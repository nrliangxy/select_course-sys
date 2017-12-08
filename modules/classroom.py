class ClassRoom(object):
    def __init__(self, class_name, course_obj):
        self.class_name = class_name
        self.course_obj = course_obj
        self.class_student = {}
