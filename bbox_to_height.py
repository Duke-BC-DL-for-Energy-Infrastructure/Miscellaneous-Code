import glob
import numpy as np

IMG_DIR = r'C:\Users\Tyler Feldman\Documents\Spring 2021 Classes\BassConnections\synthetic data\bbox_to_height_labels'

labels = glob.glob(IMG_DIR + '\*.txt')

sums = [0]*18
counts = [0]*18

for label in labels:
    index = ((int(label.split('\\')[-1].split('.')[0].split('_')[-1])-1) // 3)
    with open(label, 'r') as f:
        bbox = f.read().split('\n')
        if bbox[0] == '':
            continue
        bbox = list(filter(None, bbox))
        area = float(bbox[0].split(' ')[-1]) * float(bbox[0].split(' ')[-2]) * 608 * 608
        sums[index] += area
        counts[index] += 1

print(sums)
print(counts)

avg_areas = [round(sums[i]/counts[i]) for i in range(len(sums)) if sums[i] != 0]
print(avg_areas)
