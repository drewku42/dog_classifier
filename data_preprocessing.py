import os
import numpy as np
from dotenv import load_dotenv
from PIL import Image
import xml.etree.ElementTree as ET

def parse_annotation(annotation_path):
    '''Given an annotation path, returns the breed and bounding box of the dog image.'''
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    bndbox = root.find(".//bndbox")
    coords = {'xmin': int(bndbox.find('xmin').text),
              'ymin': int(bndbox.find('ymin').text),
              'xmax': int(bndbox.find('xmax').text),
              'ymax': int(bndbox.find('ymax').text)}
    breed = root.find(".//name").text
    return breed, coords

def load_and_preprocess_image(image_path, coords, target_size=(224, 224)):
    '''Given an image path and bounding box coords, returns a preprocessed image.'''
    image = Image.open(image_path).convert('RGB')  # Convert image to RGB
    image = image.crop((coords['xmin'], coords['ymin'], coords['xmax'], coords['ymax']))
    image = image.resize(target_size)
    return np.array(image)

def load_dataset(annotations_dir, images_dir):
    '''Loads and preprocesses the dataset from given directories.'''
    images = []  # initialize list of images
    breeds = []  # initialize list of breeds

    for breed_dir in os.listdir(annotations_dir):
        breed_path = os.path.join(annotations_dir, breed_dir)
        for annotation_file in os.listdir(breed_path):
            annotation_path = os.path.join(breed_path, annotation_file)
            breed, coords = parse_annotation(annotation_path)

            image_file = annotation_file + '.jpg'
            image_path = os.path.join(images_dir, breed_dir, image_file)
            image = load_and_preprocess_image(image_path, coords)

            images.append(image)
            breeds.append(breed)

    return np.array(images), np.array(breeds)

def main():
    '''Main function to execute preprocessing steps.'''
    load_dotenv()
    annotations_dir = os.getenv('ANNOTATIONS_DIR')
    images_dir = os.getenv('IMAGES_DIR')

    if annotations_dir is None or images_dir is None:
        raise ValueError("Please set ANNOTATIONS_DIR and IMAGES_DIR in your .env file")

    images, breeds = load_dataset(annotations_dir, images_dir)
    print(f"Loaded {len(images)} images and {len(breeds)} breeds.")

if __name__ == "__main__":
    main()