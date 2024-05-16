import csv
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert_csv_to_json(csv_file_path, json_file_path):
    # Read the CSV and convert it to a JSON array.
    data = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        # Convert each row into a dictionary and add it to data.
        for rows in csv_reader:
            data.append(rows)

    # Write the JSON output to a file.
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    messagebox.showinfo("Success", "CSV has been converted to JSON successfully!")

def open_csv_file():
    file_path = filedialog.askopenfilename(
        title="Open CSV File",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )

    if not file_path:  # If the user cancels, do nothing.
        return

    save_path = filedialog.asksaveasfilename(
        title="Save as JSON",
        filetypes=(("JSON files", "*.json"), ("All files", "*.*")),
        defaultextension=".json"
    )

    if not save_path:  # If the user cancels, do nothing.
        return

    convert_csv_to_json(file_path, save_path)

# Set up the tkinter GUI
root = tk.Tk()
root.title("CSV to JSON Converter")

# Create and place a button to open the file dialog
open_button = tk.Button(root, text="Open CSV and Convert to JSON", command=open_csv_file)
open_button.pack(expand=True, pady=50, padx=50)

# Run the GUI event loop
root.mainloop()