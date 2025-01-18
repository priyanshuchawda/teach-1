import tensorflow as tf
import numpy as np

# Generate dummy data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input (XOR problem)
y = np.array([[0], [1], [1], [0]])  # Labels

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu'),  # Hidden layer
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
print("Training the model...")
model.fit(X, y, epochs=500, verbose=0)  # Increase epochs to see better results

# Make predictions
print("\nPredictions:")
predictions = model.predict(X)
print(predictions.round())
