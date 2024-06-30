import json
import os

# Define the base directory
base_dir = '/Users/saiffouda/WorkingSpace_code/DL/Project/Structure/nnUNet_raw/Dataset001_LumbarSpine'

# Define the dataset information
dataset = {
    "channel_names": {
        "0": "MRI"
    },
    "labels": {
        "background": 0,
        "C1": 1,
        "C2": 2,
        "C3": 3,
        "C4": 4,
        "C5": 5,
        "C6": 6,
        "C7": 7,
        "C8": 8,
        "C9": 9,
        "C10": 10,
        "C11": 11,
        "C12": 12,
        "C13": 13,
        "C14": 14,
        "C15": 15,
        "C16": 16,
        "C17": 17,
        "C18": 18,
        "C19": 19,
        "C20": 20
    },
    "numTraining": 9,
    "file_ending": ".nii.gz",
    "overwrite_image_reader_writer": "SimpleITKIO",
    "training": [],
    "test": []
}

# Define paths for images and labels
imagesTr_path = os.path.join(base_dir, 'imagesTr')
labelsTr_path = os.path.join(base_dir, 'labelsTr')
imagesTs_path = os.path.join(base_dir, 'imagesTs')
labelsTs_path = os.path.join(base_dir, 'labelsTs')

# Create training entries
training_cases = [
    "BRATS_001", "BRATS_002", "BRATS_003", "BRATS_004", "BRATS_005",
    "BRATS_007", "BRATS_008", "BRATS_009", "BRATS_010"
]

for case in training_cases:
    training_entry = {
        "image": [os.path.join(imagesTr_path, f"{case}_0000.nii.gz")],
        "label": os.path.join(labelsTr_path, f"{case}.nii.gz")
    }
    dataset["training"].append(training_entry)

# Create test entries
test_cases = ["BRATS_011", "BRATS_012", "BRATS_013"]

for case in test_cases:
    test_entry = {
        "image": [os.path.join(imagesTs_path, f"{case}_0000.nii.gz")],
        "label": os.path.join(labelsTs_path, f"{case}.nii.gz")
    }
    dataset["test"].append(test_entry)

# Save the dataset.json file
with open(os.path.join(base_dir, 'dataset.json'), 'w') as f:
    json.dump(dataset, f, indent=4)

print("dataset.json created successfully.")
