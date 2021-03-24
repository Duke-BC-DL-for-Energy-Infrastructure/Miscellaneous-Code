import csv
import glob

def get_state(name):
    return name.split('_')[2]

def get_region(name):
    state = get_state(name)
    for key, val in regions.items():
        if state in val:
            return key

regions = {'SW' : ['CA', 'AZ', 'TX', 'NM', 'NV', 'UT', 'CO'], 
              'NE': ['VT', 'MD', 'ME', 'NH', 'PA', 'NJ', 'NY', 'MA', 'DE'],
              'NW': ['WA', 'ID', 'OR', 'MT'],
              'EM': ['MI', 'MN', 'MO', 'WI', 'IN', 'IA', 'IL', 'OH'],
              'WM': ['ND', 'OK', 'KS', 'SD', 'NE']}

EM_image_paths = glob.glob(r'C:\Users\Student\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Cross Domain\EM_new\images\*.jpg')
NE_image_paths = glob.glob(r'C:\Users\Student\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Cross Domain\NE_new\images\*.jpg')
NW_image_paths = glob.glob(r'C:\Users\Student\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Cross Domain\NW_new\images\*.jpg')

# Paths and names for all of the 608x608 images
image_paths = EM_image_paths + NE_image_paths + NW_image_paths # Concatentate all the lists of paths
image_names = [path.split('\\')[-1].split('.')[0] for path in image_paths if path.split('\\')[-1].split('.')[0].split('_')[0] == 'naip'] # Get just the naip image names
image_names = [img for img in image_names if (get_region(img) == 'NE')]


parent_image_coordinates = {}

# Parse the geojson file to get coordinates of each 1114x1114 parent image
with open('tiles.geojson') as f:
    lines = f.read()
    entries = lines.split('"description": ')[1:]
    for entry in entries:
        img_name = entry.split('"')[1]
        coordinates = entry.split('[[[')[1].split(']')[0]
        parent_image_coordinates[img_name] = coordinates

# For each image, get the coordinates of it (which we assume are the same as the parent image), and write name,lon,lat into csv
with open('naip_image_coordinates.csv', mode='w', newline='') as naip_image_coordinates:
    writer = csv.writer(naip_image_coordinates, delimiter=',')
    writer.writerow(['name', 'lon', 'lat'])
    for image_name in image_names:
        parent_image = '_'.join(image_name.split('_')[:-1])
        image_coordinate = parent_image_coordinates[parent_image]
        image_coordinate_pair = image_coordinate.replace(',','').split(' ')
        writer.writerow([image_name, image_coordinate_pair[0], image_coordinate_pair[1]])
