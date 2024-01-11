import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, BatchNormalization, Dropout


def crear_modelo():
    model = Sequential()

    # Capa de convolución con normalización y dropout
    model.add(Conv2D(128, (3, 3), activation='relu', input_shape=(8, 8, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    # Otra capa de convolución con normalización y dropout
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    # Capa de aplanamiento y capas densas con dropout
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(256, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    # Capa de salida con activación lineal para la predicción del próximo movimiento
    model.add(Dense(1, activation='linear'))

    # Compilación del modelo
    model.compile(optimizer='adam', loss='mean_squared_error')

    return model

# Resto del código (entrenamiento, guardado, etc.) sigue siendo el mismo


# Ejemplo de uso
modelo = crear_modelo()
