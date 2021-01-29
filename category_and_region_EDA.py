# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 09:51:48 2021

@author: TylerFeldman

Finds number of images, turbines (including small and large), and turbines/image 
for each region and each category
"""

import glob
import os

IMG_DIR = r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\\'
LBL_DIR = r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Multiclass Data\labels\\'

categories = ['deserts', 'farmlands', 'forests', 'grasslands', 'urban_suburban', 'water']
regions = {'SW' : ['CA', 'AZ', 'TX', 'NM', 'NV', 'UT', 'CO'], 
              'NE': ['VT', 'MD', 'ME', 'NH', 'PA', 'NJ', 'NY', 'MA', 'DE'],
              'NW': ['WA', 'ID', 'OR', 'MT'],
              'EM': ['MI', 'MN', 'MO', 'WI', 'IN', 'IA', 'IL', 'OH'],
              'WM': ['ND', 'OK', 'KS', 'SD', 'NE']}

def get_file_name(path):
    return path.split('\\')[-1]

def get_state(path):
    return path.split('\\')[-1].split('_')[2]

for region in regions:
    image_paths = [path for path in glob.glob(IMG_DIR + 'images\\*.jpg') if get_state(path) in regions[region]]
    label_paths = [LBL_DIR + get_file_name(path).replace('.jpg', '.txt') for path in image_paths]
    num_images = len(image_paths)
    
    num_turbines = 0
    small_turbines = 0
    large_turbines = 0
    for label in label_paths:
        if not os.path.exists(label):
            continue
        
        with open(label, 'r') as f:
            for line in f:
                num_turbines += 1
                if (line[0] == '1'):
                    small_turbines += 1
                else:
                    large_turbines += 1
                    
    turbines_per_image = num_turbines / num_images                
    print(f'For {region},\nNumber of Images: {num_images}\nNumber of Turbines: {num_turbines}\nNumber of Small Turbines: {small_turbines}\nNumber of Large Turbines: {large_turbines}\nNumber of turbines per image: {turbines_per_image}')
    

for category in categories:
    image_paths = glob.glob(IMG_DIR + category + '\\*.jpg')
    label_paths = [LBL_DIR + get_file_name(path).replace('.jpg', '.txt') for path in image_paths]
    num_images = len(image_paths)
    
    num_turbines = 0
    small_turbines = 0
    large_turbines = 0
    for label in label_paths:
        if not os.path.exists(label):
            continue
        
        with open(label, 'r') as f:
            for line in f:
                num_turbines += 1
                if (line[0] == '1'):
                    small_turbines += 1
                else:
                    large_turbines += 1
                    
    turbines_per_image = num_turbines / num_images                
    print(f'For {category},\nNumber of Images: {num_images}\nNumber of Turbines: {num_turbines}\nNumber of Small Turbines: {small_turbines}\nNumber of Large Turbines: {large_turbines}\nNumber of turbines per image: {turbines_per_image}')

    
    
