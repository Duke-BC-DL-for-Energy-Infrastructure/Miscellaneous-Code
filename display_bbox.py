
from PIL import Image, ImageDraw

# Size of the image, in this case 608x608
img_size = (608, 608) # width, height

# Provide the path of the image and its corresponding label
IMG_PATH = r'C:\Users\sarah\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Synthetic Imagery\mar24_four_condition_ALL\newclose_background_new_turbine\NW_extra_images_mar29\NW_wnd_sd0_1_extra.png'
LBL_PATH = r'C:\Users\sarah\Box Sync\Bass Connections 2020-2021\Wind Turbine Object Detection Dataset\Synthetic Imagery\mar24_four_condition_ALL\newclose_background_new_turbine\NW_extra_labels_mar29\NW_wnd_sd0_1_extra.txt'

bboxes = []
with open(LBL_PATH, 'r') as f:
    lines = list(filter(None, f.readlines()))
    lines = [line.replace('\n', '') for line in lines]
    for line in lines:
        bbox = []
        line_split = line.split(' ')
        for i in range(len(line_split)):
            val = line_split[i]
            if i == 0:
                bbox.append(val)
            if i == 1 or i == 3:
                bbox.append(int(float(val)*img_size[0]))
            if i == 2 or i == 4:
                bbox.append(int(float(val)*img_size[1]))
        bboxes.append(bbox) 

img = Image.open(IMG_PATH)
draw = ImageDraw.Draw(img)
for bbox in bboxes:
    draw.rectangle([(bbox[1]-bbox[3], bbox[2]-bbox[4]), (bbox[1]+bbox[3], bbox[2]+bbox[4])])
    draw.text((bbox[1]-bbox[3], bbox[2]-bbox[4]), str(bbox[0]))
img.show()



