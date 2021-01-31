# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:14:56 2021

@author: TylerFeldman
"""
import random
import glob

def get_file_name(path):
    return path.split('\\')[-1]

def get_state(path):
    return path.split('\\')[-1].split('_')[2]

categories = ['deserts', 'farmlands', 'forests', 'grasslands', 'urban_suburban', 'water']
regions = {'SW' : ['CA', 'AZ', 'TX', 'NM', 'NV', 'UT', 'CO'], 
              'NE': ['VT', 'MD', 'ME', 'NH', 'PA', 'NJ', 'NY', 'MA', 'DE'],
              'NW': ['WA', 'ID', 'OR', 'MT'],
              'EM': ['MI', 'MN', 'MO', 'WI', 'IN', 'IA', 'IL', 'OH'],
              'WM': ['ND', 'OK', 'KS', 'SD', 'NE']}

IMG_DIR = r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\\'
LBL_DIR = r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Multiclass Data\labels\\'
SYN_DIR = r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Synthetic Imagery\synthetic_images\\'

training_paths = [path for path in glob.glob(IMG_DIR + 'images\\*.jpg') if get_state(path) in regions['NW']]
validation_paths = [path for path in glob.glob(IMG_DIR + 'images\\*.jpg') if get_state(path) in regions['NE']]
synthetic_paths = glob.glob(SYN_DIR + '*forests.png')

#training_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\deserts\*.jpg')
#validation_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\farmlands\*.jpg')
#synthetic_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Synthetic Imagery\synthetic_images\farm*.png')
separator = '\\' # Character used to separate directories in the paths that come from calling glob

random.shuffle(training_paths)
random.shuffle(validation_paths)
random.shuffle(synthetic_paths)

training_imgs = open('training_img_paths.txt', 'w')
training_lbls = open('training_lbl_paths.txt', 'w')
for img in training_paths:
    training_imgs.write('../data/images/' + img.split(separator)[-1] + '\n')
    training_lbls.write('../data/labels/' + img.split(separator)[-1].replace('.jpg', '.txt') + '\n')
training_imgs.close()
training_lbls.close()

validation_imgs = open('val_img_paths.txt', 'w')
validation_lbls = open('val_lbl_paths.txt', 'w')
for img in validation_paths:
    validation_imgs.write('../data/images/' + img.split(separator)[-1] + '\n')
    validation_lbls.write('../data/labels/' + img.split(separator)[-1].replace('.jpg', '.txt') + '\n')
validation_imgs.close()
validation_lbls.close()
        
synthetic_imgs = open('syn_img_paths.txt', 'w')
synthetic_lbls = open('syn_lbl_paths.txt', 'w')
for img in synthetic_paths:
    synthetic_imgs.write('../data/synthetic_images/' + img.split(separator)[-1] + '\n')
    synthetic_lbls.write('../data/synthetic_labels/' + img.split(separator)[-1].replace('.png', '.txt') + '\n')
synthetic_imgs.close()
synthetic_lbls.close()
        