import tkinter as tk
from tkinter import messagebox, ttk
import joblib
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the trained model
model = joblib.load("gradient_boosting_model.pkl")

# Define the feature names
feature_names = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms", 
    "Population", "AveOccup", "Latitude", "Longitude"
]

# Function to save the prediction and features to a CSV file
def save_prediction(features, prediction):
    try:
        # Open the CSV file in append mode
        with open("predictions.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # Write the header if the file is empty
            if file.tell() == 0:
                writer.writerow(feature_names + ["Prediction"])
            # Write the features and prediction
            writer.writerow(features + [prediction[0]])
        messagebox.showinfo("Save", "Prediction saved to predictions.csv!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save prediction: {str(e)}")

# Function to make predictions and update the charts
def predict():
    try:
        # Get the input values from the entry fields
        features = []
        for i, entry in enumerate(entries):
            value = entry.get()
            if not value:
                messagebox.showerror("Error", f"Please enter a value for {feature_names[i]}.")
                return
            try:
                features.append(float(value))
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {feature_names[i]}. Please enter a number.")
                return

        # Convert the features to a numpy array
        features_array = np.array(features).reshape(1, -1)

        # Make a prediction
        prediction = model.predict(features_array)

        # Show the prediction in a message box
        messagebox.showinfo("Prediction", f"Predicted House Value: {prediction[0]:.2f}")

        # Save the prediction and features to a CSV file
        save_prediction(features, prediction)

        # Update the charts
        update_chart(features, prediction[0])
        update_scatter_plot(features, prediction[0])
        update_histogram(prediction[0])

    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to update the bar chart
def update_chart(features, prediction):
    # Clear the previous chart
    ax1.clear()

    # Plot the input features
    ax1.bar(feature_names, features, color='blue', label='Input Features')

    # Plot the predicted house value
    ax1.bar("Prediction", prediction, color='red', label='Predicted House Value')

    # Add labels and title
    ax1.set_xlabel("Features")
    ax1.set_ylabel("Value")
    ax1.set_title("Input Features and Predicted House Value")
    ax1.legend()

    # Redraw the chart
    canvas1.draw()

# Function to update the scatter plot
def update_scatter_plot(features, prediction):
    # Clear the previous chart
    ax2.clear()

    # Plot the relationship between MedInc and the predicted house value
    ax2.scatter(features[0], prediction, color='green', label='MedInc vs Prediction')

    # Add labels and title
    ax2.set_xlabel("MedInc")
    ax2.set_ylabel("Predicted House Value")
    ax2.set_title("MedInc vs Predicted House Value")
    ax2.legend()

    # Redraw the chart
    canvas2.draw()

# Function to update the histogram
def update_histogram(prediction):
    # Clear the previous chart
    ax3.clear()

    # Load all predictions from the CSV file
    try:
        with open("predictions.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            predictions = [float(row[-1]) for row in reader]
    except FileNotFoundError:
        predictions = []

    # Add the current prediction to the list
    predictions.append(prediction)

    # Plot the histogram
    ax3.hist(predictions, bins=10, color='purple', edgecolor='black', label='Predicted House Values')

    # Add labels and title
    ax3.set_xlabel("Predicted House Value")
    ax3.set_ylabel("Frequency")
    ax3.set_title("Distribution of Predicted House Values")
    ax3.legend()

    # Redraw the chart
    canvas3.draw()

# Function to load previous predictions
def load_predictions():
    try:
        # Clear the previous table
        for row in table.get_children():
            table.delete(row)

        # Open the CSV file and read the data
        with open("predictions.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row
            for row in reader:
                table.insert("", "end", values=row)
    except FileNotFoundError:
        messagebox.showerror("Error", "No predictions found. Please make a prediction first.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load predictions: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("California Housing Price Predictor")

# Create input fields for each feature
entries = []
for i, feature in enumerate(feature_names):
    # Create a label for the feature
    label = tk.Label(root, text=f"{feature}:")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    # Create an entry field for the feature
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Create a button to trigger the prediction
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=len(feature_names), column=0, columnspan=2, pady=10)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 3))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=len(feature_names) + 2, column=0, columnspan=2, padx=10, pady=10)

# Create a button to load previous predictions
load_button = tk.Button(root, text="Load Previous Predictions", command=load_predictions)
load_button.grid(row=len(feature_names) + 4, column=0, columnspan=2, pady=10)

# Create a table to display previous predictions
columns = feature_names + ["Prediction"]
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.grid(row=len(feature_names) + 5, column=0, columnspan=2, padx=10, pady=10)
# Run the Tkinter event loop
root.mainloop()