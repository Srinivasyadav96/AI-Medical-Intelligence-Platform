'''import os
import tensorflow as tf
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, "ml", "model.keras")

model = tf.keras.models.load_model(MODEL_PATH)'''

import os
import tensorflow as tf
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, "ml", "model.keras")

_model = None

def get_model():
    global _model

    if _model is None:
        _model = tf.keras.models.load_model(MODEL_PATH)

    return _model