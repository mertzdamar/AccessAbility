# AccessAbility.py

# Imports 
import time
import sys
import os
import pandas as pd

# Classes
class AccessAbility:
    def __init__(self, ability):
        self.ability = ability
   
    def set_ability(self, ability):
        self.ability = ability
    
    def get_ability(self):
        return self.ability

# Function
def check_accessability(ability):
    if ability == 'yes':
        print('Accessable')
    else:
        print('Not Accessable')

# Define Variables
ability = 'yes'

# Instantiate Class
access_ability = AccessAbility(ability)
    
# Main Routine
if __name__ == "__main__":
    print('Checking Accessability...')
    time.sleep(1)
    check_accessability(access_ability.get_ability())

# Modify Ability Status
access_ability.set_ability('no')

# Recheck Accessability
print('\nRechecking Accessability...')
time.sleep(2)
check_accessability(access_ability.get_ability())

# Output To File
print('\nWriting to file...')
time.sleep(1)
output_file = os.path.join('output.csv')

# Open File
with open(output_file, 'w') as file:
    file.write('Ability,Status\n')

# Write Ability
with open(output_file, 'a') as file:
    file.write(f'{access_ability.get_ability()},Not Accessable\n')

# Read File
print('\nReading data from file...')
time.sleep(2)
data = pd.read_csv('output.csv')
print(data)