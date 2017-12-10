#-*- coding:utf-8 -*-
__author__="xiaoyong.liang"

import os
import sys
import shelve
from conf import settings
from modules.School import School

class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print("\nwelcome to Class_system \n"
                  "1 student's view\n"
                  "2 teacher's view\n"
                  "3 school's view\n"
                  "q quit\n")
            user_choice = input("\033[34;0m please write your view:\033[0m")
            if user_choice == '1':
                Manage_student()
            elif user_choice == '2':
                Manage_teacher()
            elif user_choice == '3':
                Manage_school()
            elif user_choice == 'q':
                print("\033[34;1m thanks for your use, quit \033[0m")
                break
            else:
                print("\033[31;1m please write valid choice \033[0m")
class Manage_school(object):
    """school view"""
    def __init__(self):
        if