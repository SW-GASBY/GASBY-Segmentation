
court segmentation - v4 2024-01-09 11:16pm
==============================

This dataset was exported via roboflow.com on June 29, 2024 at 5:49 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 1566 images.
Basketball-court are annotated in COCO for MMDetection format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Random rotation of between -11 and +11 degrees
* Random shear of between -13° to +13° horizontally and -14° to +14° vertically
* Random exposure adjustment of between -14 and +14 percent
* Random Gaussian blur of between 0 and 4.6 pixels
* Salt and pepper noise was applied to 1.88 percent of pixels


