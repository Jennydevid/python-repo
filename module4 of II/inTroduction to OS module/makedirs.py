#makedirs is used to create recursive directories i.e. directory within a directory
import os

os.makedirs("my_first_directory//my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
