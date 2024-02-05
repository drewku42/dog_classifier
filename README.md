# Dog Breed Classifier

## Overview
This repository contains my machine learning project focused on classifying dog breeds using the Stanford Dogs Dataset. The project aims to tackle the challenge of fine-grained image categorization, distinguishing between 120 different breeds of dogs through images.

## Dataset
The Stanford Dogs Dataset, used in this project, comprises over 20,000 images across 120 breeds of dogs from around the world. This dataset has been constructed using images and annotations from ImageNet for the task of fine-grained image categorization.

**Original Dataset**: [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)

**Original Paper**: Aditya Khosla, Nityananda Jayadevaprakash, Bangpeng Yao, and Li Fei-Fei. "Novel dataset for Fine-Grained Image Categorization." First Workshop on Fine-Grained Visual Categorization (FGVC), IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2011.

## Project Structure
- `data_preprocessing.py`: Module for loading, preprocessing, and preparing the dataset for training.
- `label_encoding.py`: Module for encoding dog breed labels into a format suitable for model training.
- `train_model.py`: Main script for defining, training, and evaluating the dog breed classification model.

## Dependencies
- TensorFlow
- NumPy
- scikit-learn
- Pillow (PIL)
- python-dotenv


## License
This project is open source and available under the [MIT License].

## Acknowledgments
Special thanks to the creators of the Stanford Dogs Dataset and to all contributors to the TensorFlow, NumPy, and scikit-learn projects.
