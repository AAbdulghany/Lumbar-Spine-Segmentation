import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import os

def load_nifti_file(filepath):
    img = nib.load(filepath)
    img_data = img.get_fdata()
    return img_data

def save_slice_yz(img_data, slice_index, output_path, file_name):
    plt.figure(figsize=(8, 8))
    plt.imshow(img_data[slice_index, :, :], cmap='gray')
    plt.axis('off')
    output_file = os.path.join(output_path, f"{file_name}_slice_{slice_index}.png")
    plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
    plt.close()

# Paths to the provided files --Change based on you reference
base_path = "/Users/saiffouda/WorkingSpace_code/DL/Project/Structure/nnUNet_preprocessed/Dataset001_LumbarSpine/gt_segmentations"
output_path = "/Users/saiffouda/WorkingSpace_code/DL/Project/nnU-Net_Code/pythonProject/segmentation_output"
file_names = [
    "BRATS_001.nii.gz",
    "BRATS_002.nii.gz",
    "BRATS_003.nii.gz",
    "BRATS_004.nii.gz",
    "BRATS_005.nii.gz",
    "BRATS_007.nii.gz",
    "BRATS_008.nii.gz",
    "BRATS_009.nii.gz",
    "BRATS_010.nii.gz"
]

# Ensure the output directory exists
os.makedirs(output_path, exist_ok=True)

# Save middle slice for each file along the y-z axis
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    img_data = load_nifti_file(file_path)
    middle_slice = img_data.shape[0] // 2  # Take the middle slice along the y-z axis
    save_slice_yz(img_data, middle_slice, output_path, os.path.splitext(file_name)[0])
