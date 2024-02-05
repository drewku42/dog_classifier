# Import Necessary Libararies
import os
import xml.etree.ElementTree as ET
import tensorflow as tf
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical # FIX


# 1.1: Parse Annotations
# Here I have defined a function which parses XML annotation to obtain the boundary boxes of each dog.
def parse_annotation(annotation_path):
    '''Given an annotation path, returns the boundary box of the dog image.'''
    tree = ET.parse(annotation_path)  # parse XML element tree
    root = tree.getroot()  # start at root
    bndbox = root.find(".//bndbox")  # search for bound box nodes
    coords = { 'xmin': int(bndbox.find('xmin').text),
               'ymin': int(bndbox.find('ymin').text),
               'xmax': int(bndbox.find('xmax').text),
               'ymax': int(bndbox.find('ymax').text) }
    breed = root.find(".//name").text  # obtain coordinates
    return breed, coords

# 1.2 Preprocessing
# This function is responsible for loading, cropping, and resizing and image such that it fits the boundary box to the 224x224 px images for training
def load_and_preprocess_image(image_path, coords, target_size=(224, 224)):
    '''Given an image path, adjusts the image to fit the dog within a 224x224 px image.'''
    image = Image.open(image_path)  # Load the image
    image = image.crop((coords['xmin'], coords['ymin'], coords['xmax'], coords['ymax']))  # Crop the image using the bounding box coordinates
    image = image.resize(target_size)  # Resize the image to the target size
    return image

