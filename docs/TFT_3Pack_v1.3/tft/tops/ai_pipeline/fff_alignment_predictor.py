def predict_fff_alignment(model, frequency, angle):
    """
    Uses trained AI model to predict FFF alignment for a given frequency and observer angle.
    """
    import numpy as np

    input_data = np.array([[frequency, angle]])
    prediction = model.predict(input_data)

    return {
        "forci": round(prediction[0][0], 3),
        "flui": round(prediction[0][1], 3),
        "freqi": round(prediction[0][2], 3)
    }
