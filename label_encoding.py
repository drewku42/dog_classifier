from sklearn.preprocessing import LabelEncoder
from tensorflow.python.keras.utils.np_utils import to_categorical

class LabelEncoderWrapper:
    def __init__(self):
        self.label_encoder = LabelEncoder()
        self.classes_ = None

    def fit_transform(self, labels):
        """Encodes label data to integers."""
        integers = self.label_encoder.fit_transform(labels)
        self.classes_ = self.label_encoder.classes_  # Store class names for inverse transform
        return integers

    def transform(self, labels):
        """Transforms labels to integers without fitting."""
        return self.label_encoder.transform(labels)

    def inverse_transform(self, integers):
        """Converts integer-encoded labels back to original breed names."""
        return self.label_encoder.inverse_transform(integers)

    def encode_to_one_hot(self, integers, num_classes=None):
        """Converts integer-encoded labels to one-hot encoded vectors."""
        if num_classes is None:
            num_classes = len(self.classes_)
        return to_categorical(integers, num_classes=num_classes)

