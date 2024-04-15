import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load dataset
data = pd.read_csv('pg_prices_and_diseases.csv')

# Create dictionaries from dataset
area_to_pg_price = dict(zip(data['Area'], data['PG_Price']))
area_to_disease = dict(zip(data['Area'], data['Disease']))


def predict_prices_and_disease():
    area = area_entry.get().lower()

    if area in area_to_pg_price:
        pg_price = area_to_pg_price[area]
        disease = area_to_disease[area]
        messagebox.showinfo("Prediction",
                            f"Basic price of PG rooms in {area}: {pg_price}\n\nMajor disease in {area}: {disease}")
    else:
        messagebox.showerror("Error", "Area not found in database. Please enter a valid area.")


# Create GUI window
root = tk.Tk()
root.title("PG Prices and Disease Prediction Application")

# Create input field for area
area_label = tk.Label(root, text="Enter Area:")
area_label.pack()
area_entry = tk.Entry(root)
area_entry.pack()

# Create predict button
predict_button = tk.Button(root, text="Predict Prices & Disease", command=predict_prices_and_disease)
predict_button.pack()

# Run the GUI application
root.mainloop()
