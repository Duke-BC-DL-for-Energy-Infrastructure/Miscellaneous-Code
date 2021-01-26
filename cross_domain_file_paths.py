# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:14:56 2021

@author: TylerFeldman
"""
import random
import glob

training_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\deserts\*.jpg')
validation_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Splitting Images into Categories\farmlands\*.jpg')
synthetic_paths = glob.glob(r'C:\Users\Tyler Feldman\Box\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Synthetic Imagery\synthetic_images\farm*.png')
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
        