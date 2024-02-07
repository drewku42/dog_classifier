import os
import tensorflow as tf
from dotenv import load_dotenv
from keras.applications import MobileNetV2
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
from data_preprocessing import load_dataset
from label_encoding import LabelEncoderWrapper
from sklearn.model_selection import train_test_split

def main():
    # Load dataset, preprocess images and labels, encode labels, etc.
    load_dotenv()
    annotations_dir = os.getenv('ANNOTATIONS_DIR')
    images_dir = os.getenv('IMAGES_DIR')
    images, breeds = load_dataset(annotations_dir, images_dir)
    encoder = LabelEncoderWrapper()
    integers = encoder.fit_transform(breeds)
    y_onehot = encoder.encode_to_one_hot(integers)
    X_train, X_test, y_train, y_test = train_test_split(images, y_onehot, test_size=0.2, random_state=42)

    # Define data augmentation
    data_augmentation = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input
    )

    # Define the model
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(len(encoder.classes_), activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model with data augmentation
    train_generator = data_augmentation.flow(X_train, y_train, batch_size=32)
    validation_generator = ImageDataGenerator(preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input).flow(X_test, y_test, batch_size=32)
    
    model.fit(
        train_generator,
        steps_per_epoch=len(X_train) // 32,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=len(X_test) // 32
    )

    # Evaluate the model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {test_acc:.4f}")

    # Save the model if test accuracy is 80% or higher
    if test_acc >= 0.8:
        print("Achieved 80%+ accuracy, saving the model.")
        model.save('path/to/save_your_model')
    else:
        print("Did not achieve 80%+ accuracy, not saving the model.")

if __name__ == "__main__":
    main()