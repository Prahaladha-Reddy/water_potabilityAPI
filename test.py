from joblib import load

model_path = 'C:/Users/bored/Music/Water_Potability/model.joblib'

try:
    model = load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
