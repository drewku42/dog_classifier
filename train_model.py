# Import necessary modules
from data_preprocessing import load_dataset
from label_encoding import LabelEncoderWrapper
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
import os
# Import your model definition here (e.g., from a separate model.py or directly defined within this script)
# from model import your_model_definition

# import paths
annotation_path = os.env('ANNOTATIONS_DIR')
image_path = os.env('IMAGES_DIR')

def main():
    # Load and preprocess dataset
    images, breeds = load_dataset(annotation_path, image_path)
    
    # Encode labels
    encoder = LabelEncoderWrapper()
    integers = encoder.fit_transform(breeds)
    y_onehot = encoder.encode_to_one_hot(integers)
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(images, y_onehot, test_size=0.2, random_state=42)
    
    # Define and compile model
    model = ... # DEFINE MODEL ARCHITECTURE
    
    # Train model
    model.fit(X_train, y_train, epochs=10, validation_split=0.1)
    
    # Evaluate model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"Test accuracy: {test_acc:.4f}")

if __name__ == "__main__":
    main()
