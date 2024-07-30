import tkinter as tk
from tkinter import messagebox
import pickle

# Load the model and feature extraction
with open('spam_model.model', 'rb') as f:
    loaded_data = pickle.load(f)

loaded_model = loaded_data['model']
loaded_feature_extraction = loaded_data['feature_extraction']

def predict(message):
    input_mail = [message]
    input_data_features = loaded_feature_extraction.transform(input_mail)
    prediction = loaded_model.predict(input_data_features)
    
    if prediction[0] == 1:
        return 'Not Spam mail'
    else:
        return 'Spam mail'

def on_predict():
    user_input = entry.get()
    result = predict(user_input)
    messagebox.showinfo("Prediction Result", result)

# Create the main window
root = tk.Tk()
root.title("Spam Detector")

# Create and place the widgets
label = tk.Label(root, text="Enter your mail to check:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Check", command=on_predict)
button.pack(pady=10)

# Run the application
root.mainloop()
