__author__="xiaoyong.liang"
import os
from core import main
from conf import settings
import sys
import platform
if platform.system() == "Linux":
    # BASE_DIR1 = os.path.abspath(os.path.dirname(__file__))
    BASE_DIR = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-1])
else:
    BASE_DIR =  "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
# print(BASE_DIR)
# print(sys.path)
# print(len(sys.path))
sys.path.insert(0, BASE_DIR)
# print(sys.path)
# print(len(sys.path))
if __name__ == '__main__':
    obj = main.Manage_center()
    obj.run()
