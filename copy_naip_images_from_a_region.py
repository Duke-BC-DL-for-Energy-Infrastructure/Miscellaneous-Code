import glob
import os
import shutil

'''
This file takes a directory of images or labels and copies the images in a certain geographic region into the output directory.
These images must be named with the format naip_####_STATE_WND_i#j#.extension.
For example, an image might be named naip_6882_PA_i1j0.jpg and it's corresponding label would be named naip_6882_PA_i1j0.txt.
If the target region is set to 'NE' and extension set to '.jpg, then if this example image (naip_6882_PA_i1j0.jpg) is in the IMG_DIR,
then it will be copied into the OUTPUT_DIR, since is from PA, and PA is in the NE region.
'''

# Directory of where the input images are
IMG_DIR = r'C:\Users\tyler\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Data\images'

# Directory of where to copy the target images to
OUTPUT_DIR = r'C:\Users\tyler\Documents\Bass\Files\images'

target_region = 'ALL' # Target region to filter the images by. For example, if you only want to collect images from NE, then use target_region ='NE
extension = '.jpg' # Could change to .txt for labels
separator = '\\' # Character used to separate directories on your operating system

regions = {'SW' : ['CA', 'AZ', 'TX', 'NM', 'NV', 'UT', 'CO'], 
              'NE': ['VT', 'MD', 'ME', 'NH', 'PA', 'NJ', 'NY', 'MA', 'DE'],
              'NW': ['WA', 'ID', 'OR', 'MT'],
              'EM': ['MI', 'MN', 'MO', 'WI', 'IN', 'IA', 'IL', 'OH'],
              'WM': ['ND', 'OK', 'KS', 'SD', 'NE']}

def get_state(name):
    return name.split('_')[2]

def get_region(name):
    state = get_state(name)
    for key, val in regions.items():
        if state in val:
            return key

files = glob.glob(IMG_DIR + separator + '*' + extension)
files = [path for path in files if path.split(separator)[-1].split('.')[0].split('_')[0] == 'naip'] # Get just the naip image names
files = [path for path in files if (get_region(path.split(separator)[-1].split('.')[0]) == target_region or target_region == 'ALL')]

# Copy the files to the other directory
for src in files:
    dst = OUTPUT_DIR + separator + src.split(separator)[-1]
    print(src, dst)
    shutil.copy(src, dst)
