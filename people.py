import os
import json
from subprocess import check_output

user_data = {}
user_names = []

for user_name in os.listdir('/home'):
    if user_name not in ['aquota.user','lost+found']:
        user_names.append(user_name)

for user_name in user_names:

    if user_name not in user_data:
        user_data[user_name] = {}

    for file_name in ['.plan','.project']:
        file_path = "/home/%s/%s" % (user_name,file_name)
        if os.path.isfile(file_path):
            with open(file_path, "r") as file_pointer:
                user_data[user_name][file_name]=file_pointer.read()

    last = check_output(['last','-wn1',user_name]).split('\n')[0].split()
    ent = check_output(['getent','passwd',user_name]).split(":")

    user_data[user_name]['last_login'] = " ".join(last[4:])
    user_data[user_name]['shell'] = ent[6].replace("\n","")

print(user_data)
