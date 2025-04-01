import os
from PIL import Image
import tensorflow as tf
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from keras.src.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import time

def clean_directory(dir_path, valid_extensions=('.png', '.jpg', '.jpeg')):
    """
    Walk through the directory and remove:
      - Hidden files (e.g., .DS_Store)
      - Files with non-image extensions
      - Corrupted image files that cannot be opened
    """
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Remove hidden files
            if file.startswith('.'):
                print(f"Removing hidden file: {file_path}")
                os.remove(file_path)
                continue
            # Remove files without valid image extensions
            if not file.lower().endswith(valid_extensions):
                print(f"Removing non-image file: {file_path}")
                os.remove(file_path)
                continue
            # Attempt to open the image to detect corrupt files
            try:
                with Image.open(file_path) as img:
                    img.verify()  # verify image integrity
            except Exception as e:
                print(f"Removing corrupt file: {file_path}")
                os.remove(file_path)

def main():
    # Set a random seed for reproducibility
    tf.keras.utils.set_random_seed(12)

    # Define dataset directories
    train_data_dir = "dataset/train"  # Contains subfolders: infected, notinfected
    test_data_dir  = "dataset/test"   # Contains subfolders: infected, notinfected

    # Clean the dataset directories
    print("Cleaning training directory...")
    clean_directory(train_data_dir)
    print("Cleaning test directory...")
    clean_directory(test_data_dir)

    # Hyperparameters
    batch_size = 32        # You can reduce this further if needed
    img_height = 224       # Lowering to 128 can also reduce computation
    img_width  = 224
    epochs = 20
    learning_rate = 0.001

    # Data augmentation with ImageDataGenerator (includes validation split)
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        horizontal_flip=True,
        vertical_flip=True,
        rotation_range=20,
        zoom_range=0.2,
        shear_range=0.2,
        fill_mode='nearest'
    )

    # Create training data generator (80% of data)
    train_generator = datagen.flow_from_directory(
        directory=train_data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',  # Two classes -> output shape (batch, 2)
        classes=['infected', 'notinfected'],  # Ensures consistent class order
        subset='training',
        seed=12
    )

    # Create validation data generator (20% of data)
    val_generator = datagen.flow_from_directory(
        directory=train_data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        classes=['infected', 'notinfected'],
        subset='validation',
        seed=12
    )

    # Create a test dataset (set label_mode to 'categorical' for one-hot labels)
    test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        test_data_dir,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        label_mode='categorical'
    )

    # Build a smaller, lightweight CNN model
    model = Sequential([
        Conv2D(16, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
        MaxPooling2D(2, 2),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        GlobalAveragePooling2D(),  # Significantly reduces parameters versus Flatten
        Dense(32, activation='relu'),
        Dense(2, activation='softmax')
    ])

    # Compile the model using categorical crossentropy for two classes
    model.compile(optimizer=Adam(learning_rate=learning_rate),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Early stopping callback to stop training if validation loss stops improving
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, verbose=1)

    # Train the model
    history = model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=epochs,
        callbacks=[early_stopping],
        verbose=1
    )

    # Plot the training and validation loss over epochs
    plt.figure()
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Loss vs. Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    #plt.show()

    # Plot the training and validation accuracy over epochs
    plt.figure()
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Accuracy vs. Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    #plt.show()

    # Evaluate the model on the test set
    test_loss, test_acc = model.evaluate(test_dataset)
    print(f"Test Accuracy: {test_acc:.4f}, Test Loss: {test_loss:.4f}")

    # Save the trained model; this architecture is much smaller, so the h5 file will be well under 100MB.
    model.save("ultrasound_pcos_model.h5")
    print("Model saved to ultrasound_pcos_model.h5")

if __name__ == '__main__':
    start = time.time()
    main()
    print("Time taken:", time.time() - start, "seconds")