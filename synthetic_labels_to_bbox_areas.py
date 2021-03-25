import glob
import numpy as np

'''
Given a directory full of YOLOv3 formatted labels, returns a dictionary where the keys are 
the absolute path of the label and value is a list of the areas of the bounding boxes in that label
'''

# Path to the directory where the labels are stored
IMG_DIR = r'C:\Users\sarah\Documents\TYLER\Bass\test_labels'

labels = glob.glob(IMG_DIR + '\*.txt') # Collect labels in given directory

list_of_areas_for_given_label = {}

# Loop through the labels
for label in labels:
    list_of_areas = [] # List of areas for the current label

    with open(label, 'r') as f:
        # Read and split the file into separate elements in list
        bbox_list = f.read().split('\n')
        bbox_list = list(filter(None, bbox_list))

        # For each bounding box in the label, calculate area and append to the list of areas for the current label
        for bbox in bbox_list:
            area = round(float(bbox.split(' ')[-1]) * float(bbox.split(' ')[-2]) * 608 * 608)
            list_of_areas.append(area)
    list_of_areas_for_given_label[label] = list_of_areas # Add item to dictionary

# Print out dictionary
for item in list_of_areas_for_given_label.items():
    print(f'Label: {item[0]}, Areas: {item[1]}')

# With the dictionary done, depending on the setup for the synthetic data, you can calculate average areas if you want:
# Say the first 10 images are done with scale=20, the next 10 are with scale=30, ..., and up to scale=180
# Say the images for scale=20 are named in the format wnd_scale_20_... .txt and so forth for the other scales
# To average the areas for these different scales, you could do:
#
#scales = np.arange(20, 181, 10)
#for scale in scales:
#    labels_for_current_scale = glob.glob(IMG_DIR + '\wnd_scale_{}*.txt'.format(scale)) # to collect all of the scale 20 labels
#    area_sum = 0
#    num_bbox = 0
#    for label in labels_for_current_scale:
#        areas = list_of_areas_for_given_label[label]
#        area_sum += sum(areas)
#        num_bbox += len(areas)
#    average_area = area_sum / num_bbox
#    print(f'Scale: {scale}, Average Area: {}')