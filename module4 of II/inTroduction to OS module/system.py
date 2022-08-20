import os

#system fun can replace all other fun
#the command is passed as a string to the system function
os.system('mkdir system_dir')  
print(os.system('dir'))
os.system('del system_dir')
print(os.system('dir'))