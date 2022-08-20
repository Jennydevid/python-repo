import os

os.makedirs("first_directory/second_directory")
os.chdir('first_directory')
print("\n",os.getcwd())

os.chdir('second_directory')
print("\n",os.getcwd())