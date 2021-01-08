# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:04:14 2020

@author: TylerFeldman

Used to generate a histogram of number of images per state given a folder of overhead images of wind turbines
that follow a naming convention like naip_325_AZ_...
"""

import toolman as tm
import seaborn as sns
import matplotlib.pyplot as plt

# DATA_DIR Path to NAIP Imagery. The NAIP imagery must have a name convention like naip_325_AZ_WND_...
# where the third piece of information is the state, and the information is separated by underscores
DATA_DIR =r'C:\Users\Tyler Feldman\Documents\Data+\5307364\masked_imgs'

images = tm.misc_utils.get_files(DATA_DIR, '*.jpg')

print(len(images))

def get_state(file_name):
    return tm.misc_utils.get_file_name_no_extension(file_name).split('_')[2]


state_names = []
state_instances = []

for image in images:
    state = get_state(image)
    if state in state_names:
        state_instances[state_names.index(state)] += 1
    else:
        state_names.append(state)
        state_instances.append(1)

zipped_lists = zip(state_instances, state_names)
sorted_pairs = sorted(zipped_lists, reverse=True)
tuples = zip(*sorted_pairs)
state_instances, state_names = [list(tuple) for tuple in tuples]


for i in range(len(state_names)):
    print(state_names[i], state_instances[i])
    
fig, ax = plt.subplots(figsize=(20,10))
ax = sns.barplot(state_names, state_instances, palette="Blues_d")
plt.xlabel("State")
plt.ylabel("Number of Images")
plt.title("Number of Images Grouped by State")