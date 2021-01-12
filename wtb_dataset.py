"""
This file reads and creates specific power plants imagery from the `Power Plant Imagery` dataset
(https://figshare.com/articles/Power_Plant_Satellite_Imagery_Dataset/5307364) and convert it to a format that can be
annotated. It also adds the masks in this dataset to highlight the region of the power plant
"""


# Built-in
import os

# Libs
import numpy as np
import toolman as tm
from PIL import Image
from tqdm import tqdm

# Settings
DATA_DIR = r'C:\Users\Tyler Feldman\Documents\Data+\5307364'              # the home directory of the unzipped files
SAVE_DIR = r'C:\Users\Tyler Feldman\Documents\Data+\5307364\masked_imgs'  # path of image files you want to save for annotation
FUEL_TYPE = 'WND' # Type of powerplant for which to collect the images


def get_fuel_type(file_name):
    return tm.misc_utils.get_file_name_no_extension(file_name).split('_')[-1]


def get_tile_id(file_name):
    return tm.misc_utils.get_file_name_no_extension(file_name).split('_')[1]


def check_fuel_types(fold_name):
    img_names = tm.misc_utils.get_files(os.path.join(fold_name, 'uspp_naip'), '*.tif')
    fuel_types = [get_fuel_type(a) for a in img_names]
    return set(fuel_types)


def get_files(fold_name, fuel_type):
    img_dir = os.path.join(fold_name, 'uspp_naip')
    mask_dir = os.path.join(fold_name, 'annotations', 'annotations', 'binary')
    img_names = tm.misc_utils.get_files(img_dir, '*.tif')
    select_imgs = [a for a in img_names if get_fuel_type(a) == fuel_type]

    return [(a, os.path.join(mask_dir, 'bilabels_{}.png'.format(get_tile_id(a)))) for a in select_imgs]


def save_imgs(file_list, save_fold=None, vis=True):
    for rgb_img_file, lbl_img_file in tqdm(file_list):
        rgb_img = tm.misc_utils.load_file(rgb_img_file)[:, :, :3]
        lbl_img = np.array(Image.open(lbl_img_file).resize(rgb_img.shape[:2][::-1], Image.BILINEAR))
        lbl_img = np.stack([lbl_img, lbl_img, lbl_img], axis=-1)
        np.testing.assert_equal(rgb_img.shape, lbl_img.shape)
        masked_img = (rgb_img * 0.85 + lbl_img * 0.15).astype(np.uint8)

        if vis:
            tm.vis_utils.compare_figures([rgb_img, lbl_img, masked_img], (1, 3), (12, 4))

        if save_fold:
            save_name = '{}_masked.jpg'.format(tm.misc_utils.get_file_name_no_extension(rgb_img_file))
            tm.misc_utils.save_file(os.path.join(save_fold, save_name), masked_img)


if __name__ == '__main__':
    img_gt_pairs = get_files(DATA_DIR, FUEL_TYPE)
    save_imgs(img_gt_pairs, save_fold=SAVE_DIR, vis=False)
    