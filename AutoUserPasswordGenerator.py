# Last Update: 2024/05/04
# Author: Luke Kaser
# Description: A simple program to load new user data and generate a random password for each user
# E-mail: qaz442200156@gmail.com

import csv
import secrets
import subprocess  # for running cmd
from pathlib import Path  # to locate data files

# Before starting, we need to set the current directory to here
cwd = Path.cwd()

input_data_path = cwd / "data/users_in.csv"
output_data_path = cwd / "data/users_out.csv"

# If your csv was saved in `utf-8`
#csv_encoding = 'utf-8'
# If your csv was saved in `utf-8-sig`
csv_encoding = 'utf-8-sig'

with open(input_data_path , "r", encoding=csv_encoding) as file_input, open(output_data_path, "w", encoding=csv_encoding) as file_output:
    # Read the input csv data
    reader = csv.DictReader(file_input)    
    # Prepare writer before writing data (use fieldnames to set up base field names from input csv)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    # Create the same field names as the input csv
    writer.writeheader()

    for user in reader:      
        # Get field by field name e.g., user["username"], user["password"], or user["real_name"]
        '''
        # !!! Add new user account into the system !!!
        for user in new_users:
            if len(user.password) == 0:
                user.password = secrets.token_hex(8)
            useradd_cmd = ["/sbin/useradd",
                        "-c", user["real_name"],
                        "-m",
                        "-G","users",
                        "-p",user.password,
                        user.name]
            subprocess.run(useradd_cmd,check=True)
        '''
        # generate password
        if len(user["password"]) == 0:
            user["password"] = secrets.token_hex(4)
        # write data at a new row
        writer.writerow(user)
        # show result
        print("Added new user: {username:<10} ({real_name:^15}) pw:{password}".
              format(username=user["username"],
                     real_name=user["real_name"],
                     password=user["password"]))
