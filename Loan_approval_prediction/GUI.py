import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

class SelectColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_select):
        self.columns_to_select = columns_to_select

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        return X[self.columns_to_select]

class StripColumnNames(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X.columns = X.columns.str.strip()
        return X

# Function to open the file dialog and load the data file
def load_data_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path)
            predict(data)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the data: {e}")

# Function to make predictions using the loaded model
def predict(data):
    try:
        # Assuming the model expects the data in the same format as your CSV
        predictions = model.predict(data)
        result = predictions[0]

        # Display the result
        if result == 1:
            messagebox.showinfo("Prediction", "Your loan is approved")
        else:
            messagebox.showinfo("Prediction", "Your loan was rejected")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while making a prediction: {e}")

# Load your trained model (.pkl)
def load_model():
    global model
    with open('Loan_approval_prediction/Loan_approval_prediction.pkl', 'rb') as file:
        model = pickle.load(file)

# Create the main application window
root = tk.Tk()
root.title("Loan Prediction")

# Load the model when the application starts
load_model()

# Create a button to load the data file
load_button = tk.Button(root, text="Load Data File", command=load_data_file)
load_button.pack(pady=20)

# Run the application
root.mainloop()
