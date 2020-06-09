import paramiko
import os.path
import time
import sys
import re

#Checking username/password file
#Prompting user for input - Username/Password FILE
user_file = input('\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ')

#Verifying the validity of the Username/Password file
if os.path.isfile(user_file) == True:
    print("\n* Username/Password file is valid :_\n")

else:
    print('\n* File {} does not exist :( Please check and try again.\n'.format(user_file))
    sys.exit()

#Checking commands file
#Prompting user for input - Commands File
cmd_file = input("\n# Enter commands file path and name(e.g. D:\MyApps\myfile.txt): ")

#verifying the validity of the Commands File
if os.path.isfile(cmd_file) == True:
    print('\n* Command file is valid :)\n')
else:
    print('\n* File{} does not exist :( Please check and try again.\n'.format(cmd_file))
    sys.exit
