def evaluate_model(model, test_data_path):
    """
    Evaluates trained AI model on resonance lattice test data.
    """
    import pandas as pd
    from sklearn.metrics import mean_squared_error

    test_data = pd.read_csv(test_data_path)
    X_test = test_data[["frequency", "observer_angle"]]
    y_true = test_data[["forci", "flui", "freqi"]]

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_true, y_pred)

    print(f"Model MSE on test set: {round(mse, 5)}")
    return mse
