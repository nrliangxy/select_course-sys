class Course(object):
    """定义课程：包含名称，价格，周期"""
    def __init__(self, course_name, course_price, course_time):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time
        