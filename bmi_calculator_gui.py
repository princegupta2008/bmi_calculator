import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight/Height must be positive or greater than 0")

        height = height / 100
        bmi = weight / (height ** 2)

        if bmi <18.5:
            category = "You are Underweight"
        elif 18.5 < bmi < 24.9:
            category = "You weight is Normal"
        elif 25 <= bmi < 29.9:
            category = "You are Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"Your BMI is: {round(bmi, 2)} ({category})")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Enter your Weight (in kg): ").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter your Height (in centimeters [cm]): ").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()